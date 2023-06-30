from ColumnDataSource import cds_af_x_all, cores_af_x_all, eixo_x_afxall, eixo_y_afxall
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

def plot_2():
    
    grid2_fig = figure(x_range=eixo_x_afxall)

    hover = HoverTool(tooltips=[("Mortes", "@top")], mode='vline')
    grid2_fig.add_tools(hover)

    #Atribuição do tipo de plot com os eixos e cores desejados
    grid2_fig.vbar(x=eixo_x_afxall, top=eixo_y_afxall, width=0.5,
            fill_color=cores_af_x_all,
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

    grid2_fig.background_fill_color = "red"
    grid2_fig.background_fill_alpha = 0.1

    return grid2_fig

