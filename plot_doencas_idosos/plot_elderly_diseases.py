from bokeh.palettes import brewer
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter

from organizing_data_elderly_diseases import causes, data_deaths_elderly_through_years

import os
os.chdir("plot_doencas_idosos")

#=================================

# mortes causadas por doenças que afetam principalmente a população idosa (doenças cardiovasculares não inclusas)
output_file("deaths_from_old_people_diseases.html")

#=================================

# número de doenças
number_of_causes = len(causes)

# criando plot
plot_elderly_diseases = figure()

# grafico de barra empilhada
plot_elderly_diseases.varea_stack(stackers=causes, x = "Year", color = brewer["RdYlBu"][number_of_causes], legend_label = causes, source = data_deaths_elderly_through_years)

#=================================
#Personalizando

# título
plot_elderly_diseases.title = "Mortes por doenças que mais afetam idosos ao longo dos anos entre 1990 e 2019\nexcluindo-se doenças cardiovasculares em todo o mundo (números em milhões de mortes)"
plot_elderly_diseases.title.text_font_size = "20px"
plot_elderly_diseases.title.text_font = "arial"

# dimensões do gráfico
plot_elderly_diseases.width = 1280
plot_elderly_diseases.height = 720

# background do gráfico
plot_elderly_diseases.background_fill_color = "Red"
plot_elderly_diseases.background_fill_alpha = 0.1

# formatando numeros do eixo y
plot_elderly_diseases.yaxis.formatter = NumeralTickFormatter(format = "0.0a")

#eixos
# rótulos dos eixos
plot_elderly_diseases.xaxis.axis_label = "Ano"
plot_elderly_diseases.yaxis.axis_label = "Mortes"
plot_elderly_diseases.axis.axis_label_text_font_size = "20px"
plot_elderly_diseases.axis.axis_label_text_font = "arial"
# textos dos eixos
plot_elderly_diseases.axis.major_label_text_font_size = "16px"
# ticks dos eixos
# eixo y 
plot_elderly_diseases.yaxis.minor_tick_out = 0
# eixo x
plot_elderly_diseases.xaxis.minor_tick_in = 4
plot_elderly_diseases.xaxis.major_tick_out = 10

# retirando grid
# retirando grids
plot_elderly_diseases.grid.grid_line_color = None

# barra de ferramentas
# Propiedades das ferramentas
plot_elderly_diseases.toolbar.logo = None
plot_elderly_diseases.toolbar.autohide = True

# legenda
plot_elderly_diseases.legend.location = "top_left"

# plotando
show(plot_elderly_diseases)