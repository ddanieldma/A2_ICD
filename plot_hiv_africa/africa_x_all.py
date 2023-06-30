import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

def plot_2():
    
    #Leitura do csv
    df = pd.read_csv("../new_cause_of_death.csv")

    #Filtragem por continente + soma dos registros de mortes por HIV/AIDS de cada um
    df_cont_hiv = df.groupby('Continente')['HIV/AIDS'].sum().reset_index()

    #Determinação das cores a serem utilizadas no plot
    cores = ['#8b0000', '#bc634f']

    #Obtendo numero de mortes em decorrência do HIV na África
    mortes_africa = df_cont_hiv.loc[df_cont_hiv['Continente'] == "Africa", 'HIV/AIDS']
   
    #Obtendo numero de mortes em decorrência do HIV no restante do mundo
    mortes_resto_mundo = df_cont_hiv.loc[df_cont_hiv['Continente'] != "Africa", 'HIV/AIDS'].sum()

    #Criação dos eixos do plot (o eixo y são os valores obtidos acima)
    eixo_x = ['Africa', "Restante do Mundo"]
    eixo_y = [mortes_africa, mortes_resto_mundo]

    grid2_fig = figure(x_range=eixo_x)

    source = ColumnDataSource(data=dict(x=eixo_x, y=eixo_y))

    hover = HoverTool(tooltips=[("Mortes:", "@top")], mode='vline')
    grid2_fig.add_tools(hover)

    #Atribuição do tipo de plot com os eixos e cores desejados
    grid2_fig.vbar(x=eixo_x, top=eixo_y, width=0.5,
            fill_color=cores,
            line_color = None)
    
    #Customização do plot
    grid2_fig.title.text = "Comparação África x Restante do Mundo (1990-2019)"
    grid2_fig.title.text_color = "#bc634f"
    grid2_fig.title.text_font = "Arial"
    grid2_fig.title.text_font_size = "18px"
    grid2_fig.title.align = "center"

    grid2_fig.xaxis.axis_label = ""
    grid2_fig.xaxis.major_label_text_font_size = "14px"

    grid2_fig.yaxis.axis_label = "Número de Mortes"
    grid2_fig.yaxis.major_label_text_font_size = "14px"
    grid2_fig.yaxis[0].formatter = NumeralTickFormatter(format='0a')

    grid2_fig.axis.axis_label_text_color = '#bc634f'

    grid2_fig.axis.axis_label_text_font_size = "18px"

    grid2_fig.outline_line_color = "black"
    
    # Tirando o Grid
    grid2_fig.xgrid.grid_line_color = None
    grid2_fig.ygrid.grid_line_color = None

    return grid2_fig

