import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

df = pd.read_csv("../../new_cause_of_death.csv")

df_countries_hiv = df[df['Continente'] == "Africa"].groupby('Country/Territory')['HIV/AIDS'].sum().reset_index()

cds = ColumnDataSource(df_countries_hiv)

fig = figure(x_range=df_countries_hiv['Country/Territory'])

fig.vbar(x='Country/Territory', top='HIV/AIDS', source=cds)

show(fig)