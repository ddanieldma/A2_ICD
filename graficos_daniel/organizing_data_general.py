import pandas as pd

from bokeh.models import ColumnDataSource

# lendo base de dados
df_cause_of_death = pd.read_csv("new_cause_of_death.csv")

#================================================================================================
# Primeiro gráfico
# Grid plot sobre mortes por violência interperssoal e conflitos e terrorismo
# para todos os 30 anos, por continente, primeiro em números absolutos e depois
# em relação à população do continente

# mortes provocadas por homicidios (violencia interpesoal e conflitos/terrorismo) por continentes e por ano
df_homicides_by_continent = df_cause_of_death.groupby("Continente")[["Interpersonal Violence", "Conflict and Terrorism"]].sum().reset_index()

# colocando colunas com valores negativos para que o gráfico seja plotado de cima para baixo
df_homicides_by_continent["Inverted Interpersonal Violence"] = df_homicides_by_continent["Interpersonal Violence"] * -1
df_homicides_by_continent["Inverted Conflict and Terrorism"] = df_homicides_by_continent["Conflict and Terrorism"] * -1

# column data source com as colunas que queremos
data_homicides_by_continent = ColumnDataSource(df_homicides_by_continent)

#=================================================
# mesmos dados mas agora com o número de mortes em relação à população do respectivo continente

df_homicides_by_continent_proportion = df_cause_of_death.groupby("Continente")[["Interpersonal Violence", "Conflict and Terrorism", "Population"]].sum().sort_values(by = "Population").reset_index()

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
df_deaths_old_people_through_years = df_cause_of_death.groupby("Year")[causes].sum().reset_index()

# tranformando em CDS para ser utilizado pelo bokeh
source_deaths_elderly_through_years = ColumnDataSource(df_deaths_old_people_through_years)

#================================================================================================
# Terceiro gráfico
# Gráfico sobre a distribuição de mortes por acidente cardiovascular por 100 mil habitantes
# para todo o mundo no ano de 2019

# separando mortes por acidentes cardiovasculares por país no ano de 2019
df_countries_cardio_2019 = df_cause_of_death[df_cause_of_death["Year"] == 2019].groupby(['Country/Territory', 'Continente', "Population"]).agg({'Cardiovascular Diseases': 'sum'}).reset_index()

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