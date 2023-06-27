import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

df = pd.read_csv("../../new_cause_of_death.csv")

df_africa_hiv = df[df['Continente'] == "Africa"].groupby('Year')['HIV/AIDS'].sum().reset_index()

cds = ColumnDataSource(df_africa_hiv)

fig = figure()

fig.line(x="Year", y="HIV/AIDS", source=cds, line_color = '#8b0000')

show(fig)

output_file("time_line_hiv.html")