from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
SUBMISSION = ROOT / "Thesis Submission Files"
COMBINED = SUBMISSION / "combined.csv"


def load_combined() -> pd.DataFrame:
    # Row 2 carries Vensim units, not observations.
    return pd.read_csv(COMBINED, skiprows=[1])


st.set_page_config(page_title="Bitcoin system-dynamics thesis", layout="wide")
st.title("bitcoin system-dynamics thesis viewer")
st.caption("read-only browser for the committed MIT SDM thesis appendix")

if not COMBINED.exists():
    st.error("combined.csv is missing from the thesis submission folder.")
    st.stop()

data = load_combined()
numeric_columns = [
    column
    for column in data.columns
    if column != "Time" and pd.api.types.is_numeric_dtype(data[column])
]

st.subheader("simulation outputs")
st.write(
    "The viewer reads `Thesis Submission Files/combined.csv`, which was produced "
    "after applying the committed demand-side and supply-side calibration files."
)

defaults = [
    column
    for column in [
        "BTC Market Price",
        "Network Hash Rate",
        "Current Difficulty",
        "Number of Miners",
        "BTC in Circulation",
    ]
    if column in numeric_columns
]
selected = st.multiselect(
    "series",
    numeric_columns,
    default=defaults[:3] if defaults else numeric_columns[:3],
)

if selected:
    chart = data[["Time", *selected]].dropna(subset=["Time"]).set_index("Time")
    st.line_chart(chart)
else:
    st.info("Select one or more numeric series to chart.")

col1, col2, col3 = st.columns(3)
col1.metric("rows", f"{len(data):,}")
col2.metric("series", f"{len(data.columns):,}")
col3.metric("time span", f"{data['Time'].min():g} to {data['Time'].max():g}")

with st.expander("model files"):
    files = sorted(path.relative_to(SUBMISSION).as_posix() for path in SUBMISSION.rglob("*") if path.is_file())
    st.write(files)

st.subheader("local replication")
st.code(
    "\n".join(
        [
            "1. open Thesis Submission Files/thesis_checkpoint.mdl in Vensim DSS 9.2.4+",
            "2. load Thesis Submission Files/DataFiles/ConsolidatedData.vdfx",
            "3. apply demand_side_calibration.out and supply_side_calibration.out",
            "4. simulate and compare against combined.csv",
        ]
    ),
    language="text",
)

st.dataframe(data.head(50), width="stretch")
