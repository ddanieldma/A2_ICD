import pandas as pd
from numpy import log10
from math import pi
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, HoverTool, NumeralTickFormatter
from bokeh.palettes import brewer, viridis

import warnings
warnings.filterwarnings("ignore")

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
color = viridis(7)
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
continentes_unicos = []
for continente in continentes_disease:
    if continente not in continentes_unicos:
        continentes_unicos.append(continente)

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

#-----------------------------------------------------------------------------------------------------------------------
# Gráficos Daniel

#================================================================================================
# Primeiro gráfico
# Grid plot sobre mortes por violência interperssoal e conflitos e terrorismo
# para todos os 30 anos, por continente, primeiro em números absolutos e depois
# em relação à população do continente

# mortes provocadas por homicidios (violencia interpesoal e conflitos/terrorismo) por continentes e por ano
df_homicides_by_continent = df_causas_de_morte.groupby("Continente")[["Interpersonal Violence", "Conflict and Terrorism"]].sum().reset_index()

# colocando colunas com valores negativos para que o gráfico seja plotado de cima para baixo
df_homicides_by_continent["Inverted Interpersonal Violence"] = df_homicides_by_continent["Interpersonal Violence"] * -1
df_homicides_by_continent["Inverted Conflict and Terrorism"] = df_homicides_by_continent["Conflict and Terrorism"] * -1

# column data source com as colunas que queremos
data_homicides_by_continent = ColumnDataSource(df_homicides_by_continent)

#=================================================
# mesmos dados mas agora com o número de mortes em relação à população do respectivo continente

df_homicides_by_continent_proportion = df_causas_de_morte.groupby("Continente")[["Interpersonal Violence", "Conflict and Terrorism", "Population"]].sum().sort_values(by = "Population").reset_index()

df_homicides_by_continent_proportion["Proportion Violence"] = (df_homicides_by_continent_proportion["Interpersonal Violence"] / df_homicides_by_continent_proportion["Population"])
df_homicides_by_continent_proportion["Proportion Conflict"] = (df_homicides_by_continent_proportion["Conflict and Terrorism"] / df_homicides_by_continent_proportion["Population"])

# colocando novamente valores negativos
df_homicides_by_continent_proportion["Inverted Violence Proportion"] = df_homicides_by_continent_proportion["Proportion Violence"] * -1
df_homicides_by_continent_proportion["Inverted Conflict Proportion"] = df_homicides_by_continent_proportion["Proportion Conflict"] * -1

# criando column data source
source_homicides_by_continent_proportion = ColumnDataSource(df_homicides_by_continent_proportion)

#================================================================================================
# Segundo gráfico
# Gráfico sobre as mortes ao longo do tempo pelas causas que afetam majoritariamente
# pessoas idosas para todo o mundo

# doenças escolhidas
causes = ["Alzheimer's Disease and Other Dementias", "Parkinson's Disease", "Lower Respiratory Infections", "Diabetes Mellitus", "Chronic Respiratory Diseases", "Neoplasms"]

# agrupando pelos anos a lista de doenças
df_deaths_old_people_through_years = df_causas_de_morte.groupby("Year")[causes].sum().reset_index()

# tranformando em CDS para ser utilizado pelo bokeh
source_deaths_elderly_through_years = ColumnDataSource(df_deaths_old_people_through_years)

#================================================================================================
# Terceiro gráfico
# Gráfico sobre a distribuição de mortes por acidente cardiovascular por 100 mil habitantes
# para todo o mundo no ano de 2019

# separando mortes por acidentes cardiovasculares por país no ano de 2019
df_countries_cardio_2019 = df_causas_de_morte[df_causas_de_morte["Year"] == 2019].groupby(['Country/Territory', 'Continente', "Population"]).agg({'Cardiovascular Diseases': 'sum'}).reset_index()

# colocando numeros de mortes por 100 mil habitantes
df_countries_cardio_2019["Per 100k"] = df_countries_cardio_2019["Cardiovascular Diseases"] / df_countries_cardio_2019["Population"] * 100000

# Transformando a coluna continente para kind para facilitar fazer o boxplot
df_continents_boxplot = df_countries_cardio_2019.rename(columns = {"Continente" : "kind"})

# pegando os continentes únicos
kinds = df_continents_boxplot.kind.unique()

# calculando quartis por continente e colocando no dataframe o quartil
# correspondente a cada continente
qs = df_continents_boxplot.groupby("kind")["Per 100k"].quantile([0.25, 0.5, 0.75])
qs = qs.unstack().reset_index()
qs.columns = ["kind", "q1", "q2", "q3"]
df_continents_boxplot = pd.merge(df_continents_boxplot, qs, on="kind", how="left")

# calculando distancia interquartil
iqr = df_continents_boxplot.q3 - df_continents_boxplot.q1
# setando limitantes superior e inferior
df_continents_boxplot["upper"] = df_continents_boxplot.q3 + 1.5*iqr
df_continents_boxplot["lower"] = df_continents_boxplot.q1 - 1.5*iqr

# criando column data source
source_continents_boxplot = ColumnDataSource(df_continents_boxplot)

# filtrando outliers selecionando todos os valores no dataframe que caem fora do range 
# estabelecido por df_boxplot.lower e df_boxplot.upper
outliers_continents_boxplot = df_continents_boxplot[~df_continents_boxplot["Per 100k"].between(df_continents_boxplot.lower, df_continents_boxplot.upper)]

