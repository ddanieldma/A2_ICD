from organizing_data import index_values, data_homicides_by_continent
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import NumeralTickFormatter, Title

output_file("deaths_by_homicides.html")

# mortes por violencia interpessoal por continente
plot_interpersonal_violence = figure(width = 420, height = 420, y_range = index_values, title = "Mortes por violência interpessoal")
plot_interpersonal_violence.hbar(y = "Continente", right = "Interpersonal Violence",  line_color = "Black", height = 0.3, fill_color = "Color", source = data_homicides_by_continent)
plot_interpersonal_violence.xaxis.formatter = NumeralTickFormatter(format = '0.0a')

# mortes por conflitos e terrorismo por continente
plot_conflict_terrorism = figure(width = 420, height = 420, y_range = index_values, title = "Mortes por conflitos e terrorismo")
plot_conflict_terrorism.hbar(y = "Continente", right = "Conflict and Terrorism", line_color = "Black", height = 0.3, fill_color = "Color", source = data_homicides_by_continent)
plot_conflict_terrorism.xaxis.formatter = NumeralTickFormatter(format = '0.0a')

# grid plot
plot_mortes_por_homicidio = gridplot([[plot_interpersonal_violence], [plot_conflict_terrorism]])

show(plot_mortes_por_homicidio)