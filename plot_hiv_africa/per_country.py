import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

def plot_4():

    #Leitura do csv
    df = pd.read_csv("../new_cause_of_death.csv")

    #Criação de uma nova coluna que representa a quantidade de mortes em decorrência de HIV/AIDS a cada 100k habitantes em cada país
    df["per_100k_hab"] = df["HIV/AIDS"]/df["população"]*100000

    #Filtragem países africanos + soma das mortes a cada 100000 habitantes por ano + valores em ordem decrescente + top 10 valores
    df_countries_hiv = df[df['Continente'] == "Africa"].groupby('Country/Territory')['per_100k_hab'].sum().sort_values(ascending=False).head(10).reset_index()
    #O objetivo é obter os 10 países com o maior histórico de mortes a cada 100000 habitantes da áfrica (em decorrência de HIV)

    #Criação do ColumnDataSource
    cds = ColumnDataSource(df_countries_hiv)

    grid3_fig = figure(x_range=df_countries_hiv['Country/Territory'])
    #A inserção do x_range é necessária para a criação dos bar charts. Sua função é atribuir as categorias da coluna ao eixo x.

    #Atribuição do tipo de plot
    grid3_fig.vbar(x='Country/Territory', top='per_100k_hab', source=cds, width = 0.8, fill_color = '#bc634f', line_color = None)

    #Customização do plot
    grid3_fig.title.text = "Top 10 Países com mais Mortes por 100 mil Habitantes (histórico)"
    grid3_fig.title.text_color = "#bc634f"
    grid3_fig.title.text_font = "Arial"
    grid3_fig.title.text_font_size = "18px"
    grid3_fig.title.align = "center"

    grid3_fig.xaxis.axis_label = "Continente"
    grid3_fig.xaxis.major_label_text_font_size = "14px"
    grid3_fig.xaxis.major_label_orientation = "vertical"


    grid3_fig.yaxis.axis_label = "Número de Mortes"
    grid3_fig.yaxis.major_label_text_font_size = "14px"
    grid3_fig.yaxis.visible = False

    grid3_fig.axis.axis_label_text_color = '#bc634f'

    grid3_fig.axis.axis_label_text_font_size = "18px"

    grid3_fig.outline_line_color = "black"

    # Tirando o Grid
    grid3_fig.xgrid.grid_line_color = None
    grid3_fig.ygrid.grid_line_color = None

    return grid3_fig


