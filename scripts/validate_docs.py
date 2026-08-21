#!/usr/bin/env python3
"""Offline integrity checks for the AgentProof Platform documentation hub."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "SECURITY.md",
    "docs/information-architecture.md",
    "docs/architecture/system-model.md",
    "docs/security/threat-model.md",
    "docs/release/release-policy.md",
    "docs/deployment/ci-reference.md",
    "docs/roadmap/roadmap.md",
    "docs/adr/0001-local-first-ci-native-v1.md",
    "docs/adr/0002-core-contract-is-the-interoperability-center.md",
    "docs/adr/0003-simulated-side-effects-and-minimized-capture.md",
    "docs/adr/0004-release-claims-require-reproducible-evidence.md",
    "docs/runbooks/triage-ci-evidence-failure.md",
    "docs/runbooks/handle-evidence-privacy-incident.md",
    "docs/runbooks/release-rollback.md",
    ".github/workflows/ci.yml",
    ".github/workflows/codeql.yml",
    ".github/dependabot.yml",
)
COMPONENT_COMMITS = {
    "agentproof-core": "0c7f149bce6402cd4b91b08010a5a800b21f5d71",
    "agentproof-otel": "58c73b582211dc28f72e11e62f0e22ca816ac7fe",
    "agentproof-mcp": "119f2ddc6b68b9dd6d853fed0387801c84557c7a",
    "agentproof-policy": "4417d951e1b389690703cdfcb4069a6627568286",
    "agentproof-replay": "bf8f5ea8df6107e30b9557f71b8612eefb740f34",
    "agentproof-corpus": "89ea8b4098a6720fb0c29568d7adc577018c793c",
    "agentproof-action": "33c5f69cab79945027efae62d386decbff376128",
    "agentproof-python": "8254b4f1d861e5e9f7a98af35902a6dc998f5b9b",
    "agentproof-typescript": "cc5046b8ad4de0072a9ef0463f3f1a5973efbb42",
}
EXCLUDED_LINK_PREFIXES = ("#", "http://", "https://", "mailto:", "tel:")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)")
FULL_SHA_ACTION = re.compile(r"^\s*- uses: [\w./-]+@[0-9a-f]{40}\s*$", re.MULTILINE)
SECRET_FILENAMES = {".env", ".env.local", "credentials.json", "id_rsa", "id_ed25519"}


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def relative_target(document: Path, link: str) -> Path | None:
    target = unquote(link.split("#", maxsplit=1)[0].strip())
    if not target or target.startswith(EXCLUDED_LINK_PREFIXES):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return (document.parent / target).resolve()


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    inventory = ROOT / "docs/information-architecture.md"
    inventory_text = inventory.read_text(encoding="utf-8") if inventory.is_file() else ""
    for component, commit in COMPONENT_COMMITS.items():
        if component not in inventory_text or commit not in inventory_text:
            errors.append(f"inventory snapshot missing {component} at {commit}")

    manifest_path = ROOT / "release-manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"release manifest is invalid JSON: {error.msg}")
        else:
            if manifest.get("name") != "agentproof-platform":
                errors.append("release manifest has an unexpected name")
            if manifest.get("version") != "0.1.0":
                errors.append("release manifest has an unexpected version")
            if manifest.get("runtimeDependencies") != []:
                errors.append("platform runtime dependencies must remain empty")

    for document in markdown_files():
        text = document.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                errors.append(f"trailing whitespace: {document.relative_to(ROOT)}:{number}")
        for link in MARKDOWN_LINK.findall(text):
            target = relative_target(document, link)
            if target is not None and not target.exists():
                errors.append(
                    f"broken relative link: {document.relative_to(ROOT)} -> {link}"
                )

    required_terms = ("local-first", "deterministic", "no hosted control plane", "live tool")
    combined = "\n".join(
        (ROOT / relative).read_text(encoding="utf-8")
        for relative in ("README.md", "docs/architecture/system-model.md", "docs/security/threat-model.md")
        if (ROOT / relative).is_file()
    )
    combined = " ".join(combined.lower().split())
    for term in required_terms:
        if term not in combined:
            errors.append(f"required boundary language missing: {term}")

    for path in ROOT.rglob("*"):
        if path.is_file() and path.name in SECRET_FILENAMES:
            errors.append(f"credential-shaped file is forbidden: {path.relative_to(ROOT)}")

    for workflow in (ROOT / ".github/workflows").glob("*.yml"):
        text = workflow.read_text(encoding="utf-8")
        actions = [line for line in text.splitlines() if line.strip().startswith("- uses:")]
        invalid = [line for line in actions if not FULL_SHA_ACTION.match(line)]
        if invalid:
            errors.append(f"workflow has mutable or malformed action pin: {workflow.relative_to(ROOT)}")
        if "permissions:" not in text:
            errors.append(f"workflow is missing explicit permissions: {workflow.relative_to(ROOT)}")
        if "|| true" in text:
            errors.append(f"workflow has a permissive failure bypass: {workflow.relative_to(ROOT)}")

    if errors:
        print("DOCUMENTATION VALIDATION FAILED", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(
        "VALID documentation="
        f"{len(markdown_files())} inventory_components={len(COMPONENT_COMMITS)} workflows=2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
