import pandas as pd
import math
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource 
from analisando_a_base import df_causas_de_morte

# Estou tentando responder a pergunta: Do que as pessoas mais morrem em cada continente?

# Somando todos os valores das colunas
columns_to_sum = df_causas_de_morte.columns[df_causas_de_morte.columns.get_loc("Meningitis") : df_causas_de_morte.columns.get_loc("Continente")]
# Somando todos os anos
somas_por_continente = df_causas_de_morte.groupby("Continente", as_index=False)[columns_to_sum].sum()
# Transformando os dados para long format para melhor trabalhar
novo = pd.melt(somas_por_continente, id_vars="Continente", var_name="Name of the disease", value_name="Number of cases")
# Definindo o nome da doença como Index para melhor entendermos os 3 maiores valores
novo = novo.set_index("Name of the disease")
# Pegando os 3 maiores valores para cada doença em cada continente
top_3_values_per_continent = novo.groupby("Continente")["Number of cases"].nlargest(3)
# Transformando em dataframe
top_3_values_per_continent = top_3_values_per_continent.to_frame()
# Tirando o index como algo de multicategoria
top_3_values_per_continent = top_3_values_per_continent.reset_index()

top_3_africa = ColumnDataSource(top_3_values_per_continent.loc[top_3_values_per_continent["Continente"]=="Africa"])
top_3_asia = ColumnDataSource(top_3_values_per_continent.loc[top_3_values_per_continent["Continente"]=="Asia"])
top_3_europe = ColumnDataSource(top_3_values_per_continent.loc[top_3_values_per_continent["Continente"]=="Europe"])
top_3_north_america = ColumnDataSource(top_3_values_per_continent.loc[top_3_values_per_continent["Continente"]=="North America"])
top_3_south_america = ColumnDataSource(top_3_values_per_continent.loc[top_3_values_per_continent["Continente"]=="South America"])
top_3_oceania = ColumnDataSource(top_3_values_per_continent.loc[top_3_values_per_continent["Continente"]=="Oceania"])

# Fazendo um Grid para mostrar as principais causas de mortes desde 1990 no numdo
grafico_africa = figure(x_range = top_3_africa.data["Name of the disease"])
grafico_asia = figure(x_range = top_3_asia.data["Name of the disease"])
grafico_europe = figure(x_range = top_3_europe.data["Name of the disease"])
grafico_north_america = figure(x_range = top_3_north_america.data["Name of the disease"])
grafico_south_america = figure(x_range = top_3_south_america.data["Name of the disease"])
gráfico_oceania = figure(x_range = top_3_oceania.data["Name of the disease"])


# Definindo os parâmetros para o gráfico da áfrica
grafico_africa.vbar(x = "Name of the disease", top = "Number of cases", width = 0.8 ,source = top_3_africa)

# Colocando em resolução HD
grafico_africa.width = 1280
grafico_africa.height = 720

# Definindo as propiedades do título
grafico_africa.title.text = "Africa"
grafico_africa.title.text_color = "Black"

#mostrando o gráfico
show(grafico_africa)