from ColumnDataSource import cds_comp_continentes, cores_continentes, continentes, df_cont_hiv
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool

def plot_1():
    
    grid1_fig = figure(x_range=df_cont_hiv['Continente'])  
    #A inserção do x_range é necessária para a criação dos bar charts
    #Sua função é atribuir as categorias da coluna ao eixo x.

    #Atribuição do tipo de plot + aplicação da paleta
    grid1_fig.vbar(x= 'Continente', top= 'HIV/AIDS', source=cds_comp_continentes, width=0.5,
            fill_color=factor_cmap('Continente', palette = cores_continentes, factors=continentes),
            line_color = None)
    
    #Adicionando o hovertool para a vizualização do continente e da quantidade de mortes
    hover = HoverTool(tooltips=[("Continente", "@Continente"),("Mortes", "@{HIV/AIDS}{0,0}")])
    grid1_fig.add_tools(hover)

    #Customização do plot
    grid1_fig.title.text = "Mortes em Decorrência de Aids/HIV por Continente (1990-2019)"
    grid1_fig.title.text_color = "#bc634f"
    grid1_fig.title.text_font = "Arial"
    grid1_fig.title.text_font_size = "18px"
    grid1_fig.title.align = "center"

    grid1_fig.xaxis.axis_label = "Continente"
    grid1_fig.xaxis.major_label_text_font_size = "14px"

    grid1_fig.yaxis.axis_label = "Número de Mortes"
    grid1_fig.yaxis.major_label_text_font_size = "14px"
    grid1_fig.yaxis[0].formatter = NumeralTickFormatter(format='0a')

    grid1_fig.axis.axis_label_text_color = '#bc634f'

    grid1_fig.axis.axis_label_text_font_size = "18px"
    
    grid1_fig.outline_line_color = "black"
    
    # Tirando o Grid
    grid1_fig.xgrid.grid_line_color = None
    grid1_fig.ygrid.grid_line_color = None

    return grid1_fig


