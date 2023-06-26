import pandas as pd
from bokeh.models import ColumnDataSource
#================================================================================================

# lendo dados
df_cause_of_death = pd.read_csv("new_cause_of_death.csv")

# mortes provocadas por homicidios (violencia interpesoal e conflitos/terrorismo) por continentes e por ano
df_homicides_by_continent = df_cause_of_death[["Interpersonal Violence", "Conflict and Terrorism", "Continente"]].groupby(["Continente"]).sum()

# column data source com as colunas que queremos
data_homicides_by_continent = ColumnDataSource(df_homicides_by_continent)

# o bokeh não acessa índices como se fossem colunas em column data source
# por isso, precisamos acessar os índices do dataframe separadamente
# e colocar em uma variável
index_values = df_homicides_by_continent.index.values