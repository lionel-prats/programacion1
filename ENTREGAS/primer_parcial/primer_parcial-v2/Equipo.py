import json
import time
import uuid
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

    def get_lista_nombres_jugadores(self):
        return [jugador.get_nombre().lower() for jugador in self.__lista_jugadores]
    
    def get_miembros_salon_de_la_fama(self):
        string = "Miembro del Salon de la Fama del Baloncesto"
        return [jugador.get_nombre().lower() for jugador in self.__lista_jugadores if string in jugador.get_logros()]

    def get_jugadores_destacados(self, clave):
        # armo el nombre del metodo de Estadistica a validar
        getter = f"get_{clave}"
        
        # Guardo el metodo (si existe) o None, si no
        existe_metodo = getattr(Estadistica, getter, None) 
        
        if existe_metodo: # el metodo existe en Estadistica

            lista_valores_buscados = [] # lista de los valores a comparar de cada jugador
            
            lista_jugadores_destacados = [] # lista de los jugadores cuyo valor coincida con el maximo hallado
            
            for jugador in self.get_lista_jugadores():

                get_valor_buscado_jugador = getattr(jugador.get_estadistica(), getter) # almaceno en memoria (?) el getter deseado para el jugador iterado
                
                lista_valores_buscados.append(get_valor_buscado_jugador()) # guardo en la lista el valor del jugador iterado

            valor_maximo = max(lista_valores_buscados, key = lambda valor: valor) # hallo el valor maximo del valor buscado

            for jugador in self.get_lista_jugadores():

                valor_jugador = getattr(jugador.get_estadistica(), getter)() # guardo el valor del jugador iterado para validar si coincide con el valor maximo hallado
                
                if valor_jugador == valor_maximo: # coincide

                    # como coincide, apendeo a la lista final un diccionario con el nombre y el valor del jugador iterado
                    lista_jugadores_destacados.append({
                        "nombre": jugador.get_nombre(),
                        clave: valor_jugador
                    })
            return lista_jugadores_destacados
        else:
            return None

    def guardar_estadisticas_jugador(self, id_jugador:int):
        """
        genera o reescribe un .csv con el nombre y el contenido especificados por el usuario\n
        nombre_archivo_csv: str -> nombre del archivo a crear\n
        contenido_csv: str -> contenido del archivo a crear\n
        return bool -> True si el archivo se pudo crear, False caso contrario
        """ 
        jugador = self.__lista_jugadores[int(id_jugador)]
        nombre_jugador = jugador.get_nombre() 
        estadisticas_jugador_dict = jugador.get_estadistica().get_estadistas_dict()
        
        nombre_archivo = self.generar_nombre_unico_archivo(nombre_jugador)
        
        contenido = "nombre;posicion;"
        contenido += ";".join(estadisticas_jugador_dict.keys())
        contenido += "\n"
        contenido += f"{nombre_jugador};"
        contenido += f"{jugador.get_posicion()};"
        contenido += ";".join([str(valor) for valor in estadisticas_jugador_dict.values()])
        # print(nombre_archivo)
        try:
            with open(f"estadisticas_jugadores/{nombre_archivo}", "w", encoding="utf-8") as nuevo_archivo:
                nuevo_archivo.write(f"{contenido}")
            return f"el archivo \"{nombre_archivo}\" ha sido creado correctamente"
        except:  
            return None

    def generar_nombre_unico_archivo(self, nombre_generico):
        nombre_generico = nombre_generico.replace(" ","_").lower()
        timestamp = int(time.time() * 1000) # timestamp en milisegundos

        # uuid -> modulo de Python
        # uuid4() -> metodo de uuid que genera un identificador único universal (UUID-Universally Unique Identifier) de forma aleatoria
        # genera un id del tipo 550e8400-e29b-41d4-a716-446655440000, por lo que reemplazo los "-" por ""
        unique_id = str(uuid.uuid4()).replace("-", "")

        nombre_archivo = f"{nombre_generico}__{timestamp}_{unique_id}.csv"
        return nombre_archivo

if __name__ == "__main__":
    pass
    # import os
    # def limpiar_consola():
    #     if os.name in ["ce", "nt", "dos"]: # windows
    #         os.system("cls")
    #     else: # linux o mac
    #         os.system("clear")
    # limpiar_consola()