from ColumnDataSource import cds_diseases
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

#Criação da figure com dimensões especificadas
disease_fig = figure(width = 1280, height = 720)

#Atribuição do tipo de plot 
disease_fig.line(x="Year", y="Soma_doenças", source=cds_diseases, line_color = '#399e1f')

#Adicionando o hovertool para a vizualização do ano e da quantidade de mortes
hover = HoverTool(tooltips=[("Mortes:", "$y{0,0}"),("Ano: ", "@Year")])
disease_fig.add_tools(hover)

#Customização do plot
disease_fig.title.text = "Total de Mortes por Doenças (histórico)"
disease_fig.title.text_color = "#4f7227"
disease_fig.title.text_font = "Arial"
disease_fig.title.text_font_size = "26px"
disease_fig.title.align = "center"

disease_fig.xaxis.axis_label = "Ano"
disease_fig.xaxis.major_label_text_font_size = "16px"

disease_fig.yaxis.axis_label = "Número de Mortes"
disease_fig.yaxis.major_label_text_font_size = "16px"
disease_fig.yaxis[0].formatter = NumeralTickFormatter(format='0,0')

disease_fig.axis.axis_label_text_color = '#4f7227'

disease_fig.axis.axis_label_text_font_size = "24px"

disease_fig.outline_line_color = "black"

# Tirando o Grid
disease_fig.xgrid.grid_line_color = None
disease_fig.ygrid.grid_line_color = None

#criação dos círculos
coordenada_x_1 = 1990
coordenada_y_1 = 34017000

coordenada_x_2 = 2019
coordenada_y_2 = 41070000

disease_fig.circle(coordenada_x_1, coordenada_y_1, size=50, color="blue", alpha=0.2)
disease_fig.circle(coordenada_x_2, coordenada_y_2, size=50, color="red", alpha=0.2)


show(disease_fig)

