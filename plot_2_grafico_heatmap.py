import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, BasicTicker, PrintfTickFormatter, HoverTool
from bokeh.transform import linear_cmap
from math import pi
from ColumnDataSource import source_heatmap, years, diseases, df_heatmap

# Definindo as cores do heatmap
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
# Definindo as tools que usaremos
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

# Criando nossa figure
heatmap =  figure(x_range = years, y_range  = diseases, tools = TOOLS)

# Definindo as Propiedadades do título
heatmap.title.text = f"Top 10 doenças que mais mataram no Brasil({years[0]}-{years[-1]})"
heatmap.title.text_color = "Black"
heatmap.title.text_font = "Arial"
heatmap.title.text_font_size = "20px"
heatmap.title.align = "center"
# definindo interatividade 
interativo = HoverTool(tooltips=[("Ano", "@Year"), ("Doença", "@Disease_Name"), ("Número de casos", "@casos")])
heatmap.add_tools(interativo)

# Definindo o tamanho do heatmap
heatmap.width = 1280
heatmap.height = 720

# adicionando propriedades no grid
heatmap.grid.grid_line_color = None

# Configurando as propriedades da tool bar
heatmap.toolbar.logo = None
heatmap.toolbar.autohide = True

# Adicionando propriedades aos eixos
heatmap.axis.axis_line_color = None
heatmap.axis.major_tick_line_color = None
heatmap.axis.major_label_text_font_size = "12px"
heatmap.axis.major_label_standoff = 0
heatmap.xaxis.major_label_orientation = pi / 4

# Adicionando uma escala de cores que será posteriormente usada para o heatmap
color_chart = linear_cmap("casos", colors, low = df_heatmap.casos.min(), high=df_heatmap.casos.max())

# Adicionando os retângulos do heatmap
tiles = heatmap.rect(x = "Year", y = "Disease_Name",  width = 1, height=1, fill_color = color_chart, line_color = None ,source = source_heatmap)

# Adicionando uma escala com grid de cores
heatmap.add_layout(tiles.construct_color_bar(major_label_text_font_size="12px", ticker=BasicTicker(desired_num_ticks=len(colors)),
    formatter=PrintfTickFormatter(format="%0d"), label_standoff=7,border_line_color=None,padding=5,), 'right')
