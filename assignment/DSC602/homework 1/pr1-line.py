"""
DSC602 Homework 1 — Task 2: Line chart — annual average MPG by origin (1970–1982).
Deliverable: pr1-line.py
"""

from __future__ import annotations

import pr1_mpl_init  # noqa: F401 — set matplotlib backend before pyplot (fixes broken Tcl/Tk)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pr1_data import ORIGIN_COLORS, ORIGIN_ORDER, load_old_cars

plt.style.use("seaborn-v0_8")


def main() -> None:
    df = load_old_cars()
    df_task2 = df.dropna(subset=["MPG", "Model", "Origin"]).copy()
    df_task2 = df_task2[(df_task2["Model"] >= 70) & (df_task2["Model"] <= 82)]

    avg_mpg = df_task2.groupby(["Model", "Origin"])["MPG"].mean().unstack()
    years = np.arange(70, 83)
    avg_mpg = avg_mpg.reindex(years)
    origin_order = [o for o in ORIGIN_ORDER if o in avg_mpg.columns]
    avg_mpg = avg_mpg.reindex(columns=origin_order)

    fig, ax = plt.subplots(figsize=(12, 6))

    for origin in origin_order:
        ax.plot(
            years,
            avg_mpg[origin],
            marker="o",
            linewidth=2,
            label=origin,
            color=ORIGIN_COLORS.get(origin),
        )

    ax.set_title("Task 2 — Annual average MPG by Origin (1970–1982)")
    ax.set_xlabel("Model year")
    ax.set_ylabel("Average MPG")
    ax.set_xticks(years)
    ax.legend(title="Origin")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    pr1_mpl_init.show_plot()


if __name__ == "__main__":
    main()
