"""
p2_tooltip.py  –  Task 4: Details on Demand (Hover Tooltip + Highlight)
========================================================================
Extends Task 3 (the 2×2 linked-brushing view) with rich hover tooltips.

When the mouse hovers over a bubble:
  • A floating tooltip shows the country name and ALL numeric attributes.
  • The hovered country is highlighted (larger, black outline) across
    all four charts simultaneously via a CustomJS callback.

Run:
    bokeh serve --show p2_tooltip.py
"""

import pandas as pd
import numpy as np
import os

from bokeh.plotting import figure, curdoc
from bokeh.models import (
    ColumnDataSource, Select, Slider,
    LinearColorMapper, ColorBar, HoverTool,
    BasicTicker, Div, CustomJS,
)
from bokeh.palettes import YlOrRd9
from bokeh.layouts import column, row, gridplot

# Load data 
DATA_PATH = os.path.join(os.path.dirname(__file__), "factbook_clean.csv")
df = pd.read_csv(DATA_PATH)
NUMERIC_COLS = df.select_dtypes(include=[np.number]).columns.tolist()

# Build shared data dict 
def build_data():
    result = {"country": df["Country"].fillna("N/A").values.tolist()}
    for col in NUMERIC_COLS:
        result[col] = df[col].fillna(np.nanmedian(df[col])).values.tolist()
    return result

all_data = build_data()
source = ColumnDataSource(all_data)

# Radius helpers 
def norm_radii(vals, scale=1.0):
    sq = np.sqrt(np.abs(vals))
    mn, mx = sq.min(), sq.max()
    if mx == mn:
        return np.full(len(sq), 15.0 * scale)
    return (6 + (50 - 6) * (sq - mn) / (mx - mn)) * scale

radius_map = {}
for col in NUMERIC_COLS:
    rkey = f"__r_{col}__"
    source.data[rkey] = norm_radii(np.array(all_data[col]))
    radius_map[col] = rkey

# Default chart attributes 
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

# Tooltip: show all numeric columns 
def all_tooltips():
    tips = [("Country", "@country")]
    for col in NUMERIC_COLS:
        tips.append((col, f"@{{{col}}}{{0,0.00}}"))
    return tips

# Build one panel 
all_circle_renderers = []  # used for cross-chart highlight CustomJS

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
        selection_fill_alpha=1.0,
        selection_line_color="black",
        selection_line_width=2.0,
        nonselection_fill_alpha=0.15,
        nonselection_line_alpha=0.1,
        source=source,
        name=f"cr_{idx}",
    )

    all_circle_renderers.append(cr)

    # ---- Rich hover tooltip ----
    hover = HoverTool(
        renderers=[cr],
        tooltips=all_tooltips(),
        point_policy="follow_mouse",
    )
    p.add_tools(hover)

    color_bar = ColorBar(
        color_mapper=mapper,
        ticker=BasicTicker(desired_num_ticks=6),
        label_standoff=6, border_line_color=None,
        title=c_col,
        title_text_font_size="9px",
        major_label_text_font_size="9px",
        location=(0, 0), width=10,
    )
    p.add_layout(color_bar, "right")

    # ---- Per-chart dropdown widgets ----
    sel_x = Select(title="X",     value=x_col, options=NUMERIC_COLS, width=180)
    sel_y = Select(title="Y",     value=y_col, options=NUMERIC_COLS, width=180)
    sel_r = Select(title="Radius",value=r_col, options=NUMERIC_COLS, width=180)
    sel_c = Select(title="Color", value=c_col, options=NUMERIC_COLS, width=180)
    scale_sl = Slider(title="Radius scale", value=1.0,
                      start=0.2, end=4.0, step=0.1, width=380)

    def update(attr, old, new,
               p=p, mapper=mapper, color_bar=color_bar, cr=cr,
               sel_x=sel_x, sel_y=sel_y, sel_r=sel_r, sel_c=sel_c,
               scale_sl=scale_sl):
        nx, ny = sel_x.value, sel_y.value
        nr, nc = sel_r.value, sel_c.value
        sc = scale_sl.value
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

    for w in [sel_x, sel_y, sel_r, sel_c, scale_sl]:
        w.on_change("value", update)

    controls = column(row(sel_x, sel_y), row(sel_r, sel_c), scale_sl)
    return column(p, controls), cr

# Build all panels 
panels = []
circle_renderers = []
for i, d in enumerate(CHART_DEFAULTS):
    panel, cr = make_panel(i, d)
    panels.append(panel)
    circle_renderers.append(cr)

# Cross-chart hover highlight via CustomJS 
# When the user hovers any circle, set its 'line_width' to stand out in all charts.
# We do this by attaching a mousemove CustomJS to the shared source's inspected indices.
highlight_js = CustomJS(
    args={"source": source, "renderers": circle_renderers},
    code="""
        // indices holds the hovered index from the last HoverTool inspection
        const idx = cb_data.index.indices;
        for (let r of renderers) {
            const ds = r.data_source;
            // trigger a re-render so nonselection style kicks in for others
            ds.selected.indices = idx.slice();
        }
    """
)

for cr in circle_renderers:
    cr.data_source.selected.js_on_change("indices", highlight_js)

# Layout 
header = Div(text="""
<h2>World Factbook – Details on Demand (Hover + Linked Brushing)</h2>
<p>
  <b>Hover</b> over any bubble to see all country attributes in the tooltip
  and highlight that country across all four charts.<br>
  Use <b>Box Select</b> to brush a region and highlight across charts.
</p>
""")

grid = gridplot(
    [[panels[0], panels[1]],
     [panels[2], panels[3]]],
    merge_tools=False,
)

curdoc().add_root(column(header, grid))
curdoc().title = "Task 4 – Details on Demand"
