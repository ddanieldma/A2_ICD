import pandas as pd
from numpy import log10
from math import pi
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, HoverTool, NumeralTickFormatter
from bokeh.palettes import brewer


# Lendo os dados
df_causas_de_morte = pd.read_csv("new_cause_of_death.csv")
#Fazendo a soma de todas as colunas que tem doenças
df_causas_de_morte["Total Deaths"] = df_causas_de_morte.iloc[:, df_causas_de_morte.columns.get_loc("Meningitis"):df_causas_de_morte.columns.get_loc("Continente")].sum(axis=1)
#Calculando a quantos de mortos a cada 100 mil habitantes
df_causas_de_morte["Deaths per 100k"]= df_causas_de_morte["Total Deaths"]*10**5/df_causas_de_morte["Population"]

# Filtrando os dados para os dados que iremos analisar
df_causas_de_morte_Brasil = df_causas_de_morte[(df_causas_de_morte["Country Code"] == "BRA")].reset_index()

#-----------------------------------------------------------------------------------------------------------------------------------------
#Gráfico 1 - Nested

# Vamos fazer a proporção de cada doença a cada 100000 habitantes
#for colunas in df_causas_de_morte.columns[df_causas_de_morte.columns.get_loc("Meningitis") : df_causas_de_morte.columns.get_loc("Continente")]:
#    df_causas_de_morte[colunas]= df_causas_de_morte[colunas]*10**5/df_causas_de_morte["Population"]

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

# Colocando na ordem para mostrar do maior para o menor
top_3_values_per_continent = top_3_values_per_continent.sort_values("Number of cases", ascending= False)

# Dicionário com cores
diseases = top_3_values_per_continent["Name of the disease"].unique()
color = brewer["Spectral"][7]
dicionario_cores = dict(zip(diseases,color))

# Colocando os dados como uma tupla para realizar um nested bar column
continentes_disease = tuple(zip(top_3_values_per_continent["Continente"], top_3_values_per_continent["Name of the disease"]))

#Colocando os dados como um columndatasource
source_grafico_nested = ColumnDataSource(data=dict(agrupado=continentes_disease, numero_de_casos = top_3_values_per_continent["Number of cases"]))
desgrupando = source_grafico_nested.data["agrupado"]
continente_column, doenca_column = zip(*desgrupando)
source_grafico_nested.data["Continente"]= list(continente_column)
source_grafico_nested.data["Doenca"] = list(doenca_column)

# Adicionando uma coluna com a cor
cor_column = []
for doenca in source_grafico_nested.data["Doenca"]:
    cor = dicionario_cores.get(doenca)
    cor_column.append(cor)
source_grafico_nested.data["Cor"] = cor_column

# Adicionando uma lisa única com os continentes para para ajudar a plotar o gráfico
continentes = []
for continente in continentes_disease:
    if continente not in continentes:
        continentes.append(continente)

#-----------------------------------------------------------------------------------------------------------------------------
# Gráfico 2 - Heatmap
# Colocando o ano como uma string. Isso será importante para o heatmap
df_causas_de_morte_Brasil["Year"]= df_causas_de_morte_Brasil["Year"].astype(str)
# Retirando colunas desnecessárias
df_causas_de_morte_Brasil_heatmap = df_causas_de_morte_Brasil.drop(columns=["index", "Code", "Country/Territory", "Country Code", "Population", "Total Deaths", "Deaths per 100k", "Continente"])
# Colocando o ano como index
df_causas_de_morte_Brasil_heatmap = df_causas_de_morte_Brasil_heatmap.set_index("Year")
# Selecionando apenas as 10 doenças com mais casos
top_10_colunas = df_causas_de_morte_Brasil_heatmap.sum().nlargest(10)
nomes_das_colunas = top_10_colunas.index.to_list()
df_causas_de_morte_Brasil_heatmap = df_causas_de_morte_Brasil_heatmap[nomes_das_colunas]

# Guardando algumas informaçãoes que usaremos mais tarde
years = list(df_causas_de_morte_Brasil_heatmap.index)
diseases = list(reversed(df_causas_de_morte_Brasil_heatmap.columns))

# Criando o dataframe que dará origem ao nosso heatmap
df_heatmap = pd.DataFrame(df_causas_de_morte_Brasil_heatmap.stack(), columns=["casos"])
df_heatmap.reset_index(inplace=True)

# Substituindo o nome da coluna
df_heatmap= df_heatmap.rename(columns={"level_1": "Disease_Name"})

# Colocando o dataframe como um columndatasource
source_heatmap = ColumnDataSource(df_heatmap)

#---------------------------------------------------------------------------------------
# Gráfico 3 - Gridplot

# Criando colunas sobre o percentual de variação
df_causas_de_morte_Brasil["Percentual change in the population"]= df_causas_de_morte_Brasil["Population"].pct_change()
df_causas_de_morte_Brasil["Percentual change in the deaths"] = df_causas_de_morte_Brasil["Total Deaths"].pct_change()
df_causas_de_morte_Brasil["Percental change in the 100k deaths"] = df_causas_de_morte_Brasil["Deaths per 100k"].pct_change()
df_causas_de_morte_Brasil["pct_pop - pct_death"]= df_causas_de_morte_Brasil["Percentual change in the population"]-df_causas_de_morte_Brasil["Percentual change in the deaths"]

# Definindo uma nova variável para não alterar a base de dados original
df_causas_de_morte_Brasil_grid = df_causas_de_morte_Brasil.dropna()
#Adicionando coluna para a cor
def verde_ou_vermelho(x):
    if x > 0:
        return 'green'
    else:
        return 'red'
df_causas_de_morte_Brasil_grid.loc[:, 'Cor'] = df_causas_de_morte_Brasil_grid['pct_pop - pct_death'].apply(verde_ou_vermelho)

# Transformando o nosso datafram em ColumnDataSource
source_grid_Brasil = ColumnDataSource(df_causas_de_morte_Brasil_grid)

#-----------------------------------------------------------------------------------------