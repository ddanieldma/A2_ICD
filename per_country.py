from ColumnDataSource import df_countries_hiv, cds_top_10
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import HoverTool

def plot_4():

    grid3_fig = figure(x_range=df_countries_hiv['Country/Territory'])
    #A inserção do x_range é necessária para a criação dos bar charts. Sua função é atribuir as categorias da coluna ao eixo x.

    #Atribuição do tipo de plot
    grid3_fig.vbar(x='Country/Territory', top='per_100k_hab', source=cds_top_10, width = 0.8, fill_color = '#bc634f', line_color = None)

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

    hover = HoverTool(tooltips=[("País", "@{Country/Territory}")])
    grid3_fig.add_tools(hover)

    return grid3_fig


