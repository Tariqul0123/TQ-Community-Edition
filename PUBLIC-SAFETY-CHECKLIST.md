# Public Release Safety Checklist

This checklist records the actual status of the published release. The owner explicitly waived three pre-publication gates; waived items are not marked as passed.

- [x] Exact source release candidate hash recorded and ZIP integrity checked.
- [ ] Dedicated Gitleaks scan against the exact final candidate — **WAIVED by owner; not run**.
- [x] Local review and selected secret-pattern scans completed with no findings for the patterns checked; this is not a Gitleaks replacement.
- [ ] Independent third-party licensing and attribution review — **WAIVED by owner; not completed**.
- [x] Full Apache-2.0 license text included and owner attested to publication rights; independent legal verification not claimed.
- [ ] Hosted GitHub Actions CI before publication — **WAIVED by owner; not completed before publication**.
- [x] Dedicated post-publication Gitleaks v8.30.1 scan passed against the published tree in [run #40885001920](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40885001920); this does not retroactively satisfy the waived pre-publication gate.
- [x] First post-publication GitHub Actions CI run passed: [Community Edition CI #40879622784](https://github.com/Tariqul0123/TQ-Community-Edition/actions/runs/40879622784).
- [x] Source archive safety checks found no path traversal or symlink entries.
- [x] Demo/test data is synthetic and isolated from real business data in the example package.
- [x] Public issue template does not solicit secrets.
- [x] Owner-approved exception and residual risk are documented in `OWNER-APPROVED-EXCEPTION.md`.
- [x] Explicit publication authorization obtained from repository owner on 2026-10-28.

Do not interpret waived items as passing. See `RELEASE-STATUS.md` and `RELEASE-AUDIT-REPORT.md`.
