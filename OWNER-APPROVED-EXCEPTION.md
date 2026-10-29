# Owner-Approved Release Exception

- **Project:** TQ Community Edition
- **Target repository:** `Tariqul0123/TQ-Community-Edition` (public)
- **Decision date:** 2026-10-28
- **Approver:** Repository owner, via explicit written instruction in the project conversation
- **Decision:** Authorize immediate public release while accepting the residual risk of three incomplete pre-publication gates

## Explicitly waived gates

1. **Gitleaks exact-candidate scan:** not run against the exact final published Git tree before publication.
2. **Independent human licensing/provenance review:** not completed before publication. The owner previously attested to having rights to publish the candidate files under Apache-2.0; that is an owner attestation, not an independent legal conclusion.
3. **GitHub Actions CI:** not completed before publication. The repository includes a CI workflow; its first post-publication run passed, but this does not change the recorded pre-publication waiver.

## Evidence available at decision time

- Source archive: `TQ_COMMUNITY_EDITION_RECONSTRUCTED_V9.zip`
- Source candidate SHA-256: `e2a94d7608fbdc0751fdff742b5bcefe85527db0889a407281d0b65e285a265b`
- Archive integrity and path/symlink safety checks: passed
- Local unit tests: 8/8 passed
- Python compilation: passed
- Built-in heuristic release scanner: passed
- Extended selected secret-pattern scans: zero findings for the patterns checked; not equivalent to Gitleaks

## Residual risks accepted

- An unrecognized credential or sensitive string may remain despite local pattern scans.
- Licensing, attribution, and provenance obligations have not received independent review.
- Later CI runs may fail or reveal issues after future changes.
- The reconstructed candidate is not byte-identical to the historical V7 archive.

## Safety commitments

- Do not modify, publish, or expose the private production repository as part of this release.
- Do not add production credentials, secrets, private business data, broker execution, or Local AI public exposure.
- If post-publication scans or CI reveal a serious issue, promptly remediate or temporarily remove the affected public content; preserve the report and decision trail.
- This exception is a risk-acceptance record, not a declaration that the waived checks passed.

## Execution evidence

This document records the owner's approval and residual-risk decision. The first post-publication CI run [#40879622784](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40879622784) completed successfully. The pre-publication Gitleaks scan and independent licensing/provenance review remain waived/not completed.
