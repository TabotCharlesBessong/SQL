"""
p2_widgets.py  –  Task 2: Interactive Widgets
==============================================
Extends Task 1: the user can select at runtime which attribute drives
  x, y, radius, and color  (via four Select drop-down menus)
and control a size-scale multiplier via a Slider.

Run:
    bokeh serve --show p2_widgets.py
(Must run as a Bokeh server app because callbacks need Python.)
"""

import pandas as pd
import numpy as np
import os

from bokeh.plotting import figure, curdoc
from bokeh.models import (
    ColumnDataSource, Select, Slider,
    LinearColorMapper, ColorBar, HoverTool,
    BasicTicker, Div,
)
from bokeh.palettes import YlOrRd9, Viridis256
from bokeh.layouts import column, row

# Load the clean data
DATA_PATH = os.path.join(os.path.dirname(__file__), "./factbook_cleaned.csv")
data = pd.read_csv(DATA_PATH)

# Numeric columns for dropdowns
NUMERIC_COLS = data.select_dtypes(include=[np.number]).columns.tolist() 
data = data.dropna(subset=NUMERIC_COLS[:0])  # keep all rows; NaNs handled per col

# Initial attribute choices
INIT_X     = "GDP per capita"
INIT_Y     = "Life expectancy at birth"
INIT_R     = "Population"
INIT_COLOR = "Birth rate"
INIT_SCALE = 1.0   # radius multiplier

# Helper functions

def scale_radii(col_name, scale=1.0):
  """Return normalised radii [6,50]*scale for a given column."""
  vals = data[col_name].fillna(data[col_name].median()).values
  sq   = np.sqrt(np.abs(vals))
  mn, mx = sq.min(), sq.max()
  if mx == mn:
    return np.full(len(sq), 15.0 * scale)
  r = 6 + (50 - 6) * (sq - mn) / (mx - mn)
  return r * scale


def make_source(x_col, y_col, r_col, c_col, scale):
  valid = data[[x_col, y_col, r_col, c_col, "Country"]].dropna()
  return dict(
    x         = valid[x_col].values,
    y         = valid[y_col].values,
    radii     = scale_radii(r_col, scale)[valid.index],
    color_val = valid[c_col].values,
    country   = valid["Country"].values,
    x_val     = valid[x_col].values,
    y_val     = valid[y_col].values,
  )
  
# Initial ColumnDataSource
source = ColumnDataSource(make_source(INIT_X, INIT_Y, INIT_R, INIT_COLOR, INIT_SCALE))

# Color mapper
mapper = LinearColorMapper(
  palette = list(reversed(YlOrRd9)),
  low     = data[INIT_COLOR].min(),
  high    = data[INIT_COLOR].max(),
)

# Figure
p = figure(
  width=900,height=560,
  title=f"{INIT_X} vs {INIT_Y}",
  x_axis_label=INIT_X,
  y_axis_label=INIT_Y,
  tools="pan,wheel_zoom,box_zoom,reset,save")

circles = p.circle(
  x="x", y="y",
  radius="radii", radius_units="screen",
  fill_color={"field": "color_val", "transform": mapper},
  fill_alpha=0.7,
  line_color="white", line_width=0.5,
  source=source,
)

hover = HoverTool(tooltips=[
  ("Country",    "@country"),
  ("X",          "@x_val{0,0.00}"),
  ("Y",          "@y_val{0,0.00}"),
  ("Radius attr","@r_val{0,0.00}"),
  ("Color attr", "@c_val{0,0.00}"),
])
p.add_tools(hover)

color_bar = ColorBar(
  color_mapper=mapper,
    ticker=BasicTicker(desired_num_ticks=8),
  label_standoff=8,
  border_line_color=None,
  title=INIT_COLOR,
  location=(0, 0),
)
p.add_layout(color_bar, "right")

# Widgets
sel_x = Select(title="X axis",    value=INIT_X,     options=NUMERIC_COLS, width=220)
sel_y = Select(title="Y axis",    value=INIT_Y,     options=NUMERIC_COLS, width=220)
sel_r = Select(title="Radius",    value=INIT_R,     options=NUMERIC_COLS, width=220)
sel_c = Select(title="Color",     value=INIT_COLOR, options=NUMERIC_COLS, width=220)

slider = Slider(title="Radius scale", value=1.0, start=0.2, end=4.0,
                step=0.1, width=460)


# Callbacks for interactivity

def update_plot(attr,old, new):
  x_col = sel_x.value
  y_col = sel_y.value
  r_col = sel_r.value
  c_col = sel_c.value
  scale = slider.value
  
  new_data = make_source(x_col, y_col, r_col, c_col, scale)
  source.data = new_data
  
  
  # Update axis labels and plot title
  p.xaxis.axis_label = x_col
  p.yaxis.axis_label = y_col
  p.title.text = f"{x_col} vs {y_col}"
  
  # Update color mapper range and color bar title
  mapper.low = data[c_col].min()
  mapper.high = data[c_col].max()
  color_bar.title = c_col
  
for w in [sel_x, sel_y, sel_r, sel_c, slider]:
  w.on_change("value", update_plot)
  
# Layout
header  = Div(text="<h2>World Factbook – Interactive Bubble Chart</h2>")
widgets = row(sel_x, sel_y, sel_r, sel_c)
layout  = column(header, widgets, slider, p)

curdoc().add_root(layout)
curdoc().title = "Task 2 – Widgets"