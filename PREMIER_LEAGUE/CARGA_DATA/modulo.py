# uso de la clase
from cargador_datos import cargador_datos

cargador = cargador_datos("../DATA/RAW(CRUDO)/premier.csv")

cargador.cargar_datos()
cargador.resumen()


