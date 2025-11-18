#uso de la clase
from Procesador_eda import ProcesadorEDA

archivo_crudo = r"../DATA/RAW(CRUDO)/premier.csv"
archivo_limpio = r"../DATA/PROCESSED(LIMPIO)/premier_clean.csv"

procesador = ProcesadorEDA(archivo_crudo=archivo_crudo, archivo_limpio=archivo_limpio)
procesador.exploracion_inicial()
procesador.limpieza()
procesador.valores_faltantes()
procesador.eliminar_columnas()
procesador.eliminar_duplicados()
procesador.normalizar_categoricas()
procesador.guardar_dataframe()