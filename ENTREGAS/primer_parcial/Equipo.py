import json
from utils import * 

class Equipo:
    __lista_jugadores = []
    def __init__(self) -> None:
        pass
    def leer_json(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido_json = json.load(archivo)
        return contenido_json
    def get_lista_jugadores(self):
        self.set_lista_jugadores()
        return self.ordenar_jugadores_por_nombre(self.__lista_jugadores, "nombre")
    def set_lista_jugadores(self):
        json_jugadores = self.leer_json("dream_team.json")
        self.__lista_jugadores = json_jugadores.get("jugadores")
    def ordenar_jugadores_por_nombre(self, lista: list[dict], key):
        if len(lista) < 2:
            return lista
        else:
            lista_copia = lista.copy()
            pivot = lista_copia.pop()
            mas_grandes = []
            mas_chicos = []
            for jugador in lista_copia:
                if jugador[key] > pivot[key]:
                    mas_grandes.append(jugador)
                elif jugador[key] <= pivot[key]:
                    mas_chicos.append(jugador)
            return self.ordenar_jugadores_por_nombre(mas_chicos, key) + [pivot] + self.ordenar_jugadores_por_nombre(mas_grandes, key)
    def imprimir_listado_jugadores(self):
        lista_jugadores = self.get_lista_jugadores()
        for jugador in lista_jugadores:
            nro_orden = lista_jugadores.index(jugador) + 1
            nombre = jugador.get('nombre')
            posicion = jugador.get('posicion')
            puntos_por_partido = f"{jugador.get('estadisticas').get('promedio_puntos_por_partido')} puntos por partido"
            print(f"{nro_orden}. {nombre} - {posicion} || {puntos_por_partido}")
    def jugadores_destacados(self, key):
        lista_jugadores = self.get_lista_jugadores()
        valor_maximo = max(lista_jugadores, key = lambda jugador: jugador["estadisticas"][key])["estadisticas"][key]
        listado_jugadores_destacados = filter(lambda jugador: jugador["estadisticas"][key] == valor_maximo, lista_jugadores)
        return list(listado_jugadores_destacados)
    def imprimir_jugadores_destacados(self, key):
        lista_jugadores = self.jugadores_destacados(key)
        texto = f"Jugador/es con la mayor cantidad de {key.replace('_', ' ')}:\n"
        for jugador in lista_jugadores:
            nombre = jugador.get("nombre")
            dato = jugador.get("estadisticas").get(key)
            texto += f"{lista_jugadores.index(jugador) + 1}. {nombre}: {dato}\n"
        print(texto)

limpiar_consola()
estadistica = Equipo()
estadistica.imprimir_listado_jugadores()
print("\n")
estadistica.imprimir_jugadores_destacados("rebotes_totales")
print("--------------------")
print("\n")
print("""
Menú de opciones:

A Estadísticas completas jugador (2 - 3)
B Logros jugador (4 - 6)
C Salir
""")



"""  
1. Armstrong asd - Escolta - 28 puntos por partido
2. Chester asd - Base - 31 puntos por partido
3. Jordan asd - asdsad - 35 puntos por partido 
4. Princeton asd - asdsad - 48 puntos por partido 
5. asd asd - asdsad 
6. asd asd - asdsad 
7. asd asd - asdsad 
8. asd asd - asdsad 
9. asd asd - asdsad 
10. asd asd - asdsad (1 - 5)

jugador con la mayor cantidad de rebotes totales: Jordan (54) (7)

---------------

Menú de opciones:

A Estadísticas completas jugador (2 - 3)
B Logros jugador (4 - 6)
C Salir
"""