from jugador import Jugador
from equipo import Equipo
import csv

equipos = {}  ### Creamos la lista vacia para guardar jugadores ###

ruta = r"C:\Proyecto 2 Progra 2\premier_clean.csv"   ### Cambiar ruta 

with open(ruta, encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        # Crear un jugador con lo que viene del CSV
        jugador = Jugador(
            fila["Player"],
            fila["Team"],
            fila["Position"],
            fila["Age"],
            fila["Minutes"],
            fila["Goals"],
            fila["Assists"]
        )
            # Si el equipo aún no está en el diccionario, lo creamos.
            # Esto es necesario porque el CSV solo trae jugadores, no objetos Equipo.
            # Cada vez que encontramos un jugador de un equipo nuevo, debemos crear ese equipo
            # para poder guardar ahí a todos sus jugadores.

        if jugador.team not in equipos:
            equipos[jugador.team] = Equipo(jugador.team, "Premier League")


            # Agregamos el objeto Jugador dentro de la lista 'jugadores' del equipo.
            # append() sirve para meter un elemento al final de la lista.

        equipos[jugador.team].agregar_jugador(jugador)



# Print para total de equipos
print("Equipos cargados:", len(equipos))

# Print para ver los nombres de los equipos
print("Lista de equipos cargados:")
for nombre in equipos:
    print("-", nombre)

# Print para ver la cantidad de jugadores de los equipos (Liverpool en este caso)
print("Jugadores del Liverpool:", len(equipos["liverpool"].jugadores))


# Primer jugador que aparece del liverpool
primer = equipos["liverpool"].jugadores[0]
print("Primer jugador del Liverpool:", primer.name)


# Edad del primer jugador que aparece del liverpool
print("Edad del primer jugador del Liverpool:", equipos["liverpool"].jugadores[0].age)





