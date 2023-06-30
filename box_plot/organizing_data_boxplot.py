import pandas as pd

from bokeh.models import ColumnDataSource

# lendo dataset
df_cause_of_death = pd.read_csv("new_cause_of_death.csv")

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
outliers = df_continents_boxplot[~df_continents_boxplot["Per 100k"].between(df_continents_boxplot.lower, df_continents_boxplot.upper)]