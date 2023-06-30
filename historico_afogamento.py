from ColumnDataSource import cds_afogamento
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

#Criação da figure com dimensões especificadas
drowning_fig = figure(width = 1280, height = 720)

#Atribuição do tipo de plot (Para que o gráfico abrangesse do valor 0 até a frequência de mortes
# atribuí o y1 ao valor desejado e o y2 a 0, logo, todo esse espaço seria preenchido.)
drowning_fig.varea(x = 'Year', y1 = 'Drowning', y2 = 0,source = cds_afogamento)

#Adicionando o hovertool para a vizualização do ano e do número de mortes
hover = HoverTool(tooltips=[("Ano", "@Year"), ("Mortes", "@Drowning")])
drowning_fig.add_tools(hover)

#Customização do plot
drowning_fig.title.text = "Número de Afogamentos por Ano (Mundo)"
drowning_fig.title.text_color = "DarkBlue"
drowning_fig.title.text_font = "Arial"
drowning_fig.title.text_font_size = "26px"
drowning_fig.title.align = "center"

drowning_fig.xaxis.axis_label = "Ano"
drowning_fig.xaxis.major_label_text_font_size = "16px"

drowning_fig.yaxis.axis_label = "Total de Casos"
drowning_fig.yaxis.major_label_text_font_size = "16px"
drowning_fig.yaxis[0].formatter = NumeralTickFormatter(format='0a')

drowning_fig.axis.axis_label_text_color = "DarkBlue"

drowning_fig.axis.axis_label_text_font_size = "24px"

drowning_fig.xgrid.grid_line_color = "blue"
drowning_fig.xgrid.grid_line_alpha = 0.2

drowning_fig.ygrid.grid_line_color = "blue"
drowning_fig.ygrid.grid_line_alpha = 0.2

drowning_fig.outline_line_color = "black"

# Tirando o Grid
drowning_fig.xgrid.grid_line_color = None
drowning_fig.ygrid.grid_line_color = None

drowning_fig.toolbar.autohide = True
drowning_fig.toolbar.logo = None

show(drowning_fig)