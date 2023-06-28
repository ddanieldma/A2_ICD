import sys
sys.path.append('../A2_ICD')
from analisando_a_base import df_causas_de_morte_Brasil
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, BasicTicker, PrintfTickFormatter
from bokeh.transform import linear_cmap
from math import pi

# Para fazer o heatmap, vamos precisar manipular um pouco nosso dataset
# Retirando colunas desnecessárias
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil.drop(columns=["index", "Code", "Country/Territory", "Country Code", "Population", "Total Deaths", "Deaths per 100k", "Continente"])
# Colocando o ano como uma string. Isso será importante para o heatmap
df_causas_de_morte_Brasil["Year"]= df_causas_de_morte_Brasil["Year"].astype(str)
# Colocando o ano como index
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil.set_index("Year")

# Guardando algumas informaçãoes que usaremos mais tarde
years = list(df_causas_de_morte_Brasil.index)
diseases = list(reversed(df_causas_de_morte_Brasil.columns))

# Criando o dataframe que dará origem ao nosso heatmap
df_heatmap = pd.DataFrame(df_causas_de_morte_Brasil.stack(), columns=["casos"])
df_heatmap.reset_index(inplace=True)

# Substituindo o nome da coluna
df_heatmap= df_heatmap.rename(columns={"level_1": "Disease Name"})

# Colocando o dataframe como um columndatasource
source = ColumnDataSource(df_heatmap)

print(df_heatmap)

