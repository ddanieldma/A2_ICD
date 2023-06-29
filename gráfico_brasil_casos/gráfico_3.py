import sys
sys.path.append('../A2_ICD')
from analisando_a_base import df_causas_de_morte_Brasil
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, BasicTicker, PrintfTickFormatter, HoverTool
from bokeh.transform import linear_cmap
from math import pi

# Definindo os anos como string para poder plotar os gráficos
df_causas_de_morte_Brasil["Year"]=df_causas_de_morte_Brasil["Year"].astype(str)

df_causas_de_morte_Brasil["Percentual change in the population"]= df_causas_de_morte_Brasil["Population"].pct_change()*100
df_causas_de_morte_Brasil["Percentual change in the deaths"] = df_causas_de_morte_Brasil["Total Deaths"].pct_change()*100
df_causas_de_morte_Brasil["Percental change in the 100k deaths"] = df_causas_de_morte_Brasil["Deaths per 100k"].pct_change()*100
df_causas_de_morte_Brasil["pct_pop - pct_death"]= df_causas_de_morte_Brasil["Percentual change in the population"]-df_causas_de_morte_Brasil["Percentual change in the deaths"]
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil.dropna()

# Transformando o nosso datafram em ColumnDataSource
source = ColumnDataSource(df_causas_de_morte_Brasil)

# Gráfico anos e mortes por 100k
grafico_anos_mortes_100k = figure(x_range=df_causas_de_morte_Brasil["Year"], title="Deaths per 100k over the years")

grafico_anos_mortes_100k.line(x="Year", y="Deaths per 100k", source=source)

# Gráfico anos e mortes
grafico_anos_mortes = figure(x_range = df_causas_de_morte_Brasil["Year"])

grafico_anos_mortes.line(x="Year", y = "Total Deaths", source = source)

# Gráfico população

grafico_anos_pop = figure(x_range = df_causas_de_morte_Brasil["Year"])

grafico_anos_pop.line(x="Year", y = "Population", source = source)

# Gráfico percentual change
grafico_percentual = figure(x_range = df_causas_de_morte_Brasil["Year"])

grafico_percentual.vbar(x= "Year", top = "pct_pop - pct_death", width = 0.8 , fill_alpha = 0.2 ,source = source)
grafico_percentual.line(x = "Year", y= "Percentual change in the population", line_color = "red", source = source)
grafico_percentual.line(x = "Year", y= "Percentual change in the deaths", line_color = "purple", source = source)

combinados = gridplot([[grafico_anos_mortes, grafico_anos_pop],[grafico_anos_mortes_100k],[grafico_percentual]])
show(combinados)
