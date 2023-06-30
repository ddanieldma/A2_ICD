import pandas as pd
from bokeh.models import ColumnDataSource

df = pd.read_csv("new_cause_of_death.csv")

df_guilherme = df.copy()

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