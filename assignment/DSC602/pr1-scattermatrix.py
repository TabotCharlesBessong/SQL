"""
DSC602 Homework 1 — Task 4: Scatter plot matrix — MPG, Weight, Horsepower, Displacement
(color = origin). Uses pandas.plotting.scatter_matrix.
Deliverable: pr1-scattermatrix.py
"""

from __future__ import annotations

import pr1_mpl_init  # noqa: F401 — set matplotlib backend before pyplot (fixes broken Tcl/Tk)

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

from pr1_data import ORIGIN_COLORS, ORIGIN_ORDER, load_old_cars

plt.style.use("seaborn-v0_8")


def main() -> None:
    df = load_old_cars()
    cols_matrix = ["MPG", "Weight", "Horsepower", "Displacement"]
    df_task4 = df.dropna(subset=cols_matrix + ["Origin"]).copy()

    origin_to_color = ORIGIN_COLORS
    point_colors = df_task4["Origin"].map(origin_to_color).fillna("#777777")

    scatter_matrix(
        df_task4[cols_matrix],
        figsize=(12, 12),
        diagonal="hist",
        alpha=0.7,
        c=point_colors,
        marker="o",
        s=25,
        range_padding=0.1,
    )

    origin_order = [o for o in ORIGIN_ORDER if o in df_task4["Origin"].unique()]
    legend_handles = [
        mpatches.Patch(color=origin_to_color[o], label=o) for o in origin_order
    ]

    plt.suptitle("Task 4 — Scatter plot matrix (color = Origin)", y=1.02)
    plt.legend(
        handles=legend_handles,
        title="Origin",
        loc="upper right",
        bbox_to_anchor=(1.15, 1.02),
    )

    plt.tight_layout()
    pr1_mpl_init.show_plot()


if __name__ == "__main__":
    main()
