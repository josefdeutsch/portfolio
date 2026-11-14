#!/usr/bin/env python3
"""Check public portfolio structure and references, not private application claims."""

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PROJECT_IDS = {"qdf", "job-researcher", "prospect-orchestrator"}
DOCUMENTS = {
    "overview": "README.md",
    "decisions": "DECISIONS.md",
    "examples": "EXAMPLES.md",
    "architecture": "ARCHITECTURE.md",
    "engineering": "ENGINEERING.md",
    "operations": "OPERATIONS.md",
    "evidence": "EVIDENCE.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_file(relative):
    require(isinstance(relative, str) and relative, "Expected a nonempty file path")
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT), f"Path escapes repository: {relative}")
    require(path.is_file(), f"Missing file: {relative}")
    return path


def valid_date(value):
    require(isinstance(value, str), "Date must be an ISO string")
    require(date.fromisoformat(value).isoformat() == value, f"Invalid date: {value}")


def unique_ids(items, label):
    require(isinstance(items, list) and items, f"Missing {label}")
    identifiers = [item["id"] for item in items]
    require(all(isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9-]*", value)
                for value in identifiers), f"Invalid ID in {label}")
    require(len(identifiers) == len(set(identifiers)), f"Duplicate ID in {label}")
    return set(identifiers)


def check_index():
    index = json.loads(local_file("portfolio.json").read_text(encoding="utf-8"))
    require(index["schema_version"] == 1, "Unsupported index schema version")
    require(index["repository_kind"] == "documentation_portfolio", "Wrong repository kind")
    valid_date(index["content_baseline_date"])
    require(index["implementation_access"]["visibility"] == "private", "Check source visibility")
    require(index["evidence_policy"]["application_tests_executed_in_this_repository"] is False,
            "Do not claim private tests were run here")
    projects = index["projects"]
    require(unique_ids(projects, "projects") == PROJECT_IDS, "Expected the three distinct projects")
    indexed_documents = set()
    capability_count = metric_count = 0
    allowed_provenance = {
        "export_time_test_rerun_reported", "historical_test_run_reported",
        "historical_source_expansion_reported", "historical_deployment_record",
        "historical_development_ledger", "synthetic_scenario_in_reviewed_ledger",
    }
    for project in projects:
        directory = f"projects/{project['id']}"
        require(project["directory"] == directory, f"Wrong directory for {project['id']}")
        require(bool(project["summary"]) and bool(project["stack"]) and bool(project["limitations"]),
                f"Missing scope information: {project['id']}")
        expected = {key: f"{directory}/{filename}" for key, filename in DOCUMENTS.items()}
        require(project["documents"] == expected, f"Incomplete document map: {project['id']}")
        for path in expected.values():
            local_file(path)
            indexed_documents.add(path)
        evidence_path = expected["evidence"]
        evidence = local_file(evidence_path).read_text(encoding="utf-8")
        claim_ids = set(re.findall(r"^\|\s*(E\d+)\s*\|", evidence, re.MULTILINE))
        require(bool(claim_ids), f"No claim register in {evidence_path}")
        for group in ("capabilities", "metrics"):
            unique_ids(project[group], f"{project['id']} {group}")
            for item in project[group]:
                require(item["evidence_document"] == evidence_path,
                        f"Cross-project evidence reference: {project['id']}:{item['id']}")
                references = item["evidence_ids"]
                require(isinstance(references, list) and set(references) <= claim_ids,
                        f"Unknown evidence ID: {project['id']}:{item['id']}")
                if group == "capabilities":
                    require(bool(references), f"Capability needs a claim: {item['id']}")
                    require(item["status"] == "implementation_described_in_supplied_export",
                            f"Unsupported implementation status: {item['id']}")
                    capability_count += 1
                else:
                    require(type(item["value"]) is int and item["value"] >= 0,
                            f"Invalid metric value: {item['id']}")
                    require(bool(item["unit"]) and bool(item["qualifications"]),
                            f"Unqualified metric: {item['id']}")
                    require(item["provenance"] in allowed_provenance,
                            f"Unknown provenance: {item['id']}")
                    require(item["executed_in_this_repository"] is False,
                            f"Do not claim a private measurement was run here: {item['id']}")
                    if item["observed_on"] is not None:
                        valid_date(item["observed_on"])
                        require(item["observed_on"] <= index["content_baseline_date"],
                                f"Metric postdates content baseline: {item['id']}")
                    numeric_evidence = evidence.replace(",", "")
                    require(re.search(rf"(?<!\d){item['value']}(?!\d)", numeric_evidence) is not None,
                            f"Metric number absent from evidence: {item['id']}")
                    metric_count += 1
    actual_documents = {str(path.relative_to(ROOT)) for path in (ROOT / "projects").rglob("*.md")}
    require(actual_documents == indexed_documents, "Project documents and index differ")
    return len(projects), capability_count, metric_count


def check_markdown():
    documents = [ROOT / name for name in ("README.md", "AGENTS.md", "REVIEW_GUIDE.md")]
    documents += sorted((ROOT / "projects").rglob("*.md"))
    links = diagrams = 0
    for path in documents:
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        require(text.startswith("# "), f"Missing title: {relative}")
        fence = None
        visible = []
        for line in text.splitlines():
            match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if fence is None and match:
                fence = match[1]
                if match[2].strip() == "mermaid":
                    diagrams += 1
            elif fence is not None:
                if re.fullmatch(rf"\s{{0,3}}{re.escape(fence[0])}{{{len(fence)},}}\s*", line):
                    fence = None
            else:
                visible.append(line)
        require(fence is None, f"Unclosed code fence: {relative}")
        headings = [line for line in visible if line.startswith("# ")]
        require(len(headings) == 1, f"Expected one document title: {relative}")
        for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", "\n".join(visible)):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue  # External destinations are not fetched by this offline check.
            require(not parsed.query and not parsed.fragment,
                    f"Use file-level local links in this package: {relative}: {target}")
            destination = (path.parent / unquote(parsed.path)).resolve()
            require(destination.is_relative_to(ROOT) and destination.is_file(),
                    f"Broken or escaping local link: {relative}: {target}")
            links += 1
    return len(documents), links, diagrams


def main():
    try:
        projects, capabilities, metrics = check_index()
        documents, links, diagrams = check_markdown()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {projects} projects, {documents} Markdown documents, {links} local links")
    print(f"PASS: {capabilities} indexed capabilities and {metrics} qualified metrics reference evidence")
    print(f"PASS: balanced code fences; {diagrams} Mermaid blocks inventoried (not rendered)")
    print("Scope: documentation consistency only; private source and application tests not executed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
