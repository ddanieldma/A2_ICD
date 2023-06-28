from organizing_data_homicides import data_homicides_by_continent, df_homicides_by_continent
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import NumeralTickFormatter

output_file("deaths_by_homicides.html")

# mortes por violencia interpessoal por continente
plot_interpersonal_violence = figure(x_range = df_homicides_by_continent["Continente"].values)

# Título e dimensões do gráfico
plot_interpersonal_violence.title = "Mortes por violencia interpessoal por continente"
plot_interpersonal_violence.width = 400
plot_interpersonal_violence.height = 400

plot_interpersonal_violence.vbar(x = "Continente", top = "Inverted Interpersonal Violence", fill_color = "Red", width = 0.85, source = data_homicides_by_continent, line_color = None)
plot_interpersonal_violence.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Bakcground do gráfico
plot_interpersonal_violence.background_fill_color = "#242424"
plot_interpersonal_violence.background_fill_alpha = 0.9

# Cor dos eixos
plot_interpersonal_violence.xaxis.minor_tick_line_color = "#000000"

# Cor do grid
plot_interpersonal_violence.xgrid.grid_line_color = "#666666"
plot_interpersonal_violence.ygrid.grid_line_color = "#666666"



# mortes por violencia interpessoal por continente
plot_conflict_terrorism = figure(x_range = df_homicides_by_continent["Continente"].values)

# Título e dimensões do gráfico
plot_conflict_terrorism.title = "Mortes por conflitos e terrorismo por continente"
plot_conflict_terrorism.width = 400
plot_conflict_terrorism.height = 400

plot_conflict_terrorism.vbar(x = "Continente", top = "Inverted Conflict and Terrorism", fill_color = "Red", width = 0.85, source = data_homicides_by_continent, line_color = None)
plot_conflict_terrorism.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Bakcground do gráfico
plot_conflict_terrorism.background_fill_color = "#242424"
plot_conflict_terrorism.background_fill_alpha = 0.9

# Cor dos eixos
plot_conflict_terrorism.xaxis.minor_tick_line_color = "#000000"

# Cor do grid
plot_conflict_terrorism.xgrid.grid_line_color = "#666666"
plot_conflict_terrorism.ygrid.grid_line_color = "#666666"

plot_homicides_continents = gridplot([[plot_interpersonal_violence, plot_conflict_terrorism]])

show(plot_homicides_continents)