"""
DSC602 Homework 1 — Task 1: Grouped bar chart (MPG by origin, 2-MPG bins).
Deliverable: pr1-groupedBar.py
"""

from __future__ import annotations

import pr1_mpl_init  # noqa: F401 — set matplotlib backend before pyplot (fixes broken Tcl/Tk)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pr1_data import ORIGIN_COLORS, load_old_cars

plt.style.use("seaborn-v0_8")


def main() -> None:
    df = load_old_cars()
    mpg = df["MPG"].dropna()

    min_mpg = np.floor(mpg.min() / 2) * 2
    max_mpg = np.ceil(mpg.max() / 2) * 2
    bins = np.arange(min_mpg, max_mpg + 2, 2)

    df_task1 = df.dropna(subset=["MPG", "Origin"]).copy()
    df_task1["MPG_bin"] = pd.cut(df_task1["MPG"], bins=bins, right=False)

    counts = (
        df_task1.groupby(["MPG_bin", "Origin"], observed=False).size().unstack(fill_value=0)
    )
    origin_order = [o for o in ["US", "Europe", "Japan"] if o in counts.columns]
    counts = counts.reindex(columns=origin_order)

    x = np.arange(len(counts.index))
    bar_width = 0.25

    fig, ax = plt.subplots(figsize=(16, 6))

    for i, origin in enumerate(origin_order):
        ax.bar(
            x + (i - (len(origin_order) - 1) / 2) * bar_width,
            counts[origin].values,
            width=bar_width,
            label=origin,
            color=ORIGIN_COLORS.get(origin),
            edgecolor="white",
        )

    ax.set_title("Task 1 — MPG distribution (2-MPG bins) by Origin")
    ax.set_xlabel("MPG bin (2-MPG increments)")
    ax.set_ylabel("Number of cars")

    bin_labels = [f"{int(iv.left)}–{int(iv.left + 2)}" for iv in counts.index]
    ax.set_xticks(x)
    ax.set_xticklabels(bin_labels, rotation=45, ha="right")
    ax.legend(title="Origin")

    plt.tight_layout()
    pr1_mpl_init.show_plot()


if __name__ == "__main__":
    main()
