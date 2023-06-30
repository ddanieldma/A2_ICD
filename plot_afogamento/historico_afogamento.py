import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

#Leitura do csv
df = pd.read_csv("../new_cause_of_death.csv")

#Filtragem por ano com a soma dos valores da coluna ['Drowning']
df_drowning_sum = df.groupby('Year')['Drowning'].sum().reset_index()

#Criação do ColumnDataSource
cds = ColumnDataSource(df_drowning_sum)

output_file("line_plot_drowning.html")

#Criação da figure com dimensões especificadas
figure = figure(width = 1280, height = 720)

#Atribuição do tipo de plot (Para que o gráfico abrangesse do valor 0 até a frequência de mortes
# atribuí o y1 ao valor desejado e o y2 a 0, logo, todo esse espaço seria preenchido.)
figure.varea(x = 'Year', y1 = 'Drowning', y2 = 0,source = cds)

hover = HoverTool(tooltips=[("Ano: ", "@Year"), ("Mortes:", "@Drowning")])
figure.add_tools(hover)

#Customização do plot
figure.title.text = "Número de Afogamentos por Ano (Mundo)"
figure.title.text_color = "DarkBlue"
figure.title.text_font = "Times"
figure.title.text_font_size = "26px"
figure.title.align = "center"

figure.xaxis.axis_label = "Ano"
figure.xaxis.major_label_text_font_size = "16px"

figure.yaxis.axis_label = "Total de Casos"
figure.yaxis.major_label_text_font_size = "16px"
figure.yaxis[0].formatter = NumeralTickFormatter(format='0a')

figure.axis.axis_label_text_color = "DarkBlue"

figure.axis.axis_label_text_font_size = "24px"

figure.xgrid.grid_line_color = "blue"
figure.xgrid.grid_line_alpha = 0.2

figure.ygrid.grid_line_color = "blue"
figure.ygrid.grid_line_alpha = 0.2

show(figure)