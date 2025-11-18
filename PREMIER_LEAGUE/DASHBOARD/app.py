
import streamlit as st  # permite crear "interfaces" de manera sencilla
import pandas as pd # ayuda con procesamiento de datos
import altair as alt # ayuda a tener graficos interactivos y personalizados 

st.title("Dashboard Premier League")

# Cargar CSV
df = pd.read_csv(r"C:\Proyecto 2 Progra 2\premier_clean.csv") # cambiar a ruta necesaria ya que streamlit trabaja local

# Vista previa
st.write("Vista previa del dataset:")
st.dataframe(df.head())

# Convertir columnas numéricas
cols = ["Shot-Creating Actions", "Goals", "Touches"]
for c in cols:
    df[c] = pd.to_numeric(df[c].astype(str).str.replace(",", "."), errors="coerce")

# Agrupar para evitar valores duplicados
df_grouped = df.groupby("Player", as_index=False).agg({
    "Shot-Creating Actions": "sum",
    "Goals": "sum",
    "Touches": "sum"
})


# Gráfico 1 – Shot Creating Actions

st.write("Top jugadores por Shot-Creating Actions")
top_sca = df_grouped.sort_values("Shot-Creating Actions", ascending=False).head(10)

chart1 = (
    alt.Chart(top_sca)
    .mark_bar()
    .encode(
        x=alt.X("Player:N", sort=None),
        y="Shot-Creating Actions:Q",
        color="Player:N"
    )
)
st.altair_chart(chart1, use_container_width=True)


# Gráfico 2 – Goals

st.write("Top jugadores por Goals")
top_goals = df_grouped.sort_values("Goals", ascending=False).head(10)

chart2 = (
    alt.Chart(top_goals)
    .mark_bar()
    .encode(
        x=alt.X("Player:N", sort=None),
        y="Goals:Q",
        color="Player:N"
    )
)
st.altair_chart(chart2, use_container_width=True)


# Gráfico 3 – Touches

st.write("Jugadores con más Toques")
top_touches = df_grouped.sort_values("Touches", ascending=False).head(10)

chart3 = (
    alt.Chart(top_touches)
    .mark_bar()
    .encode(
        x=alt.X("Player:N", sort=None),
        y="Touches:Q",
        color="Player:N"
    )
)
st.altair_chart(chart3, use_container_width=True)



