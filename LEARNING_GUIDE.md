# PayLens — learning guide

## What it does

Explore salary estimates and uncertainty. The intended user is career researchers. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Run generate.py then train.py, start the app, and vary experience and region. Inspect holdout MAE, baseline MAE, calibration radius and observed interval coverage in artifacts/evaluation.json.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Separate training, calibration and final test rows before fitting preprocessing.
2. Ridge regression uses an explicit median baseline and train-fitted categorical encoding.
3. Split conformal residual quantiles create an illustrative prediction interval with finite-sample calibration adjustment.

## Five interview questions

1. **What problem does this project solve, and what is its unit of work?** Explain explore salary estimates and uncertainty, identify career researchers as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Separate training, calibration and final test rows before fitting preprocessing. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Ridge regression uses an explicit median baseline and train-fitted categorical encoding. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Split conformal residual quantiles create an illustrative prediction interval with finite-sample calibration adjustment. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Entire dataset is synthetic and generated from a known salary equation. Results have no validated labor-market meaning. Intervals depend on exchangeability and are not guarantees for real applicants. Sensitive attributes are not included; fairness was not established. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a seniority feature, regenerate data with a documented process, and compare the held-out baseline without reusing test data for tuning.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated explore salary estimates and uncertainty using scikit-learn · Flask, with validated data and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
