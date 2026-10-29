#!/usr/bin/env python3
"""Basic heuristic scan only; not a replacement for Gitleaks or human review."""
from pathlib import Path
import re
import sys

PATTERNS = [
    ("private key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("common credential assignment", re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"][^'\"\n]{8,}")),
    ("AWS access key shape", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token shape", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b")),
]

def scan(root: Path):
    findings = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in PATTERNS:
            for match in pattern.finditer(content):
                findings.append((str(path.relative_to(root)), label, match.start()))
    return findings

if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings = scan(root)
    if findings:
        for path, label, offset in findings:
            print(f"REVIEW: {path}: {label} at character {offset}")
        sys.exit(1)
    print("Basic heuristic scan: no matching patterns found (not a clean security certification).")
