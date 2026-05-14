"""
Matplotlib setup for homework scripts.

Import this module before ``import matplotlib.pyplot as plt``.

If Tcl/Tk is missing (TkAgg fails on Windows), we switch to the Agg backend and
``show_plot()`` saves a PNG and opens it with the default viewer.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile


def _configure() -> None:
    import matplotlib

    if os.environ.get("MPLBACKEND"):
        matplotlib.use(os.environ["MPLBACKEND"], force=True)
        return

    try:
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()
        root.destroy()
    except Exception:
        matplotlib.use("Agg", force=True)


_configure()


def show_plot() -> None:
    import matplotlib
    import matplotlib.pyplot as plt

    backend = matplotlib.get_backend().lower()
    if backend == "agg":
        path = tempfile.NamedTemporaryFile(prefix="pr1_", suffix=".png", delete=False).name
        plt.savefig(path, dpi=150, bbox_inches="tight")
        if os.name == "nt":
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path], start_new_session=True)
        else:
            subprocess.Popen(["xdg-open", path], start_new_session=True)
        print(f"Figure saved and opened ({backend} backend): {path}")
    else:
        plt.show()
