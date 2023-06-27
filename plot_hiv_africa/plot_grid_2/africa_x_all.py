import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

df = pd.read_csv("new_cause_of_death.csv")

df_cont_hiv = df.groupby('Continente')['HIV/AIDS'].sum().reset_index()

cores = ['#8b0000', '#bc634f']

#Obtendo numero de mortes em decorrência do HIV na África
df_cont_hiv.loc[df_cont_hiv['Continente'] == "Africa", 'HIV/AIDS']
#O resultado obtido foi 29106954

#Obtendo numero de mortes em decorrência do HIV no restante do mundo
df_cont_hiv.loc[df_cont_hiv['Continente'] != "Africa", 'HIV/AIDS'].sum()
#O resultado obtido foi 7257465

eixo_x = ['Africa', "Restante do Mundo"]
eixo_y = [29106954, 7257465]

fig = figure(x_range=eixo_x)

fig.vbar(x=eixo_x, top=[29106954, 7257465], width=0.5,
         fill_color=cores,
         line_color = None)

show(fig)