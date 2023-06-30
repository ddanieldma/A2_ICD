import sys
sys.path.append('../A2_ICD')
from analisando_a_base import df_causas_de_morte_Brasil
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, BasicTicker, PrintfTickFormatter, HoverTool, LinearColorMapper, NumeralTickFormatter
from bokeh.transform import linear_cmap
from math import pi

# Definindo os anos como string para poder plotar os gráficos
df_causas_de_morte_Brasil["Year"]=df_causas_de_morte_Brasil["Year"].astype(str)

df_causas_de_morte_Brasil["Percentual change in the population"]= df_causas_de_morte_Brasil["Population"].pct_change()
df_causas_de_morte_Brasil["Percentual change in the deaths"] = df_causas_de_morte_Brasil["Total Deaths"].pct_change()
df_causas_de_morte_Brasil["Percental change in the 100k deaths"] = df_causas_de_morte_Brasil["Deaths per 100k"].pct_change()
df_causas_de_morte_Brasil["pct_pop - pct_death"]= df_causas_de_morte_Brasil["Percentual change in the population"]-df_causas_de_morte_Brasil["Percentual change in the deaths"]
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil.dropna()

#Adicionando coluna para a cor
def verde_ou_vermelho(x):
    if x > 0:
        return 'green'
    else:
        return 'red'
df_causas_de_morte_Brasil.loc[:, 'Cor'] = df_causas_de_morte_Brasil['pct_pop - pct_death'].apply(verde_ou_vermelho)

# Transformando o nosso datafram em ColumnDataSource
source = ColumnDataSource(df_causas_de_morte_Brasil)

#-------------------------------------------------------------------------------------

# Gráfico anos e mortes por 100k
grafico_anos_mortes_100k = figure(x_range=df_causas_de_morte_Brasil["Year"],
                                 tools="box_zoom,pan,reset,save,wheel_zoom")
grafico_anos_mortes_100k.line(x="Year", y="Deaths per 100k", line_color = "black" ,source=source)

# Adicionando interatividade ao gráfico
interativo_anos_mortes_100k = HoverTool(tooltips=[("Ano", "@Year"), ("Mortes por 100 mil habitantes", "@{Deaths per 100k}")])
grafico_anos_mortes_100k.add_tools(interativo_anos_mortes_100k)

# Adicionando propriedades aos títulos do gráfico
grafico_anos_mortes_100k.title.text = "Quantidade de mortes a cada 100 mil habitantes de 1990 - 2019"
grafico_anos_mortes_100k.title.text_color = "Black"
grafico_anos_mortes_100k.title.text_font = "Arial"
grafico_anos_mortes_100k.title.text_font_size = "15px"
grafico_anos_mortes_100k.title.align = "center"

# Modificando o tamanho do output
grafico_anos_mortes_100k.width = 700
grafico_anos_mortes_100k.height = 400

#Definindo propriedades do eixo

grafico_anos_mortes_100k.xaxis.axis_label = "Anos"
grafico_anos_mortes_100k.xaxis.minor_tick_line_color = "black"
grafico_anos_mortes_100k.axis.minor_tick_in = 0
grafico_anos_mortes_100k.xaxis.major_label_orientation = pi/3
grafico_anos_mortes_100k.xaxis.major_label_text_font_size = "9pt"

grafico_anos_mortes_100k.yaxis.axis_label = "Quantidade de mortes a cada 100 mil habitantes"
grafico_anos_mortes_100k.yaxis.major_label_orientation = "horizontal"
grafico_anos_mortes_100k.yaxis.minor_tick_line_color = "black"
grafico_anos_mortes_100k.yaxis.minor_tick_line_color = None

# Definindo a borda
grafico_anos_mortes_100k.outline_line_color = "black"

# Tirando o Grid
grafico_anos_mortes_100k.xgrid.grid_line_color = None
grafico_anos_mortes_100k.ygrid.grid_line_color = None

# Propiedades das ferramentas
grafico_anos_mortes_100k.toolbar.logo = None
grafico_anos_mortes_100k.toolbar.autohide = True

#-------------------------------------------------------------------------------------
# Gráfico anos e mortes
grafico_anos_mortes = figure(x_range = df_causas_de_morte_Brasil["Year"])
grafico_anos_mortes.line(x="Year", y = "Total Deaths", line_color = "black" ,source = source)

interativo_anos_mortes = HoverTool(tooltips=[("Ano", "@Year"), ("Mortes", "@{Total Deaths}")])
grafico_anos_mortes.add_tools(interativo_anos_mortes)

# Adicionando propriedades aos títulos do gráfico
grafico_anos_mortes.title.text = "Quantidade de mortes de 1990 - 2019"
grafico_anos_mortes.title.text_color = "Black"
grafico_anos_mortes.title.text_font = "Arial"
grafico_anos_mortes.title.text_font_size = "15px"
grafico_anos_mortes.title.align = "center"

# Modificando o tamanho do output
grafico_anos_mortes.width = 700
grafico_anos_mortes.height = 400

#Definindo propriedades do eixo

grafico_anos_mortes.xaxis.axis_label = "Anos"
grafico_anos_mortes.xaxis.minor_tick_line_color = "black"
grafico_anos_mortes.xaxis.minor_tick_in = 0
grafico_anos_mortes.xaxis.major_label_orientation = pi/3
grafico_anos_mortes.xaxis.major_label_text_font_size = "9pt"

