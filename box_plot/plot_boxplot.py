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
boxplot = figure(x_range=kinds)

# adicionando ferramenta de interatividade
boxplot.add_tools(hover_tool)

# colocando limites superiores e inferiores
whisker = Whisker(base="kind", upper="upper", lower="lower", source=source_continents_boxplot)
whisker.upper_head.size = whisker.lower_head.size = 20
boxplot.add_layout(whisker)

# colorindo barras
cmap = factor_cmap("kind", "TolRainbow7", kinds)
# as caixas do boxplot são gráficos de barra
boxplot.vbar("kind", 0.7, "q2", "q3", source=source_continents_boxplot, color=cmap, line_color="black")
boxplot.vbar("kind", 0.7, "q1", "q2", source=source_continents_boxplot, color=cmap, line_color="black")

# fazendo outliers com scatter plot
boxplot.scatter("kind", "Per 100k", source=outliers, size=6, color="black", alpha=0.3)

#===========================================================================

# Personalizando

# dimensões do plot
boxplot.width = 1000
boxplot.height = 600

# titulo
boxplot.title.text = "Distribuição de mortes por doenças cardiovasculares por continente \n por 100 mil habitantes no ano de 2019"
boxplot.title.text_font = "arial"
boxplot.title.text_font_size = "22px"
boxplot.title.align = "center"

# eixos
boxplot.axis.major_label_text_font_size="16px"
# eixoy
boxplot.yaxis.formatter = NumeralTickFormatter(format = '0.0a')
boxplot.yaxis.axis_label = "Mortes por acidentes cardiovasculares"
boxplot.yaxis.axis_label_text_font_size = "20px"
boxplot.yaxis.axis_label_text_font = "arial"

# retirando grids
boxplot.grid.grid_line_color = None

save(boxplot)