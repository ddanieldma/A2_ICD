from numpy import linspace

from organizing_data import data_homicides_by_continent, df_homicides_by_continent
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter

import os
os.chdir("plots_homicidios")

output_file("deaths_by_homicides.html")

def ridge(category, data, scale = 20):
    return list(zip(category, scale*data))

x = linspace(-20,110, 1)

categories = list(df_homicides_by_continent["Continente"])

source = ColumnDataSource(data = dict(x = x))

plot = figure()

plot.title = "Mortes por violencia interpessoal e conflitos e terrorismo por continente"
# plot.y_range = data_homicides_by_continent
plot.width = 1280
plot.height = 720

for category in categories:
    pdf = category
    y = ridge(category, df_homicides_by_continent[df_homicides_by_continent["Continente"] == category]["Interpersonal Violence"])
    source.add(y, category)
    plot.patch("x", category, color = df_homicides_by_continent[df_homicides_by_continent["Continente"] == category]["Color"].values[0], alpha = 0.6, line_color = "Black", source = source)

plot.outline_line_color = None
plot.background_fill_color = "#efefef"

plot.xaxis.ticker = FixedTicker(ticks=list(range(0, 101, 10)))
plot.xaxis.formatter = PrintfTickFormatter(format="%d%%")

plot.ygrid.grid_line_color = None
plot.xgrid.grid_line_color = "#dddddd"
plot.xgrid.ticker = plot.xaxis.ticker

plot.axis.minor_tick_line_color = None
plot.axis.major_tick_line_color = None
plot.axis.axis_line_color = None

show(plot)