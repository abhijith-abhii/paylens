# PayLens

Explore salary estimates and uncertainty for **career researchers**.

Original topic: **Employee Salary Prediction** from [the source post](https://www.instagram.com/p/DdyMaogE4ud/).

> Personal project by Abhijith Viswanathan. Working implementation, reproducible examples and measured results are documented below.

![Application screenshot](reports/screenshots/app.png)

## What works

- Validated data
- baseline
- train/test split
- prediction interval
- feature controls

[Example output](reports/example-output.json) · [Recorded checks](reports/test-results.txt) · [Learning and interview guide](LEARNING_GUIDE.md)

## Start

Python 3.12 is the validated Python runtime. Run commands from this repository directory. Windows users activate `.venv\Scripts\activate` instead of `source`.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python generate.py
python train.py
python app.py
```

Open **http://127.0.0.1:8080**. Keep the process running. Set `PORT` to use another port. The Python development servers are intended for local demonstrations.

## Demonstration

Run generate.py then train.py, start the app, and vary experience and region. Inspect holdout MAE, baseline MAE, calibration radius and observed interval coverage in artifacts/evaluation.json.

## Architecture and decisions

Browser controls → validated Flask API → project analysis/workflow → results and export.

Stack: scikit-learn · Flask.

1. Separate training, calibration and final test rows before fitting preprocessing.
2. Ridge regression uses an explicit median baseline and train-fitted categorical encoding.
3. Split conformal residual quantiles create an illustrative prediction interval with finite-sample calibration adjustment.

## Verification

```sh
python -m pytest -q
```

See [VERIFICATION.md](VERIFICATION.md) for actual executed checks, setup verification, model/data results and any outstanding environment limitations. The [recorded CI runs](reports/ci-verification.json) passed for the linked source revision.

## Data and attribution

Transparent synthetic compensation sample. See [DATA_AND_SOURCES.md](DATA_AND_SOURCES.md) for provenance and usage notes. Original project code is MIT unless a preserved source file or dependency states otherwise. Model and third-party data licenses remain separate.

## Limitations and next improvement

Entire dataset is synthetic and generated from a known salary equation. Results have no validated labor-market meaning. Intervals depend on exchangeability and are not guarantees for real applicants. Sensitive attributes are not included; fairness was not established.

Suggested extension: Add a seniority feature, regenerate data with a documented process, and compare the held-out baseline without reusing test data for tuning.

## Honest portfolio use

AI tools assisted with implementation, tests and documentation. This is my personal portfolio work; benchmark results and deployment boundaries are documented in the repository.

## Connect

[LinkedIn — Abhijith Viswanathan](https://www.linkedin.com/in/abhijith-viswanathan-0a7216436/)
