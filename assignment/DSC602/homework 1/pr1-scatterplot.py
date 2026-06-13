"""
DSC602 Homework 1 — Task 3: Scatter plot — Horsepower vs MPG (color = model year).
Deliverable: pr1-scatterplot.py
"""

from __future__ import annotations

import pr1_mpl_init  # noqa: F401 — set matplotlib backend before pyplot (fixes broken Tcl/Tk)

import matplotlib.pyplot as plt

from pr1_data import load_old_cars

plt.style.use("seaborn-v0_8")


def main() -> None:
    df = load_old_cars()
    df_task3 = df.dropna(subset=["Horsepower", "MPG", "Model"]).copy()

    fig, ax = plt.subplots(figsize=(10, 6))

    sc = ax.scatter(
        df_task3["Horsepower"],
        df_task3["MPG"],
        c=df_task3["Model"],
        cmap="viridis",
        alpha=0.75,
        edgecolor="white",
        linewidth=0.4,
    )

    ax.set_title("Task 3 — Horsepower vs MPG (color = model year)")
    ax.set_xlabel("Horsepower")
    ax.set_ylabel("MPG")
    ax.grid(True, alpha=0.25)

    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Model year")

    plt.tight_layout()
    pr1_mpl_init.show_plot()


if __name__ == "__main__":
    main()
