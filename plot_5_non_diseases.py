from ColumnDataSource import cds_non_diseases
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

#Criação da figure com dimensões especificadas
non_disease_fig = figure(width = 1280, height = 720)

#Atribuição do tipo de plot 
non_disease_fig.line(x="Year", y="Soma_não_doenças", source=cds_non_diseases, line_color = '#399e1f')

#Adicionando o hovertool para a vizualização do ano e da quantidade de mortes
hover = HoverTool(tooltips=[("Mortes", "$y{0,0}"),("Ano", "@Year")])
non_disease_fig.add_tools(hover)

#Customização do plot
non_disease_fig.title.text = "Total de Mortes por Lesões (histórico)"
non_disease_fig.title.text_color = "#4f7227"
non_disease_fig.title.text_font = "Arial"
non_disease_fig.title.text_font_size = "26px"
non_disease_fig.title.align = "center"

non_disease_fig.xaxis.axis_label = "Ano"
non_disease_fig.xaxis.major_label_text_font_size = "16px"

non_disease_fig.yaxis.axis_label = "Número de Mortes"
non_disease_fig.yaxis.major_label_text_font_size = "16px"
non_disease_fig.yaxis[0].formatter = NumeralTickFormatter(format='0,0')

non_disease_fig.axis.axis_label_text_color = '#4f7227'

non_disease_fig.axis.axis_label_text_font_size = "24px"

#criação dos círculos
coordenada_x_1 = 1994
coordenada_y_1 = 4300000

coordenada_x_2 = 2019
coordenada_y_2 = 3122070

non_disease_fig.circle(coordenada_x_1, coordenada_y_1, size=50, color="red", alpha=0.2)
non_disease_fig.circle(coordenada_x_2, coordenada_y_2, size=50, color="blue", alpha=0.2)

non_disease_fig.outline_line_color = "black"

# Tirando o Grid
non_disease_fig.xgrid.grid_line_color = None
non_disease_fig.ygrid.grid_line_color = None

non_disease_fig.toolbar.autohide = True
non_disease_fig.toolbar.logo = None

non_disease_fig.background_fill_color = "green"
non_disease_fig.background_fill_alpha = 0.1
