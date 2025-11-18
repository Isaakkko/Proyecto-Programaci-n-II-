#uso de la clase
import pandas as pd
from Jugador import Jugador

# cargar el DataFrame
df = pd.read_csv(r"../DATA/PROCESSED(LIMPIO)/premier_clean.csv")

# tomar una fila de ejemplo (primer jugador del dataset)
fila = df.iloc[0]

