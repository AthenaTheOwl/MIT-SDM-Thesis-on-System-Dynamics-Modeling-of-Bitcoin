# MIT SDM thesis on system dynamics modeling of Bitcoin

A `.mdl` file, two `.voc` files, two `.out` calibrations, and `combined.csv`: the Bitcoin argument here lives in stocks, flows, delays, and calibration traces.

## What this repo contains

This is the public archive for a system-dynamics thesis on Bitcoin market structure. The model is kept close to the original research artifact: Vensim files, vocabulary files, calibration output, and a small app for reading the core model behavior without opening Vensim first.

The work is about explanatory structure. It asks how feedback, adoption, supply, price expectation, and market attention interact over time.

## Contents

```text
combined.csv
model.mdl
model.voc
model.out
model_2.voc
model_2.out
streamlit_app.py
requirements.txt
```

## Try it locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

The app reads the checked-in model outputs and displays the time-series structure behind the thesis.

## Validation

Run the lightweight validation check:

```bash
python scripts/validate_thesis_archive.py
```

Expected output:

```text
ok: model and calibration artifacts found
ok: combined.csv parsed
ok: streamlit entrypoint found
```

## Live demo

<!-- live-url -->

Streamlit entrypoint:

```text
streamlit_app.py
```

Local run:

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

## Notes for readers

Read this as a mechanistic model of a complex market, not as a trading signal. The useful artifact is the causal structure: what loops are assumed, what delays are modeled, and where the calibration strains.

## License

See the repository license.
