import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource 

# Criando o arquivo de saída
output_file("visualizacao.html")

# Lendo os dados
df_causas_de_morte = pd.read_csv("new_cause_of_death.csv")

# Filtrando os dados para os dados que iremos analisar
df_causas_de_morte_Brasil = df_causas_de_morte[(df_causas_de_morte["Country Code"] == "BRA")]

# Definindo as variáveis
x = df_causas_de_morte_Brasil["Year"]
y = df_causas_de_morte_Brasil["população"]

# criando o gráfico
grafico_teste = figure()

# adicionando o glifo a ele
grafico_teste.line(x,y)

# abrindo o html com o gráfico
show(grafico_teste)



# x = df_causas_de_morte["Meningitis"]
# y = df_causas_de_morte["Year"]


# print(df_causas_de_morte.columns)




