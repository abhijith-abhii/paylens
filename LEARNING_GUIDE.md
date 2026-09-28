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

1. **What do the salary numbers mean?** They are outcomes in an authored synthetic dataset, expressed in USD. The model demonstrates a regression workflow; it does not estimate market compensation reliably.

2. **Why compare against a median baseline?** A complex model should improve on a simple prediction. The held-out MAE is compared with predicting the training median for every test record.

3. **How are interval and model fitting separated?** Training fits the preprocessing and regression model. A separate calibration split estimates residual uncertainty. The untouched test split checks point accuracy and interval coverage.

4. **Does 90% coverage guarantee accuracy for each person?** No. Split conformal coverage relies on exchangeability and is marginal across the population. Distribution shift and individual subgroups can behave differently.

5. **How is leakage prevented?** Record IDs are disjoint across training, calibration and test splits, and learned preprocessing is fit only on training data. Tests and saved evaluation artifacts make those boundaries inspectable.

## Independent exercise

Add a seniority feature, regenerate data with a documented process, and compare the held-out baseline without reusing test data for tuning.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Developed a synthetic salary regression workflow with disjoint training, calibration and test splits; measured $10,142 holdout MAE against a $22,305 median baseline.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
