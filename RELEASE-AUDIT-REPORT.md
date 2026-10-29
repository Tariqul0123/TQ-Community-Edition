# Release Audit Report — Owner-Approved Exception

- Release: TQ Community Edition reconstructed release
- Decision: OWNER-APPROVED FOR PUBLICATION UNDER AN EXCEPTION
- Decision date: 2026-10-28
- Source candidate: `TQ_COMMUNITY_EDITION_RECONSTRUCTED_V9.zip`
- Source candidate SHA-256: `e2a94d7608fbdc0751fdff742b5bcefe85527db0889a407281d0b65e285a265b`
- Historical V7 archive: unavailable for byte-for-byte comparison
- Production TQ modified by publication: no

## Owner decision
The repository owner explicitly approved publication while accepting residual risk and waiving three pre-publication gates: (1) exact-candidate Gitleaks scan, (2) independent human licensing/provenance review, and (3) hosted GitHub Actions CI. These gates are **waived/not completed**, not passed. The full decision is recorded in `OWNER-APPROVED-EXCEPTION.md`.

## Local review evidence
- Source archive integrity and archive path/symlink safety checks passed.
- Unit tests: 8/8 passed locally.
- Python compilation passed locally.
- Included heuristic public-release scanner passed locally.
- Extended selected secret-pattern scans produced zero findings for the patterns checked.
- The heuristic and selected-pattern scans do not replace Gitleaks or independent human review.
- Examples are illustrative and do not connect to external providers, databases, broker accounts, or production systems.
- `CODE_OF_CONDUCT.md` is an original TQ Community Edition policy and is not presented as a Contributor Covenant adaptation.
- Full Apache License 2.0 text is included, based on owner-provided publication authorization; no independent legal opinion is claimed.

## Post-publication CI evidence
The first GitHub Actions run [Community Edition CI #40879622784](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40879622784) completed successfully. Its test, compilation, and basic heuristic scan steps passed. This is post-publication evidence only; it does not retroactively satisfy the waived pre-publication CI gate or replace Gitleaks or independent review.

## Remaining follow-up
- Run a dedicated secret scan against the published Git tree and remediate any finding immediately.
- Arrange an independent review of licensing, attribution, and provenance when available.
- Keep production repo, credentials, private data, broker execution, and Local AI exposure outside this community package.

## Scope and limitation
This report records a risk-acceptance decision; it is not a security certification, independent legal review, or assertion that every normal release gate passed.
