from organizing_data_boxplot import kinds, source_continents_boxplot, outliers

from bokeh.models import ColumnDataSource, Whisker, NumeralTickFormatter
from bokeh.plotting import show, output_file, figure
from bokeh.transform import factor_cmap

output_file("boxplot.html")

boxplot = figure(x_range=kinds, title="Distribuição de mortes por doenças cardiovasculares por continente", background_fill_color="#eaefef", y_axis_label="Mortes por acidentes cardiovasculares")
boxplot.sizing_mode = "stretch_width"
boxplot.min_width = 720
boxplot.height = 720

# outlier range
whisker = Whisker(base="kind", upper="upper", lower="lower", source=source_continents_boxplot)
whisker.upper_head.size = whisker.lower_head.size = 20
boxplot.add_layout(whisker)

# colorindo barras
cmap = factor_cmap("kind", "TolRainbow7", kinds)
# as caixas do boxplot são gráficos de barar
boxplot.vbar("kind", 0.7, "q2", "q3", source=source_continents_boxplot, color=cmap, line_color="black")
boxplot.vbar("kind", 0.7, "q1", "q2", source=source_continents_boxplot, color=cmap, line_color="black")

# fazendo outliers com scatter plot
boxplot.scatter("kind", "Cardiovascular Diseases", source=outliers, size=6, color="black", alpha=0.3)

boxplot.yaxis.formatter = NumeralTickFormatter(format = '0.0a')
boxplot.xgrid.grid_line_color = None
boxplot.axis.major_label_text_font_size="14px"
boxplot.axis.axis_label_text_font_size="12px"

show(boxplot)