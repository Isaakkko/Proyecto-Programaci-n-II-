import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizador:

    def __init__(self, df):
        self.df = df5

    
    # 1. Barras: goles totales por equipo
    
    def goles_totales_por_equipo(self):
        goles = self.df.groupby("Team")["Goals"].sum().sort_values(ascending=False)
        plt.figure(figsize=(10,5))
        plt.bar(goles.index, goles.values, color="orange", edgecolor="black")
        plt.xticks(rotation=90)
        plt.title("Goles Totales por Equipo")
        plt.xlabel("Equipo")
        plt.ylabel("Goles")
        plt.tight_layout()
        plt.show()

    
    # 2. Grafico lineal de goleadores y minutos jugados
    
    def linea_goleadores_minutos(self):
        df = self.df.copy()

        top = df.groupby("Player")[["Goals", "Minutes"]].sum().sort_values(
            "Goals", ascending=False
        ).head(10)

        fig, ax1 = plt.subplots(figsize=(12,5))

        # Línea de GOLES
        ax1.plot(top.index, top["Goals"], marker="o", linewidth=2, color="orange", label="Goles")
        ax1.set_ylabel("Goles", color="orange")
        ax1.tick_params(axis="y", labelcolor="orange")

        # Segundo eje Y (Minutos)
        ax2 = ax1.twinx()
        ax2.plot(top.index, top["Minutes"], marker="o", linewidth=2, color="blue", label="Minutos")
        ax2.set_ylabel("Minutos", color="blue")
        ax2.tick_params(axis="y", labelcolor="blue")

        # Configuración
        plt.title("Top Goleadores: Goles vs Minutos Jugados")
        ax1.set_xlabel("Jugador")
        plt.xticks(rotation=45)
        ax1.grid(True, linestyle="--", alpha=0.4)

        fig.tight_layout()
        plt.show()

    
    

    
    # 4. Histograma con edades 
    
    def histograma_edades_seleccionadas(self):
        edades_filtro = [20, 22, 24, 28, 30]
        df = self.df[self.df["Age"].isin(edades_filtro)]

        plt.figure(figsize=(8,5))
        plt.hist(df["Age"], bins=len(edades_filtro), color="skyblue", edgecolor="black")
        plt.title("Distribución de Edades Seleccionadas")
        plt.xlabel("Edad")
        plt.ylabel("Frecuencia")
        plt.xticks(edades_filtro)
        plt.tight_layout()
        plt.show()

    
    # 5. Circular: distribución de posiciones
    
    def grafico_circular(self, titulo="Distribución de posiciones principales"):
        df = self.df.copy()
        df["MainPosition"] = df["Position"].astype(str).apply(lambda x: x.split(",")[0])

        traductor_posiciones = {
            "gk": "Portero",
            "cb": "Defensa central",
            "wb": "Carrilero",
            "dm": "Mediocampista defensivo",
            "cm": "Mediocampista central",
            "lm": "Mediocampista izquierdo",
            "rm": "Mediocampista derecho",
            "lw": "Extremo izquierdo",
            "rw": "Extremo derecho",
            "fw": "Delantero",
        }
        df["MainPosition"] = df["MainPosition"].map(traductor_posiciones).fillna("Otros")

        counts = df["MainPosition"].value_counts()

        plt.figure(figsize=(8,8))
        counts.plot(kind="pie", autopct="%1.1f%%")
        plt.title(titulo)
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    # 6. Mapa de calor: Minutes vs Passes Completed
    
    def mapa_calor_minutos_pases(self):
        df = self.df[["Minutes", "Passes Completed"]].copy()

        corr = df.corr()

        plt.figure(figsize=(6,5))
        sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        plt.title("Correlación: Minutos vs Pases Completados")
        plt.tight_layout()
        plt.show()

    
    # 7. Barras horizontales: goles por posición
     
    def goles_por_posicion(self):
        df = self.df.copy()
        df["MainPosition"] = df["Position"].astype(str).apply(lambda x: x.split(",")[0])

        goles_posicion = df.groupby("MainPosition")["Goals"].sum().sort_values()

        plt.figure(figsize=(10,6))
        plt.barh(goles_posicion.index, goles_posicion.values, color="skyblue", edgecolor="black")
        plt.title("Goles Totales por Posición")
        plt.xlabel("Goles")
        plt.ylabel("Posición")
        plt.grid(axis="x", linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()
