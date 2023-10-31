class Jugador():
    def __init__(self, 
                nombre: str, 
                posicion: str, 
                estadistica: dict,
                logros: list) -> None:
        self.__nombre = nombre
        self.__posicion = posicion
        self.__estadistica = estadistica
        self.__logros = logros 

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_posicion(self):
        return self.__posicion
    
    def set_posicion(self, posicion):
        self.__posicion = posicion
    
    def get_estadistica(self):
        return self.__estadistica
    
    def set_estadistica(self, estadistica):
        self.__estadistica = estadistica
    
    def get_logros(self):
        return self.__logros
    
    def set_logros(self, logros):
        self.__logros = logros

"""  
La Clase Equipo será la encargada de levantar el archivo JSON y realizar todas las
tareas relacionadas a archivos. También se encargará de crear a cada jugador al leer el
JSON y agregarlos a una lista de jugadores la cual deberá ser atributo de la clase
Equipo.

Cada jugador tendrá como atributos una lista de logros, un nombre, posición y un
objeto de clase Estadistica.

Cada estadística tendrá 12 atributos los cuales deberán tener sus respectivos getters &
setters / properties.
Cada clase deberá tener sus respectivos Getters & Setters o properties.

"""

# import os
# def limpiar_consola():
#     if os.name in ["ce", "nt", "dos"]: # windows
#         os.system("cls")
#     else: # linux o mac
#         os.system("clear")
# limpiar_consola()

# estadistica = {
#     "temporadas": 15,
#     "puntos_totales": 32292,
#     "promedio_puntos_por_partido": 30.1,
#     "rebotes_totales": 6672,
#     "promedio_rebotes_por_partido": 6.2,
#     "asistencias_totales": 5633,
#     "promedio_asistencias_por_partido": 5.3,
#     "robos_totales": 2514,
#     "bloqueos_totales": 893,
#     "porcentaje_tiros_de_campo": 49.7,
#     "porcentaje_tiros_libres": 83.5,
#     "porcentaje_tiros_triples": 32.7
# }
# logros = [
#     "6 veces campeón de la NBA",
#     "6 veces MVP de la NBA",
#     "14 veces All-Star",
#     "10 veces líder en anotaciones de la NBA",
#     "5 veces MVP de las Finales de la NBA",
#     "Defensor del Año en la NBA en 1988",
#     "Miembro del Salon de la Fama del Baloncesto"
# ]

# jugador = Jugador("Michael Jordan", "Escolta", estadistica, logros)

# print(jugador.get_logros())
# jugador.set_logros(["goles", "campeonatos"])
# print(jugador.get_logros())
