########### Clase Equipo ###########

class Equipo:
    def __init__(self, name, liga):
        self.name = name
        self.liga = liga
        self.jugadores = []  # lista vacía

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
