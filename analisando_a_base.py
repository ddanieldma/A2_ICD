import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.models import ColumnDataSource 

output_file("visualização.html")

df_causas_de_morte = pd.read_csv("new_cause_of_death.csv")

print(df_causas_de_morte)

