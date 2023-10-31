class Estadistica():

    def __init__(self, 
                temporadas: int, 
                puntos_totales: int, 
                promedio_puntos_por_partido: float,
                rebotes_totales: int,
                promedio_rebotes_por_partido: float,
                asistencias_totales: int,
                promedio_asistencias_por_partido: float,
                robos_totales: int,
                bloqueos_totales: int,
                porcentaje_tiros_de_campo: float,
                porcentaje_tiros_libres: float,
                porcentaje_tiros_triples: float) -> None:
        self.__temporadas = temporadas
        self.__puntos_totales = puntos_totales
        self.__promedio_puntos_por_partido = promedio_puntos_por_partido
        self.__rebotes_totales = rebotes_totales 
        self.__promedio_rebotes_por_partido = promedio_rebotes_por_partido
        self.__asistencias_totales = asistencias_totales
        self.__promedio_asistencias_por_partido = promedio_asistencias_por_partido
        self.__robos_totales = robos_totales 
        self.__bloqueos_totales = bloqueos_totales 
        self.__porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
        self.__porcentaje_tiros_libres = porcentaje_tiros_libres 
        self.__porcentaje_tiros_triples = porcentaje_tiros_triples 

    def get_temporadas(self):
        return self.__temporadas
    
    def set_temporadas(self, temporadas):
        self.__temporadas = temporadas

    def get_puntos_totales(self):
        return self.__puntos_totales
    
    def set_puntos_totales(self, puntos_totales):
        self.__puntos_totales = puntos_totales
    
    def get_promedio_puntos_por_partido(self):
        return self.__promedio_puntos_por_partido
    
    def set_promedio_puntos_por_partido(self, promedio_puntos_por_partido):
        self.__promedio_puntos_por_partido = promedio_puntos_por_partido
    
    def get_rebotes_totales(self):
        return self.__rebotes_totales
    
    def set_rebotes_totales(self, rebotes_totales):
        self.__rebotes_totales = rebotes_totales
    
    def get_promedio_rebotes_por_partido(self):
        return self.__promedio_rebotes_por_partido
    
    def set_promedio_rebotes_por_partido(self, promedio_rebotes_por_partido):
        self.__promedio_rebotes_por_partido = promedio_rebotes_por_partido
    
    def get_asistencias_totales(self):
        return self.__asistencias_totales
    
    def set_asistencias_totales(self, asistencias_totales):
        self.__asistencias_totales = asistencias_totales
    
    def get_promedio_asistencias_por_partido(self):
        return self.__promedio_asistencias_por_partido
    
    def set_promedio_asistencias_por_partido(self, promedio_asistencias_por_partido):
        self.__promedio_asistencias_por_partido = promedio_asistencias_por_partido
    
    def get_robos_totales(self):
        return self.__robos_totales
    
    def set_robos_totales(self, robos_totales):
        self.__robos_totales = robos_totales
    
    def get_bloqueos_totales(self):
        return self.__bloqueos_totales
    
    def set_bloqueos_totales(self, bloqueos_totales):
        self.__bloqueos_totales = bloqueos_totales
    
    def get_porcentaje_tiros_de_campo(self):
        return self.__porcentaje_tiros_de_campo
    
    def set_porcentaje_tiros_de_campo(self, porcentaje_tiros_de_campo):
        self.__porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
    
    def get_porcentaje_tiros_libres(self):
        return self.__porcentaje_tiros_libres
    
    def set_porcentaje_tiros_libres(self, porcentaje_tiros_libres):
        self.__porcentaje_tiros_libres = porcentaje_tiros_libres
    
    def get_porcentaje_tiros_triples(self):
        return self.__porcentaje_tiros_triples
    
    def set_porcentaje_tiros_triples(self, porcentaje_tiros_triples):
        self.__porcentaje_tiros_triples = porcentaje_tiros_triples

    def get_estadistas_dict(self):
        return {
            "temporadas": self.__temporadas,
            "puntos_totales": self.__puntos_totales,
            "promedio_puntos_por_partido": self.__promedio_puntos_por_partido,
            "rebotes_totales": self.__rebotes_totales,
            "promedio_rebotes_por_partido": self.__promedio_rebotes_por_partido,
            "asistencias_totales": self.__asistencias_totales,
            "promedio_asistencias_por_partido": self.__promedio_asistencias_por_partido,
            "robos_totales": self.__robos_totales,
            "bloqueos_totales": self.__bloqueos_totales,
            "porcentaje_tiros_de_campo": self.__porcentaje_tiros_de_campo,
            "porcentaje_tiros_libres": self.__porcentaje_tiros_libres,
            "porcentaje_tiros_triples": self.__porcentaje_tiros_triples
        }


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

# diccionario = {
#     "temporadas": 10, 
#     "puntos_totales": 20, 
#     "promedio_puntos_por_partido": 30,
#     "rebotes_totales": 40,
#     "promedio_rebotes_por_partido": 50,
#     "asistencias_totales": 60,
#     "promedio_asistencias_por_partido": 70,
#     "robos_totales": 80,
#     "bloqueos_totales": 90,
#     "porcentaje_tiros_de_campo": 100,
#     "porcentaje_tiros_libres": 110,
#     "porcentaje_tiros_triples": 120
# }
# estadistica = Estadistica(**diccionario)

# print(estadistica.get_temporadas())
# print(estadistica.get_puntos_totales())
# print(estadistica.get_promedio_puntos_por_partido())
# print(estadistica.get_rebotes_totales())
# print(estadistica.get_promedio_rebotes_por_partido())
# print(estadistica.get_asistencias_totales())
# print(estadistica.get_promedio_asistencias_por_partido())
# print(estadistica.get_robos_totales())
# print(estadistica.get_bloqueos_totales())
# print(estadistica.get_porcentaje_tiros_de_campo())
# print(estadistica.get_porcentaje_tiros_libres())
# print(estadistica.get_porcentaje_tiros_triples())
