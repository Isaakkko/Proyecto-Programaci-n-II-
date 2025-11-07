#--------------CLASE DE LIMPIEZA DE DATOS (EDA)

import pandas as pd
import numpy as np

#carga del csv
df = pd.read_csv(r"C:\Pycharm\Proyecto Programacion II\Premier_League\DATA\RAW(CRUDO)\premier.csv")

#----Exploracion Inicial

#Primeras filas
print(df.head())
#stats Basicas
print(df.describe())
#tipo de dato
print(df.info())
#numero de filas y columnas
print(df.shape)
#Ver nulos
print(df.isnull().sum())

#----Limpieza

#Eliminar en "Age" los numeros innecesarios "-###"
df["Age"]= df["Age"].str.split("-").str[0]
df["Age"]= pd.to_numeric(df["Age"], errors="coerce")

print(df["Age"].head())