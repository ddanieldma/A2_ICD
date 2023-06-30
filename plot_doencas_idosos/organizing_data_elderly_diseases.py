from bokeh.models import ColumnDataSource

# importando dataset
# colocando a pasta superior com o módulo que contem o dataframe no path do python
import sys
sys.path.append('../A2_ICD')

from dataframe import df_cause_of_death

# doenças escolhidas
causes = ["Alzheimer's Disease and Other Dementias", "Parkinson's Disease", "Lower Respiratory Infections", "Diabetes Mellitus", "Chronic Respiratory Diseases", "Neoplasms"]

# agrupando pelos anos a lista de doenças
df_deaths_old_people_through_years = df_cause_of_death.groupby("Year")[causes].sum().reset_index()

# tranformando em CDS para ser utilizado pelo bokeh
data_deaths_elderly_through_years = ColumnDataSource(df_deaths_old_people_through_years)