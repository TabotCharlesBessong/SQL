
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_notebook, output_file
from bokeh.models import (ColorBar,HoverTool, ColumnDataSource, LinearColorMapper, BasicTicker)
from bokeh.palettes import YlOrRd9 as palette

output_notebook()

data = pd.read_csv("./factbook_cleaned.csv")
data = data.dropna(subset=["GDP per capita","Population","Birth rate","Life expectancy at birth"])

# scale radii: area proportional to population
pop_sqrt = np.sqrt(data["Population"].values)
radii = 6 + (50 - 6) * (pop_sqrt - pop_sqrt.min()) / (pop_sqrt.max() - pop_sqrt.min())

source = ColumnDataSource(dict(
  x          = data["GDP per capita"].values,
  y          = data["Life expectancy at birth"].values,
  radii      = radii,
  color_val  = data["Birth rate"].values,
  country    = data["Country"].values,
  population = data["Population"].values,
  birth_rate = data["Birth rate"].values,
))

mapper = LinearColorMapper(
  palette = list(reversed(palette)),
  low     = data["Birth rate"].min(),
  high    = data["Birth rate"].max(),
)

output_file("p2_bubbles.html", title="Bubble Chart – World Factbook")

p = figure(width=860, height=520,
           title="GDP per Capita vs Life Expectancy "
                 "(bubble size = Population, color = Birth rate)",
           x_axis_label="GDP per Capita (USD)",
           y_axis_label="Life Expectancy at Birth (years)",
           tools="pan,wheel_zoom,box_zoom,reset,save")

p.circle(x="x", y="y",
         radius="radii", radius_units="screen",
         fill_color={"field":"color_val","transform":mapper},
         fill_alpha=0.7, line_color="white", line_width=0.5,
         source=source)

p.add_tools(HoverTool(tooltips=[
    ("Country",        "@country"),
    ("GDP per capita", "@x{$0,0}"),
    ("Life exp",       "@y{0.0} yrs"),
    ("Population",     "@population{0,0}"),
    ("Birth rate",     "@birth_rate{0.00}"),
]))

p.add_layout(ColorBar(color_mapper=mapper,
                       ticker=BasicTicker(desired_num_ticks=8),
                       title="Birth rate", location=(0,0)), "right")
p.xaxis.formatter.use_scientific = False
show(p)
print("✓ Saved p2_bubbles.html")