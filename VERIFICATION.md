# PayLens — verification

Verification date: 28 September 2026. Tests and examples were executed; they are not illustrative pass claims.

- Project checks: 10 passed.
- Dependency/setup verification: fresh isolated Python 3.12 environment passed.
- Main browser/API workflow: verified locally; actual result saved in reports/example-output.json.
- Publication: [public repository](https://github.com/abhijith-abhii/paylens) verified under **abhijith-abhii**.
- Actual application screenshot: reports/screenshots/app.png. Browser rendered successfully at 1280px width.

Synthetic holdout MAE: $10,142.43; median baseline: $22,305.38. Observed 90% interval coverage: 92.5%. No real salary accuracy is claimed.

## Evidence
- `reports/test-results.txt`: actual test output.
- `reports/clean-setup.json`: isolated setup result where applicable.
- `reports/publication-check.json`: credential-pattern and file audit.
- `DATA_AND_SOURCES.md`: source and license notes.

## GitHub verification

- [Verify: passed](https://github.com/abhijith-abhii/paylens/actions/runs/36416593927)

Verified source revision: `d42bb0aaac359011806491221ec08ce669f0f30a`. Subsequent presentation-only changes do not change that implementation evidence.
