import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

#Leitura do csv
df = pd.read_csv("../new_cause_of_death.csv")

#Criando uma nova coluna que representa a soma dos valores numéricos das colunas especificadas
df['Soma'] = df[["Drowning", "Interpersonal Violence", "Fire, Heat, and Hot Substances", "Road Injuries", "Poisonings" ,
"Protein-Energy Malnutrition", "Conflict and Terrorism", "Self-harm", "Exposure to Forces of Nature", 
"Environmental Heat and Cold Exposure"]].sum(axis=1)

#Filtrando por ano (+ soma de todos os valores da coluna ['Soma'] desse ano)
df_non_diseases = df.groupby('Year')['Soma'].sum().reset_index()

#Criação do ColumnDataSource
cds = ColumnDataSource(df_non_diseases)

#Criação da figure com dimensões especificadas
fig = figure(width = 1280, height = 720)

#Atribuição do tipo de plot 
fig.line(x="Year", y="Soma", source=cds, line_color = '#399e1f')

#Adicionando o hovertool para a vizualização do ano e da quantidade de mortes
hover = HoverTool(tooltips=[("Mortes:", "$y{0,0}"),("Ano: ", "@Year")])
fig.add_tools(hover)

#Customização do plot
fig.title.text = "Total de Mortes por Lesões (histórico)"
fig.title.text_color = "#4f7227"
fig.title.text_font = "Arial"
fig.title.text_font_size = "26px"
fig.title.align = "center"

fig.xaxis.axis_label = "Ano"
fig.xaxis.major_label_text_font_size = "16px"

fig.yaxis.axis_label = "Número de Mortes"
fig.yaxis.major_label_text_font_size = "16px"
fig.yaxis[0].formatter = NumeralTickFormatter(format='0,0')

fig.axis.axis_label_text_color = '#4f7227'

fig.axis.axis_label_text_font_size = "24px"


show(fig)

