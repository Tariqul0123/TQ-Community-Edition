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


## Post-publication follow-up — 2026-10-29

- **Dedicated secret scan:** Gitleaks v8.30.1 scanned the checked-out published tree using the directory scan mode. The binary archive SHA-256 was verified before execution. GitHub Actions run [#40885001920](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40885001920) passed the Gitleaks step with no findings.
- **License template correction:** the Apache-2.0 template's unresolved `Copyright [yyyy] [name of copyright owner]` placeholder was replaced with `Copyright 2026 TQ Community Edition contributors`. This attribution follows the repository owner's publication authorization; it is not an independent legal determination.
- **Internal provenance review:** the 26-file tree was reviewed for obvious third-party dependency/source indicators. The Python examples use the standard library and are short TQ-specific illustrative implementations; no third-party runtime dependency manifest or vendored third-party source was found in the tree. This limited text/tree inspection cannot prove authorship, provenance, or legal rights.
- **Independent review status:** an independent human licensing/provenance review remains **not completed**. It is not marked as passed and still requires a reviewer independent of this implementation/release process.

The successful post-publication scan does not retroactively satisfy the owner-waived pre-publication gate. It is a separate follow-up result. The package remains a community reference, not a production deployment recipe.
