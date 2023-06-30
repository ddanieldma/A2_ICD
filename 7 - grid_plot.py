from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from ColumnDataSource import cds_comp_continentes, cores_continentes, continentes, df_cont_hiv, cds_timeline, df_africa_hiv_timeline, df_countries_hiv, cds_top_10, cds_af_x_all, cores_af_x_all, eixo_x_afxall, eixo_y_afxall
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, BoxAnnotation
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

    grid1_fig.background_fill_color = "red"
    grid1_fig.background_fill_alpha = 0.1

    return grid1_fig


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

    grid3_fig.background_fill_color = "red"
    grid3_fig.background_fill_alpha = 0.1

    return grid3_fig


#Após importar as função, atribuímos uma variável a cada
plot_1 = plot_1()
plot_2 = plot_2()
plot_3 = plot_3()
plot_4 = plot_4()

#criação do grid plot (são utilizadas duas listas para que o grid fique 2x2)
grid_hiv_africa = gridplot([[plot_1, plot_2], [plot_3, plot_4]])

grid_hiv_africa.toolbar.autohide = True
grid_hiv_africa.toolbar.logo = None

output_file("grid_plot.html")

save(grid_hiv_africa)
show(grid_hiv_africa)