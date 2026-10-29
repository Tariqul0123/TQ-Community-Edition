# Release Status

**Status: OWNER-APPROVED PUBLICATION UNDER AN EXCEPTION — WAIVED PRE-PUBLICATION GATES NOT PASSED**

This is a reconstructed community-edition release, not a byte-identical copy of the historical V7 archive. The repository owner explicitly authorized publication while accepting the residual risk of three incomplete pre-publication gates. This is a documented exception, not a claim that the waived checks passed.

## Owner-approved exceptions
- **Dedicated Gitleaks scan:** waived before publication; not run against the exact final published Git tree.
- **Independent human licensing/provenance review:** waived before publication; no independent review is claimed.
- **GitHub Actions CI:** waived as a pre-publication gate. The workflow was included and the first post-publication run passed; this does not mean pre-publication CI was completed.

The owner's prior attestation states they have the right to publish all candidate files under Apache-2.0. This report records that attestation as owner-provided information, not as independent legal advice or verification.

## Local evidence
- Candidate source archive integrity and archive safety checks passed.
- Unit tests: 8/8 passed locally.
- Python compilation passed locally.
- Built-in heuristic scanner passed locally.
- Extended selected secret-pattern scans returned no findings for the patterns checked. These checks are not equivalent to Gitleaks and are not a security certification.

## Publication verification
The target repository's commit history and file tree are the source of truth for what was published. The first post-publication GitHub Actions run [#40879622784](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40879622784) completed successfully, including tests, compilation, and the basic heuristic scan. The private production repository `Tariqul0123/tq-command-centre` is outside the release scope and must remain private and unchanged.

## Safety boundary
- This public repository contains only the community-edition reference package; it is not a production deployment recipe.
- Do not add production credentials, private data, broker connections, or deployment secrets.
- Human approval remains required for irreversible/high-impact actions.

See [OWNER-APPROVED-EXCEPTION.md](OWNER-APPROVED-EXCEPTION.md) and [RELEASE-AUDIT-REPORT.md](RELEASE-AUDIT-REPORT.md) for the recorded decision and limitations.


## Post-publication follow-up — 2026-10-29

- **Dedicated secret scan:** Gitleaks v8.30.1 scanned the checked-out published tree using the directory scan mode. The binary archive SHA-256 was verified before execution. GitHub Actions run [#40885001920](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40885001920) passed the Gitleaks step with no findings.
- **License template correction:** the Apache-2.0 template's unresolved `Copyright [yyyy] [name of copyright owner]` placeholder was replaced with `Copyright 2026 TQ Community Edition contributors`. This attribution follows the repository owner's publication authorization; it is not an independent legal determination.
- **Internal provenance review:** the 26-file tree was reviewed for obvious third-party dependency/source indicators. The Python examples use the standard library and are short TQ-specific illustrative implementations; no third-party runtime dependency manifest or vendored third-party source was found in the tree. This limited text/tree inspection cannot prove authorship, provenance, or legal rights.
- **Independent review status:** an independent human licensing/provenance review remains **not completed**. It is not marked as passed and still requires a reviewer independent of this implementation/release process.

The successful post-publication scan does not retroactively satisfy the owner-waived pre-publication gate. It is a separate follow-up result. The package remains a community reference, not a production deployment recipe.
