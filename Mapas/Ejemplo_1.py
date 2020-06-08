# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: Mapas
# -- archivo: Ej.py
# -- mantiene: violetarcia
# -- repositorio: https://github.com/violetarcia/
# -- ------------------------------------------------------------------------------------ -- #

# Importing and initializing main Python libraries
#import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# reference to the file path
paths = ['datos/conectividad_municipal/ConectividadMunicipal.shx',
		  'datos/colonias/Colonias.shx',
		  'datos/codigos_postales/CP_Jal.shx']

# 0 == municipal | 1 == colonia | 2 == CP
d = 2
file_path = paths[d]
map_us = gpd.read_file(file_path)

# Creating a subplot, with 'fig' and 'ax'
fig, ax = plt.subplots(1, figsize=(15, 8))

# Sending the filtered dat to plot
plt.title('Mapa de Jalisco', size=16)

# Column name according with file
columns = ['NOMBRE', 'COLONIA', 'd_cp']
map_us.plot(column=columns[d],
             cmap='Greens',      # Colormap for the states
             linewidth=0.4,      # line width for state borders
             ax=ax,              # plotting the map on 'ax'
             edgecolor='black'); # State border colors
plt.show()


#datos = map_us[['NOMBRE', 'REGION','Clave', 'Area_km', 'geometry']]