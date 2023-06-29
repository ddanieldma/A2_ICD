import sys
sys.path.append('../A2_ICD')
from analisando_a_base import df_causas_de_morte_Brasil
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource, FactorRange, BasicTicker, PrintfTickFormatter, HoverTool
from bokeh.transform import linear_cmap
from math import pi

# Para fazer o heatmap, vamos precisar manipular um pouco nosso dataset
# Retirando colunas desnecessárias
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil.drop(columns=["index", "Code", "Country/Territory", "Country Code", "Population", "Total Deaths", "Deaths per 100k", "Continente"])
# Colocando o ano como uma string. Isso será importante para o heatmap
df_causas_de_morte_Brasil["Year"]= df_causas_de_morte_Brasil["Year"].astype(str)
# Colocando o ano como index
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil.set_index("Year")
# Selecionando apenas as 10 doenças com mais casos
top_10_colunas = df_causas_de_morte_Brasil.sum().nlargest(10)
nomes_das_colunas = top_10_colunas.index.to_list()
df_causas_de_morte_Brasil = df_causas_de_morte_Brasil[nomes_das_colunas]

# Guardando algumas informaçãoes que usaremos mais tarde
years = list(df_causas_de_morte_Brasil.index)
diseases = list(reversed(df_causas_de_morte_Brasil.columns))

# Criando o dataframe que dará origem ao nosso heatmap
df_heatmap = pd.DataFrame(df_causas_de_morte_Brasil.stack(), columns=["casos"])
df_heatmap.reset_index(inplace=True)

# Substituindo o nome da coluna
df_heatmap= df_heatmap.rename(columns={"level_1": "Disease_Name"})

# Colocando o dataframe como um columndatasource
source = ColumnDataSource(df_heatmap)

# Definindo as cores do heatmap
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
# Definindo as tools que usaremos
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

# Criando nossa figure
heatmap =  figure(x_range = years, y_range  = diseases, tools = TOOLS)

# Definindo as Propiedadades do título
heatmap.title = f"Top 10 doenças que mais mataram no Brasil({years[0]}-{years[-1]})"

# definindo interatividade 
interativo = HoverTool(tooltips=[("Ano", "@Year"), ("Doença", "@Disease_Name"), ("Número de casos", "@casos")])
heatmap.add_tools(interativo)

# Definindo o tamanho do heatmap
heatmap.width = 900
heatmap.height = 400

# adicionando propriedades no grid
heatmap.grid.grid_line_color = None

# Adicionando propriedades aos eixos
heatmap.axis.axis_line_color = None
heatmap.axis.major_tick_line_color = None
heatmap.axis.major_label_text_font_size = "10px"
heatmap.axis.major_label_standoff = 0
heatmap.xaxis.major_label_orientation = pi / 3

# Adicionando uma escala de cores que será posteriormente usada para o heatmap
color_chart = linear_cmap("casos", colors, low = df_heatmap.casos.min(), high=df_heatmap.casos.max())

# Adicionando os retângulos do heatmap
tiles = heatmap.rect(x = "Year", y = "Disease_Name",  width = 1, height=1, fill_color = color_chart, line_color = None ,source = source)

# Adicionando um grid com barra de cores
heatmap.add_layout(tiles.construct_color_bar(
    major_label_text_font_size="12px",
    ticker=BasicTicker(desired_num_ticks=len(colors)),
    formatter=PrintfTickFormatter(format="%0.1e"),
    label_standoff=7,
    border_line_color=None,
    padding=5,
), 'right')
show (heatmap)