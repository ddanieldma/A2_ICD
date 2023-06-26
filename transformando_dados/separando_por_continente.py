import pandas as pd
import os
os.chdir("transformando_dados")

# Lendo a nossa base de dados
causas_de_morte = pd.read_csv("cause_of_deaths.csv")

# Colocando o csv com os países e continentes na base de dados
paises_e_continentes = pd.read_csv("Countries-Continents.csv")

# Colocando as duas colunas como um dicionário
dicio_paises_e_cont = dict(zip(paises_e_continentes["Country"], paises_e_continentes["Continent"]))

# Colocando os continentes na base de dados
causas_de_morte["Continente"] = causas_de_morte["Country/Territory"].map(dicio_paises_e_cont)

# Colocando a base num csv
causas_de_morte.to_csv("../new_cause_of_death.csv")









