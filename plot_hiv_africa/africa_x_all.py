import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap


def plot_2():
    
    #Leitura do csv
    df = pd.read_csv("../new_cause_of_death.csv")

    #FIltragem por continente + soma dos registros de mortes por HIV/AIDS de cada um
    df_cont_hiv = df.groupby('Continente')['HIV/AIDS'].sum().reset_index()

    #Determinação das cores a serem utilizadas no plot
    cores = ['#8b0000', '#bc634f']

    #Obtendo numero de mortes em decorrência do HIV na África
    df_cont_hiv.loc[df_cont_hiv['Continente'] == "Africa", 'HIV/AIDS']
    #O resultado obtido foi 29106954

    #Obtendo numero de mortes em decorrência do HIV no restante do mundo
    df_cont_hiv.loc[df_cont_hiv['Continente'] != "Africa", 'HIV/AIDS'].sum()
    #O resultado obtido foi 7257465

    #Criação dos eixos do plot (o eixo y são os valores obtidos acima)
    eixo_x = ['Africa', "Restante do Mundo"]
    eixo_y = [29106954, 7257465]

    fig = figure(x_range=eixo_x)

    #Atribuição do tipo de plot com os eixos e cores 
    fig.vbar(x=eixo_x, top=eixo_y, width=0.5,
            fill_color=cores,
            line_color = None)
    
    #Customização do plot
    fig.title.text = "Comparação África x Restante do Mundo (1990-2019)"
    fig.title.text_color = "#bc634f"
    fig.title.text_font = "Times"
    fig.title.text_font_size = "18px"
    fig.title.align = "center"

    fig.xaxis.axis_label = ""
    fig.xaxis.major_label_text_font_size = "14px"

    fig.yaxis.axis_label = "Número de Mortes"
    fig.yaxis.major_label_text_font_size = "14px"

    fig.axis.axis_label_text_color = '#bc634f'

    fig.axis.axis_label_text_font_size = "18px"

    return fig

