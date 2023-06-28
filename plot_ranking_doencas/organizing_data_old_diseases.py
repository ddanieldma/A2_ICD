from dataframe import df_cause_of_death

import pandas as pd

from bokeh.models import ColumnDataSource

# doenças escolhidas
causes = ["Alzheimer's Disease and Other Dementias", "Parkinson's Disease", "Lower Respiratory Infections", "Diabetes Mellitus", "Chronic Respiratory Diseases", "Neoplasms"]

# agrupando pelos anos a lista de doenças
df_deaths_old_people_through_years = df_cause_of_death.groupby("Year")[causes].sum().reset_index()

# tranformando em CDS para ser utilizado pelo bokeh
data_deaths_old_people_through_years = ColumnDataSource(df_deaths_old_people_through_years)