grafico_anos_mortes.yaxis.formatter = NumeralTickFormatter(format="0.0a")
grafico_anos_mortes.yaxis.axis_label = "Quantidade de mortos"
grafico_anos_mortes.yaxis.major_label_orientation = "horizontal"
grafico_anos_mortes.yaxis.minor_tick_line_color = "black"
grafico_anos_mortes.yaxis.minor_tick_line_color = None

# Definindo a borda
grafico_anos_mortes.outline_line_color = "black"

# Tirando o Grid
grafico_anos_mortes.xgrid.grid_line_color = None
grafico_anos_mortes.ygrid.grid_line_color = None

# Propiedades das ferramentas
grafico_anos_mortes.toolbar.logo = None
grafico_anos_mortes.toolbar.autohide = True
# Tirando o Grid
grafico_anos_mortes.xgrid.grid_line_color = None
grafico_anos_mortes.ygrid.grid_line_color = None

#-------------------------------------------------------------------------------------

# Gráfico população

grafico_anos_pop = figure(x_range = df_causas_de_morte_Brasil["Year"])
grafico_anos_pop.line(x="Year", y = "Population", line_color = "black",source = source)

interativo_anos_pop = HoverTool(tooltips=[("Ano", "@Year"), ("População", "@Population")])
grafico_anos_pop.add_tools(interativo_anos_pop)

# Adicionando propriedades aos títulos do gráfico
grafico_anos_pop.title.text = "População Brasileira de 1990 - 2019"
grafico_anos_pop.title.text_color = "Black"
grafico_anos_pop.title.text_font = "Arial"
grafico_anos_pop.title.text_font_size = "15px"
grafico_anos_pop.title.align = "center"

# Modificando o tamanho do output
grafico_anos_pop.width = 700
grafico_anos_pop.height = 400

#Definindo propriedades do eixo

grafico_anos_pop.xaxis.axis_label = "Anos"
grafico_anos_pop.xaxis.minor_tick_line_color = "black"
grafico_anos_pop.xaxis.minor_tick_in = 0
grafico_anos_pop.xaxis.major_label_orientation = pi/3
grafico_anos_pop.xaxis.major_label_text_font_size = "9pt"

grafico_anos_pop.yaxis.axis_label = "População Brasileira"
grafico_anos_pop.yaxis.formatter = NumeralTickFormatter(format="0.0a")
grafico_anos_pop.yaxis.major_label_orientation = "horizontal"
grafico_anos_pop.yaxis.minor_tick_line_color = "black"
grafico_anos_pop.yaxis.minor_tick_line_color = None

# Definindo a borda
grafico_anos_pop.outline_line_color = "black"

# Tirando o Grid
grafico_anos_pop.xgrid.grid_line_color = None
grafico_anos_pop.ygrid.grid_line_color = None

# Propiedades das ferramentas
grafico_anos_pop.toolbar.logo = None
grafico_anos_pop.toolbar.autohide = True
# Tirando o Grid
grafico_anos_pop.xgrid.grid_line_color = None
grafico_anos_pop.ygrid.grid_line_color = None

#-------------------------------------------------------------------------------------

# Gráfico percentual change
grafico_percentual = figure(x_range = df_causas_de_morte_Brasil["Year"])

grafico_percentual.vbar(x= "Year", top = "pct_pop - pct_death", width = 0.8 , color = "Cor", fill_alpha = 0.4, line_alpha = 0.4 ,source = source)
# grafico_percentual.line(x = "Year", y= "Percentual change in the population", line_color = "red", source = source)
# grafico_percentual.line(x = "Year", y= "Percentual change in the deaths", line_color = "purple", source = source)

interativo_anos_pop = HoverTool(tooltips=[("Ano", "@Year"), ("Diferença de porcentagens", "@{pct_pop - pct_death}")])
grafico_percentual.add_tools(interativo_anos_pop)

# Adicionando propriedades aos títulos do gráfico
grafico_percentual.title.text = "Diferença entre a taxa de crescimento da população e a taxa de crescimento de mortes"
grafico_percentual.title.text_color = "Black"
grafico_percentual.title.text_font = "Arial"
grafico_percentual.title.text_font_size = "15px"
grafico_percentual.title.align = "center"

# Modificando o tamanho do output
grafico_percentual.width = 700
grafico_percentual.height = 400

#Definindo propriedades do eixo

grafico_percentual.xaxis.axis_label = "Anos"
grafico_percentual.xaxis.minor_tick_line_color = "black"
grafico_percentual.xaxis.minor_tick_in = 0
grafico_percentual.xaxis.major_label_orientation = pi/3
grafico_percentual.xaxis.major_label_text_font_size = "9pt"

grafico_percentual.yaxis.axis_label = "Diferença percentual (*100)"
grafico_percentual.yaxis.formatter = NumeralTickFormatter(format="0.0%")
grafico_percentual.yaxis.major_label_orientation = "horizontal"
grafico_percentual.yaxis.minor_tick_line_color = "black"
grafico_percentual.yaxis.minor_tick_line_color = None

# Definindo a borda
grafico_percentual.outline_line_color = "black"

# Tirando o Grid
grafico_percentual.xgrid.grid_line_color = None
grafico_percentual.ygrid.grid_line_color = None

# Propiedades das ferramentas
grafico_percentual.toolbar.logo = None
grafico_percentual.toolbar.autohide = True

# Tirando o Grid
grafico_percentual.xgrid.grid_line_color = None
grafico_percentual.ygrid.grid_line_color = None

#-------------------------------------------------------------------------------------

combinados = gridplot([[grafico_anos_mortes, grafico_anos_pop],[grafico_anos_mortes_100k, grafico_percentual]])
show(combinados)
