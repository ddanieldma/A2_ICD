import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

df = pd.read_csv("../../new_cause_of_death.csv")

df_africa_hiv = df[df['Continente'] == "Africa"].groupby('Year')['HIV/AIDS'].sum().reset_index()

cds = ColumnDataSource(df_africa_hiv)

figure = figure()

figure.line(x="Year", y="HIV/AIDS", source=cds, line_color = '#8b0000')

figure.title.text = "Número de Mortes por Aids/HIV na África (Linha do Tempo)"
figure.title.text_color = "#bc634f"
figure.title.text_font = "Times"
figure.title.text_font_size = "18px"
figure.title.align = "center"

figure.xaxis.axis_label = "Ano"
figure.xaxis.major_label_text_font_size = "14px"

figure.yaxis.axis_label = "Número de Mortes"
figure.yaxis.major_label_text_font_size = "14px"

figure.axis.axis_label_text_color = '#bc634f'

figure.axis.axis_label_text_font_size = "18px"

show(figure)

show(fig)

output_file("time_line_hiv.html")