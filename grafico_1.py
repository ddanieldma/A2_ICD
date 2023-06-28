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

# Fazendo um Grid para mostrar as principais causas de mortes desde 1990 no numdo

grafico_africa = figure()
grafico_asia = figure()
grafico_europe = figure()
grafico_north_america = figure()
grafico_south_america = figure()
gráfico_oceania = figure()

# Definindo os parâmetros para o gráfico da áfrica

grafico_africa.width = 1020
grafico_africa.length = 960