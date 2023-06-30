from organizing_data_boxplot import kinds, source_continents_boxplot, outliers

from bokeh.models import ColumnDataSource, Whisker, NumeralTickFormatter, HoverTool
from bokeh.plotting import show, save, output_file, figure
from bokeh.transform import factor_cmap

import os
os.chdir("box_plot")

output_file("boxplot.html")

# ferramenta de interatividade
hover_tool = HoverTool(
    tooltips = [
        ("Pais", "@{Country/Territory}"),
        ("Mortes", "@{Per 100k}")
    ]
)

# criando boxplot
boxplot_cardiovascular_deaths = figure(x_range=kinds)

# adicionando ferramenta de interatividade
boxplot_cardiovascular_deaths.add_tools(hover_tool)

# colocando limites superiores e inferiores
whisker = Whisker(base="kind", upper="upper", lower="lower", source=source_continents_boxplot)
whisker.upper_head.size = whisker.lower_head.size = 20
boxplot_cardiovascular_deaths.add_layout(whisker)

# colorindo barras
cmap = factor_cmap("kind", "TolRainbow7", kinds)
# as caixas do boxplot são gráficos de barra
boxplot_cardiovascular_deaths.vbar("kind", 0.7, "q2", "q3", source=source_continents_boxplot, color=cmap, line_color="black")
boxplot_cardiovascular_deaths.vbar("kind", 0.7, "q1", "q2", source=source_continents_boxplot, color=cmap, line_color="black")

# fazendo outliers com scatter plot
boxplot_cardiovascular_deaths.scatter("kind", "Per 100k", source=outliers, size=6, color="black", alpha=0.3)

#===========================================================================
# Personalizando

# titulo
boxplot_cardiovascular_deaths.title.text = "Distribuição de mortes por doenças cardiovasculares por continente \n por 100 mil habitantes no ano de 2019"
boxplot_cardiovascular_deaths.title.text_font = "arial"
boxplot_cardiovascular_deaths.title.text_font_size = "22px"

# dimensões do plot
boxplot_cardiovascular_deaths.width = 1000
boxplot_cardiovascular_deaths.height = 600

# fundo
boxplot_cardiovascular_deaths.background_fill_color = "Red"
boxplot_cardiovascular_deaths.background_fill_alpha = 0.1

# eixos
# tamanho da fonte do rótulo
boxplot_cardiovascular_deaths.axis.major_label_text_font_size="16px"
# formatando números do eixo y
boxplot_cardiovascular_deaths.yaxis.formatter = NumeralTickFormatter(format = '0.0a')
# titulo do eixo y
boxplot_cardiovascular_deaths.yaxis.axis_label = "Mortes por acidentes cardiovasculares"
# texto do eixo y
boxplot_cardiovascular_deaths.yaxis.axis_label_text_font_size = "20px"
boxplot_cardiovascular_deaths.yaxis.axis_label_text_font = "arial"

# colocando textos do eixo x na diagonal
boxplot_cardiovascular_deaths.xaxis.major_label_orientation = 0.785

# retirando grids
boxplot_cardiovascular_deaths.grid.grid_line_color = None

# barra de ferramentas
# Propiedades das ferramentas
boxplot_cardiovascular_deaths.toolbar.logo = None
boxplot_cardiovascular_deaths.toolbar.autohide = True

# plotando
save(boxplot_cardiovascular_deaths)