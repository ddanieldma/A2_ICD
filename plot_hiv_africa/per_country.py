import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

def plot_4():
    df = pd.read_csv("../new_cause_of_death.csv")

    df["per_100k_hab"] = df["HIV/AIDS"]/df["população"]*100000

    df_countries_hiv = df[df['Continente'] == "Africa"].groupby('Country/Territory')['per_100k_hab'].sum().sort_values(ascending=False).head(10).reset_index()

    cds = ColumnDataSource(df_countries_hiv)

    fig = figure(x_range=df_countries_hiv['Country/Territory'])

    fig.vbar(x='Country/Territory', top='per_100k_hab', source=cds, width = 0.8, fill_color = '#bc634f', line_color = None)

    fig.title.text = "Top 10 Países com mais Mortes por 100 mil Habitantes (histórico)"
    fig.title.text_color = "#bc634f"
    fig.title.text_font = "Times"
    fig.title.text_font_size = "18px"
    fig.title.align = "center"

    fig.xaxis.axis_label = "Continente"
    fig.xaxis.major_label_text_font_size = "14px"
    fig.xaxis.major_label_orientation = "vertical"


    fig.yaxis.axis_label = "Número de Mortes"
    fig.yaxis.major_label_text_font_size = "14px"


    fig.axis.axis_label_text_color = '#bc634f'

    fig.axis.axis_label_text_font_size = "18px"

    return fig


