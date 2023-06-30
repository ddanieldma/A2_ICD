from ColumnDataSource import cds_timeline, df_africa_hiv_timeline
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.models import BoxAnnotation

def plot_3():

    grid4_fig = figure()

    #Atribuição do tipo de plot
    grid4_fig.line(x="Year", y="HIV/AIDS", source=cds_timeline, line_color = '#8b0000')
    
    hover = HoverTool(tooltips=[("Mortes", "$y{0,0}"), ("Ano", "@Year")], mode='vline')
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

    grid4_fig.background_fill_color = "red"
    grid4_fig.background_fill_alpha = 0.1

    #box annotation:
    x_box = (2002, 2006)
    y_box = (1400000, 1600000)
    box_annotation = BoxAnnotation(left=x_box[0], right=x_box[1], bottom=y_box[0], top=y_box[1], fill_color='red', fill_alpha=0.3)

    #add text
    text_labels = ['Pico de Mortes no Ano de 2004']
    grid4_fig.text(x=2012, y=1460000, text=text_labels, text_font_size='11pt', text_color='red', text_align='center')
    grid4_fig.add_layout(box_annotation)

    return grid4_fig