from ColumnDataSource import cds_timeline, df_africa_hiv_timeline
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

def plot_3():

    grid4_fig = figure()

    #Atribuição do tipo de plot
    grid4_fig.line(x="Year", y="HIV/AIDS", source=cds_timeline, line_color = '#8b0000')
    
    hover = HoverTool(tooltips=[("Mortes:", "$y{0,0}"), ("Ano:", "@Year")], mode='vline')
    grid4_fig.add_tools(hover)

    #Customização do plot
    grid4_fig.title.text = "Número de Mortes por Aids/HIV na África (Linha do Tempo)"
    grid4_fig.title.text_color = "#bc634f"
    grid4_fig.title.text_font = "Arial"
    grid4_fig.title.text_font_size = "18px"
    grid4_fig.title.align = "center"

    grid4_fig.xaxis.axis_label = "Ano"
    grid4_fig.xaxis.major_label_text_font_size = "14px"

    grid4_fig.yaxis.axis_label = "Número de Mortes"
    grid4_fig.yaxis.major_label_text_font_size = "14px"
    grid4_fig.yaxis[0].formatter = NumeralTickFormatter(format='0a')

    grid4_fig.axis.axis_label_text_color = '#bc634f'

    grid4_fig.axis.axis_label_text_font_size = "18px"

    grid4_fig.outline_line_color = "black"

    # Tirando o Grid
    grid4_fig.xgrid.grid_line_color = None
    grid4_fig.ygrid.grid_line_color = None

    return grid4_fig