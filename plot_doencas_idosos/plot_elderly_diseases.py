from bokeh.palettes import brewer
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter

from organizing_data_elderly_diseases import causes, data_deaths_elderly_through_years

import os
os.chdir("plot_ranking_doencas")

# mortes causadas por doenças que afetam principalmente a população idosa (doenças cardiovasculares não inclusas)
output_file("deaths_from_old_people_diseases.html")

number_of_causes = len(causes)

plot_elderly_diseases = figure()

# título e dimensões do gráfico
plot_elderly_diseases.title = "Mortes por doenças que mais afetam idosos ao longo dos anos entre 1990 e 2019 excluindo-se doenças cardiovasculares \n (números em milhões de mortes)"
# largura responsiva
plot_elderly_diseases.sizing_mode = "stretch_width"
plot_elderly_diseases.min_width = 720
plot_elderly_diseases.height = 720

plot_elderly_diseases.varea_stack(stackers=causes, x = "Year", color = brewer["RdYlBu"][number_of_causes], legend_label = causes, source = data_deaths_elderly_through_years)

plot_elderly_diseases.yaxis.formatter = NumeralTickFormatter(format = "0.0a")

# texto do título
plot_elderly_diseases.title.text_font_size = "20px"

# background do gráfico
plot_elderly_diseases.background_fill_color = "#cccccc"
plot_elderly_diseases.background_fill_alpha = 0.95

# rótulos dos eixos
plot_elderly_diseases.xaxis.axis_label = "Ano"
plot_elderly_diseases.yaxis.axis_label = "Mortes"

# ticks dos eixos
# eixo y 
plot_elderly_diseases.yaxis.minor_tick_out = 0
# eixo x
plot_elderly_diseases.xaxis.minor_tick_in = 4
plot_elderly_diseases.xaxis.major_tick_out = 10

# legenda
plot_elderly_diseases.legend.location = "top_left"

show(plot_elderly_diseases)