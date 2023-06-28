from bokeh.palettes import brewer
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter

from organizing_data_elderly_diseases import causes, data_deaths_elderly_through_years

output_file("deaths_from_old_people_diseases.html")

number_of_causes = len(causes)

plot_elderly_diseases = figure()

# título e dimensões do gráfico
plot_elderly_diseases.title = "Mortes por doenças que mais afetam idosos ao longo dos anos entre 1990 e 2019 excluindo-se doenças cardiovasculares \n (números em milhões de mortes)"
# largura responsiva
plot_elderly_diseases.sizing_mode = "stretch_width"
plot_elderly_diseases.height = 720

plot_elderly_diseases.varea_stack(stackers=causes, x = "Year", color = brewer["RdYlBu"][number_of_causes], legend_label = causes, source = data_deaths_elderly_through_years)
plot_elderly_diseases.yaxis.formatter = NumeralTickFormatter(format = "0.0a")

show(plot_elderly_diseases)