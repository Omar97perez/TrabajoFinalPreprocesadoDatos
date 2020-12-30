import matplotlib.pyplot as plt
import pandas as pd
import StrategyFile as sf
import sys
import string
import os
import geopandas as gpd
import numpy as np
from time import time

def GetResult(value):
    if value == 'G':
        return "0"
    elif value == 'E':
        return "1"
    elif value == 'P':
        return "2"

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

array = df.values
fila = ""
final = ""

for row in array:
    if row[2] == 1:
        match = 1
        fila += row[3] + "," + row[1]
        for all in array:
            if all[3] == row[3] and all[1] == row[1] and match <= 30: 
                fila += "," + GetResult(all[7])
                match += 1
            elif all[4] == row[3] and all[1] == row[1] and match <= 30:
                fila += "," + GetResult(all[8])
                match += 1
        final += fila + "\n"
        fila = ""
        match = 1
        fila += row[4] + "," + row[1]
        for all in array:
            if all[3] == row[4] and all[1] == row[1] and match <= 30:
                fila += "," + GetResult(all[7])
                match += 1
            elif all[4] == row[4] and all[1] == row[1] and match <= 30 :
                fila += "," + GetResult(all[8])
                match += 1
        final += fila + "\n"
        fila = ""

file = open( "./DatosTratados/" + "Resultados" + ".csv", "w")
file.write(final)