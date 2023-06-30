import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, BasicTicker, PrintfTickFormatter, HoverTool, NumeralTickFormatter
from bokeh.transform import linear_cmap
from math import pi
from gráfico_3 import df_causas_de_morte_Brasil
from gráfico_3 import source

# Gráfico anos e mortes por 100k
grafico_anos_mortes_100k = figure(x_range=df_causas_de_morte_Brasil["Year"],
                                 tools="box_zoom,pan,reset,save,wheel_zoom")
grafico_anos_mortes_100k.line(x="Year", y="Deaths per 100k", source=source)

# Adicionando interatividade ao gráfico
interativo_anos_mortes_100k = HoverTool(tooltips=[("Ano", "@Year"), ("Mortes por 100 mil habitantes", "@{Deaths per 100k}")])
grafico_anos_mortes_100k.add_tools(interativo_anos_mortes_100k)

# Adicionando propriedades aos títulos do gráfico
grafico_anos_mortes_100k.title.text = "Gráfico sobre como variou a morte a cada 100 mil habitantes de 1990 - 2019"
grafico_anos_mortes_100k.title.text_color = "Black"
grafico_anos_mortes_100k.title.text_font = "Arial"
grafico_anos_mortes_100k.title.text_font_size = "15px"
grafico_anos_mortes_100k.title.align = "center"

# Modificando o tamanho do output
grafico_anos_mortes_100k.width = 700
grafico_anos_mortes_100k.height = 400

#Definindo propriedades do eixo

grafico_anos_mortes_100k.xaxis.axis_label = "Anos"
grafico_anos_mortes_100k.xaxis.minor_tick_line_color = "black"
grafico_anos_mortes_100k.axis.minor_tick_in = 0
grafico_anos_mortes_100k.xaxis.major_label_orientation = pi/3
grafico_anos_mortes_100k.xaxis.major_label_text_font_size = "9pt"

grafico_anos_mortes_100k.yaxis.axis_label = "Quantidade de mortes a cada 100 mil habitantes"
grafico_anos_mortes_100k.yaxis.major_label_orientation = "vertical"
grafico_anos_mortes_100k.yaxis.minor_tick_line_color = "black"
grafico_anos_mortes_100k.yaxis.minor_tick_line_color = None

# Definindo a borda
grafico_anos_mortes_100k.outline_line_color = "black"

# Tirando o Grid
grafico_anos_mortes_100k.xgrid.grid_line_color = None
grafico_anos_mortes_100k.ygrid.grid_line_color = None

# Propiedades das ferramentas
grafico_anos_mortes_100k.toolbar.logo = None
grafico_anos_mortes_100k.toolbar.autohide = True