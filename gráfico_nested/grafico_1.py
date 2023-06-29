import sys
sys.path.append('../A2_ICD')
from analisando_a_base import df_causas_de_morte
import pandas as pd
from numpy import log10
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange

# Estou tentando responder a pergunta: Do que as pessoas mais morrem em cada continente?

# Somando todos os valores das colunas
columns_to_sum = df_causas_de_morte.columns[df_causas_de_morte.columns.get_loc("Meningitis") : df_causas_de_morte.columns.get_loc("Continente")]
# Somando todos os anos
somas_por_continente = df_causas_de_morte.groupby("Continente", as_index=False)[columns_to_sum].sum()
# Transformando os dados para long format para melhor trabalhar
tabela_long_format = pd.melt(somas_por_continente, id_vars="Continente", var_name="Name of the disease", value_name="Number of cases")
# Definindo o nome da doença como Index para melhor entendermos os 3 maiores valores
tabela_long_format = tabela_long_format.set_index("Name of the disease")
# Pegando os 3 maiores valores para cada doença em cada continente
top_3_values_per_continent = tabela_long_format.groupby("Continente")["Number of cases"].nlargest(3)
# Transformando em dataframe
top_3_values_per_continent = top_3_values_per_continent.to_frame()
# Tirando o index como algo de multicategoria
top_3_values_per_continent = top_3_values_per_continent.reset_index()

top_3_values_per_continent = top_3_values_per_continent.sort_values("Number of cases", ascending= False)
# # Tranformando em escala logarítimica
# top_3_values_per_continent["Number of cases"] = log10(top_3_values_per_continent["Number of cases"])

# Colocando os dados como uma tupla para realizar um nested bar column
continentes_disease = tuple(zip(top_3_values_per_continent["Continente"], top_3_values_per_continent["Name of the disease"]))

#Colocando os dados como um columndatasource
source = ColumnDataSource(data=dict(agrupado=continentes_disease, numero_de_casos = top_3_values_per_continent["Number of cases"]))
continentes = []
for continente in continentes_disease:
    if continente not in continentes:
        continentes.append(continente)


grafico_juntos = figure(x_range = FactorRange(*continentes))
grafico_juntos.vbar(x = "agrupado" , top = "numero_de_casos", width = 0.8, source=source)

grafico_juntos.width = 1500
grafico_juntos.height = 720
grafico_juntos.xaxis.major_label_orientation = 1

# #mostrando o gráfico
show(grafico_juntos)