<!-- ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ -->

# N° 03 · a thesis on bitcoin, in system dynamics

> *stocks and flows, all the way down.*

all model files required to replicate the SDM-program thesis at MIT, advised by **prof. hazhir rahmandad**. the question: what happens when you stop arguing about bitcoin in op-eds and try to model it as a system — with feedback loops, delays, and accumulations that don't care what anyone thinks?

`vensim DSS` · `python` · 2022 · **status: running**

📄 *thesis submission folder* — the state of the work the week of submission, may 6, 2022.
✉️ vignesh — `vigneshg@mit.edu`

<!-- ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ -->

## the model files

| file | what it is |
|---|---|
| `thesis_checkpoint.mdl`            | the model. opens in **vensim DSS 9.2.4**. |
| `bitcoin_demand.voc`               | calibration control file — market side |
| `bitcoin2.voc`                     | calibration control file — production side |
| `demand_side_calibration.out`      | calibration result — apply before simulation |
| `supply_side_calibration.out`      | calibration result — apply before simulation |
| `demand_side_calibration.rep`      | calibration report — RSquared, MAPE, MSE |
| `supply_side_calibration.rep`      | calibration report — RSquared, MAPE, MSE |
| `combined.csv`                     | simulated output, both `.out` files applied |
| `DataPull.py`                      | pulls exogenous inputs from blockchain.com APIs |
| `DataFiles/ConsolidatedData.vdfx`  | consolidated data in vensim's native format. **load this for the model to run.** |
| `DataFiles/*.csv`                  | raw pulls per series, before consolidation |

## the data pipeline

```
blockchain.com API
        │
        ▼
   DataPull.py
        │
        ▼
   DataFiles/*.csv  ──▶  ConsolidatedData.csv  ──▶  ConsolidatedData.vdfx
                                                            │
                                                            ▼
                                              thesis_checkpoint.mdl
                                                            │
                                                            ▼
                                                      simulation
```

to refresh the data: rerun `DataPull.py`, regenerate the consolidated csv, re-import to vdfx in vensim.

## to run

1. open `thesis_checkpoint.mdl` in **vensim DSS** (9.2.4 or later)
2. load `DataFiles/ConsolidatedData.vdfx`
3. apply both `.out` files (demand- and supply-side calibration)
4. simulate

## the calibration reports

`*.rep` files document the fit:
- **RSquared** — variance explained
- **MAPE** — mean absolute percentage error
- **MSE** — mean squared error

reports are committed alongside the model so the fit isn't a black box.

<!-- ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ -->

## colophon

an MIT SDM thesis on system dynamics modeling of bitcoin. the repo is the appendix — every file you'd need to rerun, recalibrate, or pull fresh data and try it again.

*built downstairs.* — [the basement, room 7](https://github.com/AthenaTheOwl)
