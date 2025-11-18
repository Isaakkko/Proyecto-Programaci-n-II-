
# Colegio Universitario de Cartago
##Costa Rica
![](https://images.seeklogo.com/logo-png/3/1/colegio-universitario-de-cartago-cuc-logo-png_seeklogo-33301.png)

###Realizado por:
-Isaac Ulloa Calvo
-Jeffrey Jiménez Cordero
-Felipe Montenegro Artavia

# 📊 Premier League Insights

Este proyecto implementa un sistema orientado a objetos en Python para analizar datos reales de la Premier League (2024/2025). Incluye ingesta de datos, análisis exploratorio (EDA), modelado de entidades del dominio y visualización estática e interactiva.

---

## 📁 Información general del dataset

- **Competición:** Premier League  
- **Rango de fechas:** 16 de agosto – 12 de diciembre de 2024  
- **Filas:** 4,270  
- **Columnas:** 33  
- **Total de datos aproximado:** 140,910  
- **Porcentaje de nulos:** 0.04%  
- **Duplicados:** 0  
- **Formato original:** CSV (`premier.csv`)

El proyecto analiza este dataset para identificar patrones, relaciones entre variables y generar hallazgos mediante gráficos y exploración estadística.

---

# 🧩 Arquitectura del proyecto

Este proyecto sigue una estructura modular orientada a objetos

#✔️ Requerimientos técnicos

Python 3.10+

Librerías:
pandas
numpy
matplotlib
seaborn
streamlit 


#👉Contenido  y estructura del repositorio

+ Premier League
    * CARGA_DATA
	-cargador_datos
	-modulo
    * CLASES
	-Equipo
	-Jugador
	-modulo
    * DASHBOARDS
	-visualizador
    * DATA
	-PROCESSED(LIMPIO)
	--premier_clean
	-RAW(CRUDO)
	--premier
    * EDA
	modulo
	Procesador_eda
    * NOTEBOOKS
	* VISUALIZACIÓN



# ⚙️ Funcionalidades principales

### 1. 📥 Ingesta de datos — `CargadorDatos`
La clase **CargadorDatos** se encarga de:

- Cargar el archivo `premier.csv`
- Verificar número de filas/columnas
- Calcular el porcentaje de datos nulos
- Mostrar un resumen inicial del dataset

### 2. 🧼 Procesamiento y EDA — `ProcesadorEDA`

Incluye métodos para:

- Limpieza de datos  
  - Conversión de tipos  
  - Manejo de nulos  
  - Normalización de categorías  
- Resumen estadístico (mean, std, median, quartiles, etc.)
- Matriz de correlación
- Identificación de valores faltantes
- Exportación del dataset limpio (`premier_clean.csv`)

### 3. 📊 Visualización — `Visualizador`

Genera gráficos como:

- Histogramas  
- Heatmap de correlación  
- Gráficos de dispersión  
- Comparaciones entre métricas clave (goles, asistencias, minutos, etc.)  


### 4. 🧱 Modelado del dominio — `Jugador` y `Equipo`

Clases que representan entidades reales de la Premier League:

- **Jugador**: nombre, equipo, posición, edad, minutos, goles, asistencias…
- **Equipo**: nombre del equipo, liga, lista de jugadores.



#FIN
