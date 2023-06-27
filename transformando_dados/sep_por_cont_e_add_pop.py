import pandas as pd
import os
os.chdir("transformando_dados")

"""
O objetivo deste arquivo é adicionar algumas informações que nos ajudarão a realizar com mais facilidade o trabalho,
tal como adicionar uma coluna chamada continente para nos ajudar com alguns plots, e adicionar a população em cada ano.
"""


# Separando a base por continente
# Lendo a nossa base de dados
causas_de_morte = pd.read_csv("cause_of_deaths.csv")

# Colocando o csv com os países e continentes na base de dados
paises_e_continentes = pd.read_csv("Countries-Continents.csv")

# Colocando as duas colunas como um dicionário
dicio_paises_e_cont = dict(zip(paises_e_continentes["Country"], paises_e_continentes["Continent"]))

# Colocando os continentes na base de dados
causas_de_morte["Continente"] = causas_de_morte["Country/Territory"].map(dicio_paises_e_cont)

# Adicionando a população na base
""" 
Esses dados vieram do World Bank Data e se referem a população de cada ano desde 1990 até 2019.
O principal problema é que a população veio de um jeito no qual cada ano é uma coluna, 
mas queremos os anos como uma coluna só, assim, precisaremos ajeitar um pouco nossa base de dados.
"""
# Lendo o csv com a população
populacao = pd.read_csv("population.csv")

# Arrumando o nome das colunas
for titulo in range(4,34):
    ano = populacao.columns[titulo][:4]
    populacao.rename(columns = {populacao.columns[titulo] : ano}, inplace=True)

# Colocando as colunas como linhas com a função pd.melt
populacao = pd.melt(populacao, id_vars=['Country Name', 'Country Code', 'Series Name', 'Series Code'], var_name= "Year", value_name="Value")

# Garantindo que o ano seja tratado como inteiro
populacao["Year"] = populacao["Year"].astype(int)

# Juntando os dataframes populacao e causas_de_morte
causas_de_morte = causas_de_morte.merge(populacao, left_on=['Country/Territory', 'Year'], right_on=['Country Name', 'Year'], how='left')

# Adicionando a coluna População com base na coluna "Value"
causas_de_morte.loc[causas_de_morte['Country Name'].notnull(), 'população'] = causas_de_morte['Value']

# Excluindo colunas desnecessárias
causas_de_morte = causas_de_morte.drop(['Country Name', 'Value'], axis=1)

# Colocando a base num csv
causas_de_morte.to_csv("../new_cause_of_death.csv")









