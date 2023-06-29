from organizing_data_homicides import data_homicides_by_continent, data_homicides_by_continent_proportion, df_homicides_by_continent
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import NumeralTickFormatter

import os
os.chdir("plots_homicidios")

output_file("deaths_by_homicides.html")

# mortes por violencia interpessoal por continente
plot_interpersonal_violence = figure(x_range = df_homicides_by_continent["Continente"].values)

# Título e dimensões do gráfico
plot_interpersonal_violence.title = "Mortes por violencia interpessoal por continente \n entre os anos de 1990 e 2019"
plot_interpersonal_violence.width = 500
plot_interpersonal_violence.height = 500

plot_interpersonal_violence.vbar(x = "Continente", top = "Inverted Interpersonal Violence", fill_color = "Red", width = 0.85, source = data_homicides_by_continent, line_color = None)
plot_interpersonal_violence.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Bakcground do gráfico
plot_interpersonal_violence.background_fill_color = "#242424"
plot_interpersonal_violence.background_fill_alpha = 0.9

# Cor dos eixos
plot_interpersonal_violence.xaxis.minor_tick_line_color = "#000000"
# removendo ticks menores do eixo y
plot_interpersonal_violence.yaxis.minor_tick_out = 0

# Cor do grid
plot_interpersonal_violence.xgrid.grid_line_color = "#666666"
plot_interpersonal_violence.ygrid.grid_line_color = "#666666"

# Colocando rótulos do eixo x na diagonal
plot_interpersonal_violence.xaxis.major_label_orientation = 0.785

#=================================

# mortes por violencia interpessoal por continente
plot_conflict_terrorism = figure(x_range = df_homicides_by_continent["Continente"].values)

# Título e dimensões do gráfico
plot_conflict_terrorism.title = "Mortes por conflitos e terrorismo por continente \n entre os anos de 1990 e 2019"
plot_conflict_terrorism.width = 500
plot_conflict_terrorism.height = 500

plot_conflict_terrorism.vbar(x = "Continente", top = "Inverted Conflict and Terrorism", fill_color = "Red", width = 0.85, source = data_homicides_by_continent, line_color = None)
plot_conflict_terrorism.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Bakcground do gráfico
plot_conflict_terrorism.background_fill_color = "#242424"
plot_conflict_terrorism.background_fill_alpha = 0.9

# Cor dos eixos
plot_conflict_terrorism.xaxis.minor_tick_line_color = "#000000"
# removendo ticks menores do eixo y
plot_conflict_terrorism.yaxis.minor_tick_out = 0

# Cor do grid
plot_conflict_terrorism.xgrid.grid_line_color = "#666666"
plot_conflict_terrorism.ygrid.grid_line_color = "#666666"

# Colocando rótulos do eixo x na diagonal
plot_conflict_terrorism.xaxis.major_label_orientation = 0.785

#================================================================================================

# plots com números em proporção

# mortes por violencia interpessoal por continente em proporção à população total
plot_interpersonal_violence_proportion = figure(x_range = df_homicides_by_continent["Continente"].values)

# Título e dimensões do gráfico
plot_interpersonal_violence_proportion.title = "Mortes por violencia interpessoal por continente em relação \n à população total entre os anos de 1990 a 2019"
plot_interpersonal_violence_proportion.width = 500
plot_interpersonal_violence_proportion.height = 500

plot_interpersonal_violence_proportion.vbar(x = "Continente", top = "Inverted Violence Proportion", fill_color = "Red", width = 0.85, source = data_homicides_by_continent_proportion, line_color = None)
plot_interpersonal_violence_proportion.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Bakcground do gráfico
plot_interpersonal_violence_proportion.background_fill_color = "#242424"
plot_interpersonal_violence_proportion.background_fill_alpha = 0.9

# Cor dos ticks dos eixos
plot_interpersonal_violence_proportion.xaxis.minor_tick_line_color = "#000000"
# removendo ticks do eixo y
plot_interpersonal_violence_proportion.yaxis.minor_tick_out = 0
plot_interpersonal_violence_proportion.yaxis.major_tick_out = 0

# Cor do grid
plot_interpersonal_violence_proportion.xgrid.grid_line_color = "#666666"
plot_interpersonal_violence_proportion.ygrid.grid_line_color = "#666666"

# Rótulo dos eixos
plot_interpersonal_violence_proportion.yaxis.major_label_text_font_size = "0pt"
# Colocando rótulos do eixo x na diagonal
plot_interpersonal_violence_proportion.xaxis.major_label_orientation = 0.785

#=================================

# mortes por conflitos e terrorismo por continente em proporção à população total
plot_conflict_terrorism_proportion = figure(x_range = df_homicides_by_continent["Continente"].values)

# Título e dimensões do gráfico
plot_conflict_terrorism_proportion.title = "Mortes por conflitos e terrorismo por continente em relação \n à população total entre os anos de 1990 e 2019"
plot_conflict_terrorism_proportion.width = 500
plot_conflict_terrorism_proportion.height = 500

plot_conflict_terrorism_proportion.vbar(x = "Continente", top = "Inverted Conflict Proportion", fill_color = "Red", width = 0.85, source = data_homicides_by_continent_proportion, line_color = None)
plot_conflict_terrorism_proportion.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Bakcground do gráfico
plot_conflict_terrorism_proportion.background_fill_color = "#242424"
plot_conflict_terrorism_proportion.background_fill_alpha = 0.9

# Cor dos ticks dos eixos
plot_conflict_terrorism_proportion.xaxis.minor_tick_line_color = "#000000"

# removendo ticks do eixo y
plot_conflict_terrorism_proportion.yaxis.minor_tick_out = 0
plot_conflict_terrorism_proportion.yaxis.major_tick_out = 0

# Cor do grid
plot_conflict_terrorism_proportion.xgrid.grid_line_color = "#666666"
plot_conflict_terrorism_proportion.ygrid.grid_line_color = "#666666"

# Rótulo dos eixos
plot_conflict_terrorism_proportion.yaxis.major_label_text_font_size = "0pt"
# Colocando rótulos do eixo x na diagonal
plot_conflict_terrorism_proportion.xaxis.major_label_orientation = 0.785

#================================================================================================

# grid plot
plot_homicides_continents = gridplot([[plot_interpersonal_violence, plot_conflict_terrorism], [plot_interpersonal_violence_proportion, plot_conflict_terrorism_proportion]])

show(plot_homicides_continents)