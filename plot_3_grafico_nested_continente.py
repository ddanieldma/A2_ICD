import pandas as pd
from math import pi
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, HoverTool, NumeralTickFormatter
from bokeh.palettes import brewer
from ColumnDataSource import source_grafico_nested, continentes

# Plotando o gráfico
grafico_juntos = figure(x_range = FactorRange(*continentes))
grafico_juntos.vbar(x = "agrupado" , top = "numero_de_casos",
                    color = "Cor", width = 0.8, 
                    legend_field = "Doenca",
                    source=source_grafico_nested)

grafico_juntos.legend.label_text_font = "Arial"


# Adicionando propriedades aos títulos do gráfico
grafico_juntos.title.text = "As três maiores causas de morte por continente de 1990 até 2019"
grafico_juntos.title.text_color = "Black"
grafico_juntos.title.text_font = "Arial"
grafico_juntos.title.text_font_size = "22px"
grafico_juntos.title.align = "center"

#Definindo propriedades do eixo
grafico_juntos.xaxis.axis_label = "Continentes"
grafico_juntos.xaxis.minor_tick_line_color = "black"
grafico_juntos.xaxis.minor_tick_in = 0
grafico_juntos.xaxis.major_label_orientation = pi/4
grafico_juntos.xaxis.major_label_text_font_size = "9pt"

grafico_juntos.yaxis.axis_label = "Quantidade de mortes"
grafico_juntos.yaxis.formatter = NumeralTickFormatter(format="0.0a")
grafico_juntos.yaxis.major_label_orientation = "horizontal"
grafico_juntos.yaxis.minor_tick_line_color = "black"
grafico_juntos.yaxis.minor_tick_line_color = None

# Definindo a borda
grafico_juntos.outline_line_color = "black"

# Tirando o Grid
grafico_juntos.xgrid.grid_line_color = None
grafico_juntos.ygrid.grid_line_color = None
grafico_juntos.grid.grid_line_color = None


# Adicionando interatividade
interativo = HoverTool(tooltips = [("Continent", "@Continente"), ("Doença", "@Doenca"),("Número de casos", "@numero_de_casos")])
grafico_juntos.add_tools(interativo)

# Definindo altura e largura
grafico_juntos.width = 1280
grafico_juntos.height = 720

# Configurando as propriedades da tool bar
grafico_juntos.toolbar.logo = None
grafico_juntos.toolbar.autohide = True

# Adicionando cor de fundo
grafico_juntos.background_fill_color = "blue"
grafico_juntos.background_fill_alpha = 0.1
