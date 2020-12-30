import matplotlib.pyplot as plt
import pandas as pd
import StrategyFile as sf
import sys
import string
import os
import geopandas as gpd
import numpy as np
from time import time

#Cargamos los datos de un fichero
file = sys.argv[1]
fichero = os.path.splitext(file)
nombreFichero = fichero[0]
fichero = fichero[0] + ".csv"

if file.endswith('.csv'):
    fileSelected = sf.Csv(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.json'):
    fileSelected= sf.Json(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.xlsx'):
    fileSelected= sf.Xlsx(file, fichero)
    df = fileSelected.collect()
else:
    print("Formato no soportado")
    sys.exit()

resultados = df.values

#Cargamos los datos de un fichero
file = sys.argv[2]
fichero = os.path.splitext(file)
nombreFichero = fichero[0]
fichero = fichero[0] + ".csv"

if file.endswith('.csv'):
    fileSelected = sf.Csv(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.json'):
    fileSelected= sf.Json(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.xlsx'):
    fileSelected= sf.Xlsx(file, fichero)
    df = fileSelected.collect()
else:
    print("Formato no soportado")
    sys.exit()

clasificacion = df.values
final = ""
fila = ""

for result in resultados:
    for clasific in clasificacion:
        if result[0] == clasific[1] and result[1] == clasific[7]:
            for rlt in result:
                fila += str(rlt) + ","
            final += fila +  str(clasific[0]) + "\n"
            fila = ""

file = open( "./" + "final" + ".csv", "w")
file.write(final)