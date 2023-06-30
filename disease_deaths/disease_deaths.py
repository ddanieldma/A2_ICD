import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter

#Leitura do csv
df = pd.read_csv("../new_cause_of_death.csv")

#Criando uma nova coluna que representa a soma dos valores numéricos das colunas especificadas
df['Soma_doenças'] = df[["Meningitis","Alzheimer's Disease and Other Dementias", "Parkinson's Disease", 
"Cardiovascular Diseases","Lower Respiratory Infections", "Acute Hepatitis", "Digestive Diseases", "Cirrhosis and Other Chronic Liver Diseases", 
"Chronic Respiratory Diseases", "Diabetes Mellitus","Chronic Kidney Disease", "Nutritional Deficiencies", "Malaria", "Maternal Disorders", 
"HIV/AIDS","Drug Use Disorders","Tuberculosis","Neonatal Disorders","Alcohol Use Disorders","Diarrheal Diseases"]].sum(axis=1)

#Filtrando por ano (+ soma de todos os valores da coluna ['Soma_doenças'] desse ano)
df_diseases = df.groupby('Year')['Soma_doenças'].sum().reset_index()

#Criação do ColumnDataSource
cds = ColumnDataSource(df_diseases)

output_file("line_plot_drowning.html")

#Criação da figure com dimensões especificadas
fig = figure(width = 1280, height = 720)

#Atribuição do tipo de plot 
fig.line(x="Year", y="Soma_doenças", source=cds, line_color = '#399e1f')

#Customização do plot
fig.title.text = "Total de Mortes por Doenças (histórico)"
fig.title.text_color = "#4f7227"
fig.title.text_font = "Times"
fig.title.text_font_size = "26px"
fig.title.align = "center"

fig.xaxis.axis_label = "Ano"
fig.xaxis.major_label_text_font_size = "16px"

fig.yaxis.axis_label = "Número de Mortes"
fig.yaxis.major_label_text_font_size = "16px"
fig.yaxis[0].formatter = NumeralTickFormatter(format='0a')

fig.axis.axis_label_text_color = '#4f7227'

fig.axis.axis_label_text_font_size = "24px"

show(fig)

