import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

def plot_3():

    #Leitura do csv
    df = pd.read_csv("../new_cause_of_death.csv")

    #Filtragem apenas por países africanos + soma das mortes por HIV/AIDS em cada ano
    df_africa_hiv = df[df['Continente'] == "Africa"].groupby('Year')['HIV/AIDS'].sum().reset_index()

    #Criação do ColumnDataSource
    cds = ColumnDataSource(df_africa_hiv)

    fig = figure()

    #Atribuição do tipo de plot
    fig.line(x="Year", y="HIV/AIDS", source=cds, line_color = '#8b0000')
    
    #Customização do plot
    fig.title.text = "Número de Mortes por Aids/HIV na África (Linha do Tempo)"
    fig.title.text_color = "#bc634f"
    fig.title.text_font = "Times"
    fig.title.text_font_size = "18px"
    fig.title.align = "center"

    fig.xaxis.axis_label = "Ano"
    fig.xaxis.major_label_text_font_size = "14px"

    fig.yaxis.axis_label = "Número de Mortes"
    fig.yaxis.major_label_text_font_size = "14px"

    fig.axis.axis_label_text_color = '#bc634f'

    fig.axis.axis_label_text_font_size = "18px"

    return fig