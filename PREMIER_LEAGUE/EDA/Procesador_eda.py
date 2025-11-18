#--------------CLASE DE LIMPIEZA DE DATOS (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ProcesadorEDA:
    def __init__(self, archivo_crudo, archivo_limpio):
        # Inicialización de la clase con los archivos de entrada y salida
        self.__archivo_crudo = archivo_crudo
        self.__archivo_limpio = archivo_limpio
        self.df = pd.read_csv(self.__archivo_crudo)

    def exploracion_inicial(self):
#primeras filas
        print(self.df.head())

#stats básicas
        print(self.df.describe())

#tipo de dato
        print(self.df.info())

#numero de filas y columnas
        print(self.df.shape)

#nulos
        print(self.df.isnull().sum())

    def limpieza(self):
        #Eliminar en "Age" los números innecesarios "-###"
        self.df["Age"] = self.df["Age"].str.split("-").str[0]
        self.df["Age"] = pd.to_numeric(self.df["Age"], errors="coerce")
        print(self.df["Age"].head())

#Columna datetime
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        print(self.df["Date"].head())

    def valores_faltantes(self):
#Exploración de valores faltantes y gráfico correspondiente
    # Gráfico de missing values
        missing_values = self.df.isnull().sum()
        print(missing_values.head())
        sns.barplot(x=missing_values.index, y=missing_values)
        plt.xticks(rotation=90)
        plt.title("Missing Values")
        plt.show()

    def eliminar_columnas(self):
#Eliminar columnas innecesarias
        cols_to_delete = [
            "Dribbles", "Tackles", "Blocks", "Expected Goals (xG)",
            "Non-Penalty xG (npxG)", "Expected Assists (xAG)", "Pass Completion %",
            "Progressive Passes", "Carries", "Progressive Carries", "Dribble Attempts"
        ]
        self.df = self.df.drop(columns=cols_to_delete)
        print(self.df.head())

    def eliminar_duplicados(self):
#Eliminar valores duplicados
        print(f"Duplicados: {self.df.duplicated().sum()}")
        self.df = self.df.drop_duplicates()

    def normalizar_categoricas(self):
#Normalizar las columnas categóricas
        category_col = self.df.select_dtypes(include=object).columns
        print(category_col)

        self.df[category_col] = self.df[category_col].apply(lambda col: col.str.strip().str.lower())
        print(self.df[category_col].head())

    def guardar_dataframe(self):
#Guardar archivo limpio
        self.df.to_csv(self.__archivo_limpio, index=False)
        print(f"Dataframe limpio guardado en: {self.__archivo_limpio}")







