#--------------CLASE DE LIMPIEZA DE DATOS (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

#columna datetime
df["Date"]= pd.to_datetime(df["Date"])
print(df["Date"].head())

#Exploracion de valores faltantes
#grafico de missing values
missing_values=df.isnull().sum()
print(missing_values.head())
sns.barplot(x=missing_values.index,y=missing_values)
plt.xticks(rotation=90)
plt.title("Missing Values")
plt.show()

#eliminar columnas del dataset
cols_to_delete = [
    "Dribbles","Tackles","Blocks",
    "Expected Goals (xG)","Non-Penalty xG (npxG)",
    "Expected Assists (xAG)","Pass Completion %",
    "Progressive Passes", "Carries",
    "Progressive Carries","Dribble Attempts"
]

df = df.drop(columns=cols_to_delete)

print(df.head())

#Valores duplicasdos
print("Duplicados:", df.duplicated().sum())
#Normalizar las columnas categoricas
#detectarlas
category_col= df.select_dtypes(include=object).columns
print(category_col)

#Normalizarlas
df[category_col] = df[category_col].apply(lambda col: col.str.strip().str.lower())

print(df[category_col].head())
#Guardar el dataframe limpio
df.to_csv(r"C:\Pycharm\Proyecto Programacion II\Premier_League\DATA\PROCESSED(LIMPIO)\premier_clean.csv",index=False)