"""
p2_brushing.py  –  Task 3: Linked Brushing (2×2 Bubble Charts)
===============================================================
Four bubble charts share the same ColumnDataSource.
Selections made in any chart (Box Select tool) are instantly
mirrored in the other three – that is Bokeh's built-in linked brushing.

Run:
    bokeh serve --show p2_brushing.py
"""

import pandas as pd
import numpy as np
import os

from bokeh.plotting import figure, curdoc
from bokeh.models import (
    ColumnDataSource, Select, Slider,
    LinearColorMapper, ColorBar, HoverTool,
    BasicTicker, Div, CDSView, IndexFilter,
)
from bokeh.palettes import YlOrRd9, Plasma256
from bokeh.layouts import column, row, gridplot

# Load data 
DATA_PATH = os.path.join(os.path.dirname(__file__), "factbook_clean.csv")
df = pd.read_csv(DATA_PATH)
NUMERIC_COLS = df.select_dtypes(include=[np.number]).columns.tolist()

# Default attribute assignments per chart
CHART_DEFAULTS = [
    {"x": "GDP per capita",          "y": "Life expectancy at birth",
     "r": "Population",              "c": "Birth rate"},
    {"x": "Birth rate",              "y": "Death rate",
     "r": "Population",              "c": "Infant mortality rate"},
    {"x": "Inflation rate",          "y": "GDP real growth rate",
     "r": "Population",              "c": "Unemployment rate"},
    {"x": "Electricity consumption", "y": "Internet users",
     "r": "Population",              "c": "GDP per capita"},
]

# Build master flat data dict (one row per country per chart col)
def build_data():
    """Flatten all 4 charts into the shared source."""
    n = len(df)
    result = {"country": df["Country"].fillna("N/A").values.tolist()}
    # include all numeric columns
    for col in NUMERIC_COLS:
        result[col] = df[col].fillna(np.nanmedian(df[col])).values.tolist()
    return result

all_data = build_data()

# Shared ColumnDataSource – Bokeh's linked brushing works because every chart
# references the SAME source object.
source = ColumnDataSource(all_data)

# Helper: scale radii from a column array 
def norm_radii(vals, scale=1.0):
    sq = np.sqrt(np.abs(vals))
    mn, mx = sq.min(), sq.max()
    if mx == mn:
        return np.full(len(sq), 15.0 * scale)
    return (6 + (50 - 6) * (sq - mn) / (mx - mn)) * scale

# Pre-compute radius columns for every numeric column and store in source
radius_map = {}
for col in NUMERIC_COLS:
    rkey = f"__r_{col}__"
    source.data[rkey] = norm_radii(np.array(all_data[col]))
    radius_map[col] = rkey

# Make one bubble chart panel
def make_panel(idx, defaults):
    x_col = defaults["x"]
    y_col = defaults["y"]
    r_col = defaults["r"]
    c_col = defaults["c"]

    mapper = LinearColorMapper(
        palette=list(reversed(YlOrRd9)),
        low=float(np.nanmin(all_data[c_col])),
        high=float(np.nanmax(all_data[c_col])),
    )

    p = figure(
        width=480, height=400,
        title=f"Chart {idx+1}: {x_col} vs {y_col}",
        x_axis_label=x_col, y_axis_label=y_col,
        tools="pan,wheel_zoom,box_select,reset,save",
    )
    p.title.text_font_size = "11px"

    cr = p.circle(
        x=x_col, y=y_col,
        radius=radius_map[r_col], radius_units="screen",
        fill_color={"field": c_col, "transform": mapper},
        fill_alpha=0.7,
        line_color="white", line_width=0.5,
        # selected / unselected appearance for brushing
        selection_fill_alpha=1.0,
        selection_line_color="black",
        selection_line_width=1.5,
        nonselection_fill_alpha=0.15,
        nonselection_line_alpha=0.1,
        source=source,
    )

    hover = HoverTool(tooltips=[
        ("Country", "@country"),
        (x_col, f"@{{{x_col}}}{{0,0.00}}"),
        (y_col, f"@{{{y_col}}}{{0,0.00}}"),
    ])
    p.add_tools(hover)

    color_bar = ColorBar(
        color_mapper=mapper,
        ticker=BasicTicker(desired_num_ticks=6),
        label_standoff=6,
        border_line_color=None,
        title=c_col,
        title_text_font_size="9px",
        major_label_text_font_size="9px",
        location=(0, 0),
        width=10,
    )
    p.add_layout(color_bar, "right")

    # ---- per-chart widget controls -----
    sel_x = Select(title="X",     value=x_col,  options=NUMERIC_COLS, width=180)
    sel_y = Select(title="Y",     value=y_col,  options=NUMERIC_COLS, width=180)
    sel_r = Select(title="Radius",value=r_col,  options=NUMERIC_COLS, width=180)
    sel_c = Select(title="Color", value=c_col,  options=NUMERIC_COLS, width=180)
    scale_slider = Slider(title="Radius scale", value=1.0,
                          start=0.2, end=4.0, step=0.1, width=380)

    def update(attr, old, new,
               p=p, mapper=mapper, color_bar=color_bar,
               cr=cr, sel_x=sel_x, sel_y=sel_y,
               sel_r=sel_r, sel_c=sel_c, scale_slider=scale_slider):
        nx = sel_x.value
        ny = sel_y.value
        nr = sel_r.value
        nc = sel_c.value
        sc = scale_slider.value

        # recompute radii for new column+scale
        rkey = f"__r_{nr}__{idx}"
        source.data[rkey] = norm_radii(np.array(all_data[nr]), sc)

        cr.glyph.x = nx
        cr.glyph.y = ny
        cr.glyph.radius = rkey
        cr.glyph.fill_color = {"field": nc, "transform": mapper}
        mapper.low  = float(np.nanmin(all_data[nc]))
        mapper.high = float(np.nanmax(all_data[nc]))
        color_bar.title = nc
        p.xaxis.axis_label = nx
        p.yaxis.axis_label = ny
        p.title.text = f"Chart {idx+1}: {nx} vs {ny}"

    for w in [sel_x, sel_y, sel_r, sel_c, scale_slider]:
        w.on_change("value", update)

    controls = column(
        row(sel_x, sel_y),
        row(sel_r, sel_c),
        scale_slider,
    )
    return column(p, controls)

# ── Assemble 2×2 grid ──────────────────────────────────────────────────────────
panels = [make_panel(i, CHART_DEFAULTS[i]) for i in range(4)]

header = Div(text="""
<h2>World Factbook – Linked Brushing (2×2 Bubble Charts)</h2>
<p>Use the <b>Box Select</b> tool in <em>any</em> chart to highlight countries
across all four charts simultaneously.</p>
""")

grid = gridplot(
    [[panels[0], panels[1]],
     [panels[2], panels[3]]],
    merge_tools=False,
)

curdoc().add_root(column(header, grid))
curdoc().title = "Task 3 – Linked Brushing"
