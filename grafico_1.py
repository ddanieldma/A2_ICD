import pandas as pd
import math
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource 
from analisando_a_base import df_causas_de_morte

# Estou tentando responder a pergunta: Do que as pessoas mais morrem em cada continente?

# Somando todos os valores das colunas
columns_to_sum = df_causas_de_morte.columns[df_causas_de_morte.columns.get_loc("Meningitis") : df_causas_de_morte.columns.get_loc("Continente")]
# Somando todos os anos
somas_por_continente = df_causas_de_morte.groupby("Continente", as_index=False)[columns_to_sum].sum()
# Transformando os dados para long format para melhor trabalhar
novo = pd.melt(somas_por_continente, id_vars="Continente", var_name="Name of the disease", value_name="Number of cases")
# Definindo o nome da doença como Index para melhor entendermos os 3 maiores valores
novo = novo.set_index("Name of the disease")
# Pegando os 3 maiores valores para cada doença em cada continente
top_3_values_per_continent = novo.groupby("Continente")["Number of cases"].nlargest(3)
# Transformando em dataframe
top_3_values_per_continent = top_3_values_per_continent.to_frame()
# Tirando o index como algo de multicategoria
top_3_values_per_continent = top_3_values_per_continent.reset_index()


# Fazendo um gráfico anular
# Vamos separar algumas variáveis que iremos utilizar
Diseases = top_3_values_per_continent["Name of the disease"].unique()
# As cores que iremos utilizar para o gráfico
Colors = ["#f94144", "#f3722c", "#f8961e", "#f9c74f", "#90be6d", "#43aa8b", "#577590"]
# As cores que utilizaremos para mapear os continentes
Continents = {"Africa" : "Yellow", "North America" : "Red", "South America" : "DarkRed", "Europe" : "Black", "Oceania" : "Blue", "Asia" : "Green"}

# Para fazer um gráfico anular, precisaremos dos angulos de cada uma das fatias
# para isso, vamos adicionar esses angulos como propriedades do dataframe
big_angle = 2 * np.pi / 7
angles = np.pi/2 - 3 * big_angle/2 - np.vectorize(math.floor)((np.array(top_3_values_per_continent.index))/3) * big_angle
top_3_values_per_continent["start"] = angles
top_3_values_per_continent["end"] = angles + big_angle
top_3_values_per_continent["Colors"]= top_3_values_per_continent["Continente"].map(Continents)
# Vamos definir a escala do nosso gráfico anular
micmin = np.sqrt(np.log(.001*1E4))
micmax = np.sqrt(np.log(1000*1E4))
def scale(mic):
    return - np.sqrt(np.log(mic * 1E4)) + (micmin + micmax)
# Definindo o nosso dataframe como ColumnDataSource
source = ColumnDataSource(top_3_values_per_continent)

# Plotando nosso gráfico
grafico_1 = figure(
    width=800, height=800, title=None, tools="", toolbar_location=None,
    x_axis_type=None, y_axis_type=None, match_aspect=True,
    min_border=0, outline_line_color="black", background_fill_color="#f0e1d2",
)

glifo = grafico_1.annular_wedge(x=0, y=0, inner_radius=micmax, outer_radius= micmin, start_angle="start", end_angle = "end", fill_color="Colors", line_color="#f0e1d2", source=source)


radii = scale(10.0 ** np.arange(-3, 4))
grafico_1.circle(0, 0, radius=radii, fill_color=None, line_color="#f0e1d2")
grafico_1.text(0, radii, ["0.001", "0.01", "0.1", "1", "10", "100", "1000"],
    text_font_size="12px", anchor="center")




print(top_3_values_per_continent)
show(grafico_1)
