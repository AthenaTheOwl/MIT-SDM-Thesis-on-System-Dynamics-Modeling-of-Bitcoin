#!/usr/bin/env python3
"""Validate the committed thesis appendix files used by the Streamlit viewer."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUBMISSION = ROOT / "Thesis Submission Files"
REQUIRED_FILES = [
    "thesis_checkpoint.mdl",
    "bitcoin_demand.voc",
    "bitcoin2.voc",
    "demand_side_calibration.out",
    "supply_side_calibration.out",
    "demand_side_calibration.rep",
    "supply_side_calibration.rep",
    "combined.csv",
    "DataPull.py",
    "DataFiles/ConsolidatedData.vdfx",
]


def validate_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (SUBMISSION / name).exists()]
    if missing:
        raise SystemExit(f"missing required thesis file(s): {', '.join(missing)}")


def validate_combined_csv() -> None:
    combined = SUBMISSION / "combined.csv"
    with combined.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        rows = list(reader)
    if len(rows) < 3:
        raise SystemExit("combined.csv has fewer than 3 rows")
    header = rows[0]
    if "Time" not in header:
        raise SystemExit("combined.csv has no Time column")
    data_rows = rows[2:]  # row 2 carries units
    if len(data_rows) < 10:
        raise SystemExit("combined.csv has too few observation rows")
    numeric_columns = 0
    for column_index, name in enumerate(header):
        if name == "Time":
            continue
        values = [
            row[column_index]
            for row in data_rows
            if column_index < len(row) and row[column_index].strip()
        ]
        if not values:
            continue
        try:
            for value in values[:20]:
                float(value)
        except ValueError:
            continue
        numeric_columns += 1
    if numeric_columns < 5:
        raise SystemExit("combined.csv has fewer than 5 numeric series")


def main() -> int:
    validate_required_files()
    validate_combined_csv()
    print(f"validated {len(REQUIRED_FILES)} required files and combined.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