#=========================================================================================================================

# Parte Guilherme
df_guilherme = df_causas_de_morte.copy()

#GRÁFICO MORTES POR DOENÇAS

#Criando uma nova coluna que representa a soma dos valores numéricos das colunas especificadas
df_guilherme['Soma_doenças'] = df_guilherme[["Meningitis","Alzheimer's Disease and Other Dementias", "Parkinson's Disease", 
"Cardiovascular Diseases","Lower Respiratory Infections", "Acute Hepatitis", "Digestive Diseases", "Cirrhosis and Other Chronic Liver Diseases", 
"Chronic Respiratory Diseases", "Diabetes Mellitus","Chronic Kidney Disease", "Nutritional Deficiencies", "Malaria", "Maternal Disorders", 
"HIV/AIDS","Drug Use Disorders","Tuberculosis","Neonatal Disorders","Alcohol Use Disorders","Diarrheal Diseases"]].sum(axis=1)

#Filtrando por ano (+ soma de todos os valores da coluna ['Soma_doenças'] desse ano)
df_diseases = df_guilherme.groupby('Year')['Soma_doenças'].sum().reset_index()

#Criação do ColumnDataSource
cds_diseases = ColumnDataSource(df_diseases)

#GRÁFICO MORTES NÃO RELACIONADAS A DOENÇAS

#Criando uma nova coluna que representa a soma dos valores numéricos das colunas especificadas
df_guilherme['Soma_não_doenças'] = df_guilherme[["Drowning", "Interpersonal Violence", "Fire, Heat, and Hot Substances", "Road Injuries", "Poisonings" ,
"Protein-Energy Malnutrition", "Conflict and Terrorism", "Self-harm", "Exposure to Forces of Nature", 
"Environmental Heat and Cold Exposure"]].sum(axis=1)

#Filtrando por ano (+ soma de todos os valores da coluna ['Soma'] desse ano)
df_non_diseases = df_guilherme.groupby('Year')['Soma_não_doenças'].sum().reset_index()

#Criação do ColumnDataSource
cds_non_diseases = ColumnDataSource(df_non_diseases)

#GRÁFICO AFOGAMENTO

#Filtragem por ano com a soma dos valores da coluna ['Drowning']
df_drowning_sum = df_guilherme.groupby('Year')['Drowning'].sum().reset_index()

#Criação do ColumnDataSource
cds_afogamento = ColumnDataSource(df_drowning_sum)


#GRÁFICOS DO GRID

#GRÁFICO COMPARAÇÃO CONTINENTES

#Filtragem por continente + soma dos registros de mortes por HIV/AIDS de cada um
df_cont_hiv = df_guilherme.groupby('Continente')['HIV/AIDS'].sum().reset_index()

#Obtenção dos 5 continentes (para aplicar a paleta)
continentes = df_cont_hiv['Continente'].unique()

#Criação da paleta
cores_continentes = ['#8b0000', '#bc634f', '#bc634f', '#bc634f', '#bc634f', '#bc634f']
    
#Criação do ColumnDataSource
cds_comp_continentes = ColumnDataSource(df_cont_hiv)


#GRAFICO AFRICA X SOMA DOS OUTROS

#Determinação das cores a serem utilizadas no plot
cores_af_x_all = ['#8b0000', '#bc634f']

#Obtendo numero de mortes em decorrência do HIV na África
mortes_africa = df_cont_hiv.loc[df_cont_hiv['Continente'] == "Africa", 'HIV/AIDS']
   
#Obtendo numero de mortes em decorrência do HIV no restante do mundo
mortes_resto_mundo = df_cont_hiv.loc[df_cont_hiv['Continente'] != "Africa", 'HIV/AIDS'].sum()

#Criação dos eixos do plot (o eixo y são os valores obtidos acima)
eixo_x_afxall = ['Africa', "Restante do Mundo"]
eixo_y_afxall = [mortes_africa, mortes_resto_mundo]

cds_af_x_all = ColumnDataSource(data=dict(x=eixo_x_afxall, y=eixo_y_afxall))


#GRÁFICO TOP 10 PAÍSES

#Criação de uma nova coluna que representa a quantidade de mortes em decorrência de HIV/AIDS a cada 100k habitantes em cada país
df_guilherme["per_100k_hab"] = df_guilherme["HIV/AIDS"]/df_guilherme["Population"]*100000

#Filtragem países africanos + soma das mortes a cada 100000 habitantes por ano + valores em ordem decrescente + top 10 valores
df_countries_hiv = df_guilherme[df_guilherme['Continente'] == "Africa"].groupby('Country/Territory')['per_100k_hab'].sum().sort_values(ascending=False).head(10).reset_index()
#O objetivo é obter os 10 países com o maior histórico de mortes a cada 100000 habitantes da áfrica (em decorrência de HIV)

#Criação do ColumnDataSource
cds_top_10 = ColumnDataSource(df_countries_hiv)

#GRÁFICO LINHA DO TEMPO HIV ÁFRICA

#Filtragem apenas por países africanos + soma das mortes por HIV/AIDS em cada ano
df_africa_hiv_timeline = df_guilherme[df_guilherme['Continente'] == "Africa"].groupby('Year')['HIV/AIDS'].sum().reset_index()

#Criação do ColumnDataSource
cds_timeline = ColumnDataSource(df_africa_hiv_timeline)