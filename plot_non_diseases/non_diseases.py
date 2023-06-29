import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

df = pd.read_csv("../new_cause_of_death.csv")

df['Soma'] = df[["Drowning", "Interpersonal Violence", "Fire, Heat, and Hot Substances", "Road Injuries", "Poisonings" ,
"Protein-Energy Malnutrition", "Conflict and Terrorism", "Self-harm", "Exposure to Forces of Nature", 
"Environmental Heat and Cold Exposure"]].sum(axis=1)

df_non_diseases = df.groupby('Year')['Soma'].sum().reset_index()

cds = ColumnDataSource(df_non_diseases)

fig = figure(width = 1280, height = 720)

fig.line(x="Year", y="Soma", source=cds, line_color = '#399e1f')

fig.title.text = "Total de Mortes por Lesões (histórico)"
fig.title.text_color = "#4f7227"
fig.title.text_font = "Times"
fig.title.text_font_size = "26px"
fig.title.align = "center"

fig.xaxis.axis_label = "Ano"
fig.xaxis.major_label_text_font_size = "16px"

fig.yaxis.axis_label = "Número de Mortes"
fig.yaxis.major_label_text_font_size = "16px"


fig.axis.axis_label_text_color = '#4f7227'

fig.axis.axis_label_text_font_size = "24px"


#4f7227

show(fig)

print(df_non_diseases.columns)