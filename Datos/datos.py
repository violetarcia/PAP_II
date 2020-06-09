# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: Mapas
# -- archivo: Ej.py
# -- mantiene: violetarcia
# -- repositorio: https://github.com/violetarcia/
# -- ------------------------------------------------------------------------------------ -- #

# Importing and initializing main Python libraries
import pandas as pd
import entradas as ent

# -- ------------------------------------------------------------------------------------ -- #
# -- Leer archivo de datos del indice y guardalo en un DataFrame
# -- ------------------------------------------------------------------------------------ -- #
def f_leer_archivo(file_path, sheet):
    """
    Parameters
    ---------
    :param: 
        file: str : nombre de archivo leer

    Returns
    ---------
    :return: 
        df_data DataFrame : Datos del archivo

    Debuggin
    ---------
        file_path = 'Base_de_datos.xlsx'
		sheet = 'IIEG_E_1'

    """
    # Leer archivo xls
    df_data = pd.read_excel('archivos/' + file_path, sheet_name=sheet)
    return df_data

df = f_leer_archivo(ent.path, 'IIEG_E_1')

#%%
temp = list(df.groupby(['CP']))

print(int(temp[0][0]))