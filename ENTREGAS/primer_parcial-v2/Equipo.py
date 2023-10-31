import json
from Jugador import Jugador
from Estadistica import Estadistica

class Equipo:

    __path_json = ""
    __lista_jugadores = []

    def __init__(self, path_json) -> None:
        self.__path_json = path_json
        self.set_lista_jugadores()

    def leer_json(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido_json = json.load(archivo)
        return contenido_json
    
    def get_lista_jugadores(self):
        return self.__lista_jugadores
    
    def set_lista_jugadores(self):
        lista_jugadores_json = self.leer_json(self.__path_json).get("jugadores")
        for jugador in lista_jugadores_json:
            objeto_estadistica = Estadistica(**jugador.get("estadisticas"))
            objeto_jugador = Jugador(
                                jugador.get("nombre"), 
                                jugador.get("posicion"), 
                                objeto_estadistica, 
                                jugador.get("logros")
                            )
            self.__lista_jugadores.append(objeto_jugador)

    def get_lista_jugadores_ordenada_por_clave_asc(self, lista, key):
        if len(lista) < 2:
            return lista
        else:
            copia_lista_jugadores = lista.copy()
            jugador_pivot = copia_lista_jugadores.pop()
            dato_a_comparar_jugador_pivot = jugador_pivot.get_estadistica().get_estadistas_dict()[key]
            mas_grandes = []
            mas_chicos = []
            for jugador in copia_lista_jugadores:
                dato_a_comparar_jugador = jugador.get_estadistica().get_estadistas_dict()[key]
                if dato_a_comparar_jugador > dato_a_comparar_jugador_pivot:
                    mas_grandes.append(jugador)
                elif dato_a_comparar_jugador <= dato_a_comparar_jugador_pivot:
                    mas_chicos.append(jugador)
            return self.get_lista_jugadores_ordenada_por_clave_asc(mas_chicos, key) + [jugador_pivot] + self.get_lista_jugadores_ordenada_por_clave_asc(mas_grandes, key)
    
    def get_lista_jugadores_ordenada_alfabeticamente(self, lista):
        if len(lista) < 2:
            return lista
        else:
            copia_lista_jugadores = lista.copy()
            jugador_pivot = copia_lista_jugadores.pop()
            nombre_jugador_pivot = jugador_pivot.get_nombre()
            mas_grandes = []
            mas_chicos = []
            for jugador in copia_lista_jugadores:
                nombre_jugador = jugador.get_nombre()
                if nombre_jugador > nombre_jugador_pivot:
                    mas_grandes.append(jugador)
                elif nombre_jugador <= nombre_jugador_pivot:
                    mas_chicos.append(jugador)
            return self.get_lista_jugadores_ordenada_alfabeticamente(mas_chicos) + [jugador_pivot] + self.get_lista_jugadores_ordenada_alfabeticamente(mas_grandes)

    def get_promedio_puntos_equipo(self):
        total_puntos_equipo = sum(jugador.get_estadistica().get_promedio_puntos_por_partido() for jugador in self.__lista_jugadores)
        cantidad_jugadores = len(self.__lista_jugadores)
        return total_puntos_equipo / cantidad_jugadores

    def get_miembros_salon_de_la_fama(self):
        string = "Miembro del Salon de la Fama del Baloncesto"
        return [jugador.get_nombre().lower() for jugador in self.__lista_jugadores if string in jugador.get_logros()]






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

# equipo = Equipo("dream_team.json")
# print(equipo.get_promedio_puntos_equipo())

# jugadores_ordenados = equipo.get_lista_jugadores_ordenada_por_clave_asc(equipo.get_lista_jugadores(), "promedio_puntos_por_partido")
# for jugador in jugadores_ordenados:
#     print(f"{jugador.get_nombre()}")

# print("------------")

# jugadores_ordenados = equipo.get_lista_jugadores_ordenada_alfabeticamente(equipo.get_lista_jugadores())
# for jugador in jugadores_ordenados:
#     print(f"{jugador.get_nombre()}")


# print(equipo.get_lista_jugad
# 
# ores()[7].get_logros())

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/primer_parcial-v2
# python Equipo.py

# def ordenar_jugadores_por_nombre(self, lista: list[dict], key):
#     if len(lista) < 2:
#         return lista
#     else:
#         lista_copia = lista.copy()
#         pivot = lista_copia.pop()
#         mas_grandes = []
#         mas_chicos = []
#         for jugador in lista_copia:
#             if jugador[key] > pivot[key]:
#                 mas_grandes.append(jugador)
#             elif jugador[key] <= pivot[key]:
#                 mas_chicos.append(jugador)
#         return self.ordenar_jugadores_por_nombre(mas_chicos, key) + [pivot] + self.ordenar_jugadores_por_nombre(mas_grandes, key)

# def get_jugadores_destacados(self, key):
#     lista_jugadores = self.get_lista_jugadores()
#     valor_maximo = max(lista_jugadores, key = lambda jugador: jugador["estadisticas"][key])["estadisticas"][key]
#     listado_jugadores_destacados = filter(lambda jugador: jugador["estadisticas"][key] == valor_maximo, lista_jugadores)
#     return list(listado_jugadores_destacados)

# def imprimir_jugadores_destacados(self, key):
#     lista_jugadores = self.get_jugadores_destacados(key)
#     texto = f"Jugador/es con la mayor cantidad de {key.replace('_', ' ')}:\n"
#     for jugador in lista_jugadores:
#         nombre = jugador.get("nombre")
#         dato = jugador.get("estadisticas").get(key)
#         texto += f"{lista_jugadores.index(jugador) + 1}. {nombre}: {dato}\n"
#     print(texto)