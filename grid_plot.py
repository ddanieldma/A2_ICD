from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from plot_hiv_africa import plot_1
from africa_x_all import plot_2
from linha_do_tempo_africa import plot_3
from per_country import plot_4

#Após importar as função, atribuímos uma variável a cada
plot_1 = plot_1()
plot_2 = plot_2()
plot_3 = plot_3()
plot_4 = plot_4()

#criação do grid plot (são utilizadas duas listas para que o grid fique 2x2)
grid_hiv_africa = gridplot([[plot_1, plot_2], [plot_3, plot_4]])

grid_hiv_africa.toolbar.autohide = True
grid_hiv_africa.toolbar.logo = None

output_file("grid_plot.html")

save(grid_hiv_africa)
show(grid_hiv_africa)