import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

df = pd.read_csv("../../new_cause_of_death.csv")

df_cont_hiv = df.groupby('Continente')['HIV/AIDS'].sum().reset_index()

categorias = df_cont_hiv['Continente'].unique()
cores = ['#8b0000', '#bc634f', '#bc634f', '#bc634f', '#bc634f', '#bc634f']

cds = ColumnDataSource(df_cont_hiv)

output_file("hiv_continents.html")

figure = figure(x_range=df_cont_hiv['Continente'])  
#A inserção do x_range é necessária para a criação dos bar charts
#Sua função é atribuir as categorias da coluna ao eixo x.

figure.vbar(x= 'Continente', top= 'HIV/AIDS', source=cds, width=0.5,
         fill_color=factor_cmap('Continente', palette = cores, factors=categorias),
         line_color = None)

figure.title.text = "Mortes em Decorrência de Aids/HIV por Continente (1990-2019)"
figure.title.text_color = "#bc634f"
figure.title.text_font = "Times"
figure.title.text_font_size = "18px"
figure.title.align = "center"

figure.xaxis.axis_label = "Continente"
figure.xaxis.major_label_text_font_size = "14px"

figure.yaxis.axis_label = "Número de Mortes"
figure.yaxis.major_label_text_font_size = "14px"

figure.axis.axis_label_text_color = '#bc634f'

figure.axis.axis_label_text_font_size = "18px"

show(figure)


