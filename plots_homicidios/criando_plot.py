from organizando_dados import index_values, data_homicides_by_continent
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import NumeralTickFormatter

output_file("deaths_by_homicides.html")

# mortes por violencia interpessoal por continente
plot_interpersonal_violence = figure(width = 420, height = 420, title = "Mortes por violência interpessoal", x_range = index_values)
plot_interpersonal_violence.vbar(x = "Continente", top = "Interpersonal Violence", source = data_homicides_by_continent)
plot_interpersonal_violence.yaxis.formatter = NumeralTickFormatter(format = '0,0')

# mortes por conflitos e terrorismo por continente
plot_conflict_terrorism = figure(width = 420, height = 420, title = "Mortes por conflitos e terrorismo", x_range = index_values)
plot_conflict_terrorism.vbar(x = "Continente", top = "Conflict and Terrorism", source = data_homicides_by_continent)
plot_conflict_terrorism.yaxis.formatter = NumeralTickFormatter(format = '0,0')

# grid plot
plot_mortes_por_homicidios = gridplot([[plot_interpersonal_violence], [plot_conflict_terrorism]])

show(plot_mortes_por_homicidios)