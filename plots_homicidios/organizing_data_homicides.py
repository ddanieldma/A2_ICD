import pandas as pd
from bokeh.models import ColumnDataSource
#================================================================================================

# lendo dados
df_cause_of_death = pd.read_csv("new_cause_of_death.csv")

# mortes provocadas por homicidios (violencia interpesoal e conflitos/terrorismo) por continentes e por ano
df_homicides_by_continent = df_cause_of_death.groupby("Continente")[["Interpersonal Violence", "Conflict and Terrorism"]].sum().reset_index()

# dicionario de cores para os continentes
color_dict = {"Africa" : "Yellow", "North America" : "Red", "South America" : "DarkRed", "Europe" : "Black", "Oceania" : "Blue", "Asia" : "Green"}

# colocando a cor para cada continente no dataframe
colors = []
for each_continent in df_homicides_by_continent["Continente"]:
    colors.append(color_dict[each_continent])

df_homicides_by_continent["Color"] = colors
df_homicides_by_continent["Inverted Interpersonal Violence"] = df_homicides_by_continent["Interpersonal Violence"] * -1
df_homicides_by_continent["Inverted Conflict and Terrorism"] = df_homicides_by_continent["Conflict and Terrorism"] * -1

# column data source com as colunas que queremos
data_homicides_by_continent = ColumnDataSource(df_homicides_by_continent)