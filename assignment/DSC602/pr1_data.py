"""
Prerequisite: load and clean the old cars dataset for DSC602 Homework 1.

Used by pr1-groupedBar.py, pr1-line.py, pr1-scatterplot.py, pr1-scattermatrix.py.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ORIGIN_ORDER = ["US", "Europe", "Japan"]
ORIGIN_COLORS = {"US": "#4C72B0", "Europe": "#55A868", "Japan": "#C44E52"}


def _base_dir() -> Path:
    return Path(__file__).resolve().parent


def _resolve_csv_path() -> Path:
    base = _base_dir()
    candidates = [
        base / "old_cars - old_cars.csv",
        base.parent / "DSC602" / "old_cars - old_cars.csv",
        Path("old_cars - old_cars.csv"),
        Path(".") / "old_cars - old_cars.csv",
        Path("assignment") / "DSC602" / "old_cars - old_cars.csv",
    ]
    for p in candidates:
        if p.exists():
            return p.resolve()
    raise FileNotFoundError(
        "Could not find 'old_cars - old_cars.csv'. "
        "Place the CSV next to this file or update pr1_data._resolve_csv_path."
    )


def load_old_cars() -> pd.DataFrame:
    csv_path = _resolve_csv_path()
    df = pd.read_csv(csv_path)
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]

    numeric_cols = ["MPG", "Displacement", "Horsepower", "Weight", "Model"]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df.loc[df["Horsepower"] == 0, "Horsepower"] = np.nan
    df["Origin"] = df["Origin"].astype(str).str.strip()
    df["Car"] = df["Car"].astype(str).str.strip()

    return df
