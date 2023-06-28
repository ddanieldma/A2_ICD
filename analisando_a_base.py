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
#Fazendo a soma de todas as colunas que tem doenças
df_causas_de_morte["Total Deaths"] = df_causas_de_morte.iloc[:, df_causas_de_morte.columns.get_loc("Meningitis"):df_causas_de_morte.columns.get_loc("Continente")].sum(axis=1)
#Calculando a quantos de mortos a cada 100 mil habitantes
df_causas_de_morte["Deaths per 100k"]= df_causas_de_morte["Total Deaths"]*10**5/df_causas_de_morte["Population"]

# Filtrando os dados para os dados que iremos analisar
df_causas_de_morte_Brasil = df_causas_de_morte[(df_causas_de_morte["Country Code"] == "BRA")].reset_index()

# print(df_causas_de_morte_Brasil)

# Definindo as variáveis
# Gráfico realcionando alzheimer e parkinson
x1 = df_causas_de_morte_Brasil["Alzheimer's Disease and Other Dementias"]
y1 = df_causas_de_morte_Brasil["Parkinson's Disease"]
# Gráfico realacionando o ano com as mortes a cada 100 mil habitantes
x2 = df_causas_de_morte_Brasil["Year"]
y2 = df_causas_de_morte_Brasil["Deaths per 100k"]
# gráfico relacionando o número total de mortes com o ano
x3 = df_causas_de_morte_Brasil["Year"]
y3 = df_causas_de_morte_Brasil["Total Deaths"]

# gráfico para ver em quais doenças o brasil se destaca
# Somando todos os valores das colunas
cols_to_sum = df_causas_de_morte.columns[df_causas_de_morte.columns.get_loc("Meningitis") : df_causas_de_morte.columns.get_loc("Continente")]
# Somando todos os anos
juntando_os_dados = df_causas_de_morte.groupby("Code")[cols_to_sum].sum()

# Fazendo um loop for para pegar apenas as doenças nas quais o Brasil aparece no top 10 com mais casos
paises_com_maiores_casos = {}
for nome in juntando_os_dados.columns:
    paises_maiores_valores = juntando_os_dados[nome].sort_values(ascending=False).head(10)
    if "BRA" in paises_maiores_valores.index:
        paises_com_maiores_casos[nome] = paises_maiores_valores

# for nome, paises in paises_com_maiores_casos.items():
#     print(f"Países com maiores valores em '{nome}':")
#     print(paises)
#     print()

# # criando o gráfico
# grafico_1 = figure()
# grafico_2 = figure()
# grafico_3 = figure()
# gráfico_4 = figure()

# # adicionando o glifo a eles
# grafico_1.circle(x1,y1)
# grafico_2.line(x2,y2)
# grafico_3.line(x3,y3)

# # plotando o grid
# grafico_teste = gridplot([[grafico_1], [grafico_2], [grafico_3]])

# # abrindo o html com o gráfico
# show(grafico_teste)

"""
O gráfico do Brasil possui algo curioso, pois o núemro de mortes a cada 100 mil habitantes caiu de 1990 até 2005 e depois começou a subir novamente.
O que será que aconteceu? Que tipo de mortes levantaram esse índice para cima?

"""
