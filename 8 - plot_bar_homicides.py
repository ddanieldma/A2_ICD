from organizing_data_homicides import data_homicides_by_continent, source_homicides_by_continent_proportion, df_homicides_by_continent
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import NumeralTickFormatter, Span, Label

def grafico_padrao(figure):
		# fonte do titulo
		figure.title.text_font = "arial"
		figure.title.text_font_size = "14px"
		
		# dimensões dos gráficos
		figure.width = 500
		figure.height = 500
		
		# fundo do gráfico
		figure.background_fill_color = "#242424"
		figure.background_fill_alpha = 0.9

		# Cor dos eixos
		figure.xaxis.minor_tick_line_color = "#000000"
		# removendo ticks menores do eixo y
		figure.yaxis.minor_tick_out = 0

		# retirando grids
		figure.grid.grid_line_color = None

		# Colocando rótulos do eixo x na diagonal
		figure.xaxis.major_label_orientation = 0.785
		
		# eixos
		# tamanho da fonte dos rótulos
		figure.axis.major_label_text_font_size="14px"
		# formatando números do eixo y
		figure.yaxis.formatter = NumeralTickFormatter(format = '0.0a')
		
		# texto do eixo y
		figure.yaxis.axis_label_text_font_size = "14px"
		figure.yaxis.axis_label_text_font = "arial"

		return figure
    

output_file("deaths_by_homicides.html")

#=================================
# mortes por violencia interpessoal por continente
plot_interpersonal_violence = figure(x_range = df_homicides_by_continent["Continente"].values)

# fazendo gráfico
plot_interpersonal_violence.vbar(x = "Continente", top = "Inverted Interpersonal Violence", fill_color = "Red", width = 0.85, source = data_homicides_by_continent, line_color = None)

#=================================

# adicionando anotação
# adicionando span no primerio gráfico
linha_3_milhões = Span(location = -3000000, dimension = "width", line_color = "Orange", line_width = 3)

# adicionando texto referente a linha
text = Label(x = 200, y = 110, x_units = "screen", y_units = "screen", text = "Mais de 273 mortes\n por dia", text_color = "Orange")

#colocando linha no plot
plot_interpersonal_violence.add_layout(linha_3_milhões)
plot_interpersonal_violence.add_layout(text)

#=================================

# Personalizando

# Título do gráfico
plot_interpersonal_violence.title = "Mortes por violencia interpessoal por continente \n entre os anos de 1990 e 2019"

# colocando configuração padrão do gráfico
plot_interpersonal_violence = grafico_padrao(plot_interpersonal_violence)

# titulo do eixo y
plot_interpersonal_violence.yaxis.axis_label = "Mortes"

#=================================
# mortes por violencia interpessoal por continente
plot_conflict_terrorism = figure(x_range = df_homicides_by_continent["Continente"].values)

# fazendo gráfico
plot_conflict_terrorism.vbar(x = "Continente", top = "Inverted Conflict and Terrorism", fill_color = "Red", width = 0.85, source = data_homicides_by_continent, line_color = None)

# Personalizando

# Título do gráfico
plot_conflict_terrorism.title = "Mortes por conflitos e terrorismo por continente \n entre os anos de 1990 e 2019"

# colocando configuração padrão do gráfico
plot_conflict_terrorism = grafico_padrao(plot_conflict_terrorism)

# titulo do eixo y
plot_conflict_terrorism.yaxis.axis_label = "Mortes"

#================================================================================================
# plots com números em proporção

# mortes por violencia interpessoal por continente em proporção à população total
plot_interpersonal_violence_proportion = figure(x_range = df_homicides_by_continent["Continente"].values)

plot_interpersonal_violence_proportion.vbar(x = "Continente", top = "Inverted Violence Proportion", fill_color = "Red", width = 0.85, source = source_homicides_by_continent_proportion, line_color = None)
plot_interpersonal_violence_proportion.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Personalizando

# Título do gráfico
plot_interpersonal_violence_proportion.title = "Mortes por violencia interpessoal por continente em relação \n à população total entre os anos de 1990 a 2019"

# removendo tixks eixo y
plot_interpersonal_violence_proportion.yaxis.minor_tick_out = 0
plot_interpersonal_violence_proportion.yaxis.major_tick_out = 0

# colocando configuração padrão do gráfico
plot_interpersonal_violence_proportion = grafico_padrao(plot_interpersonal_violence_proportion)

# Rótulo dos eixos
plot_interpersonal_violence_proportion.yaxis.major_label_text_font_size = "0pt"
# Colocando rótulos do eixo x na diagonal
plot_interpersonal_violence_proportion.xaxis.major_label_orientation = 0.785

#=================================

# mortes por conflitos e terrorismo por continente em proporção à população total
plot_conflict_terrorism_proportion = figure(x_range = df_homicides_by_continent["Continente"].values)

plot_conflict_terrorism_proportion.vbar(x = "Continente", top = "Inverted Conflict Proportion", fill_color = "Red", width = 0.85, source = source_homicides_by_continent_proportion, line_color = None)
plot_conflict_terrorism_proportion.yaxis.formatter = NumeralTickFormatter(format = '0.0a')

# Personalizando

# Título do gráfico
plot_conflict_terrorism_proportion.title = "Mortes por conflitos e terrorismo por continente em relação \n à população total entre os anos de 1990 e 2019"

# removendo ticks do eixo y
plot_conflict_terrorism_proportion.yaxis.minor_tick_out = 0
plot_conflict_terrorism_proportion.yaxis.major_tick_out = 0

# colocando configuração padrão do gráfico
plot_conflict_terrorism_proportion = grafico_padrao(plot_conflict_terrorism_proportion)

# Rótulo dos eixos
plot_conflict_terrorism_proportion.yaxis.major_label_text_font_size = "0pt"
# Colocando rótulos do eixo x na diagonal
plot_conflict_terrorism_proportion.xaxis.major_label_orientation = 0.785

#================================================================================================

# colocando todos em grid plot
plot_homicides_continents = gridplot([[plot_interpersonal_violence, plot_conflict_terrorism], [plot_interpersonal_violence_proportion, plot_conflict_terrorism_proportion]])

# configuração da barra de ferramentas
# Propiedades das ferramentas
plot_homicides_continents.toolbar.logo = None
plot_homicides_continents.toolbar.autohide = True