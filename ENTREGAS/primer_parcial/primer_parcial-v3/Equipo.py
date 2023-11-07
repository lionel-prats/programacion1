""" 
Fecha: 31-10-2023
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Parcial nro. 1
"""

# IMPORTANTE: para la creacion de archivos funcione hay que crear la carpeta /estadisticas_jugadores en la raiz del proyecto

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
        """  
        recibe la ruta del archivo json y retorna el contenido del archivo parseado
        """
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido_json = json.load(archivo)
        return contenido_json
    
    def get_lista_jugadores(self):
        """ 
        retorna la lista de jugadores levantada del json
        """
        return self.__lista_jugadores
    
    def set_lista_jugadores(self):
        """  
        setea el atributo __lista_jugadores
        """
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
        """  
        recibe una lista de jugadores y una clave (robos_totales, temporadas, etc)\n
        retorna la misma lista ordenada por esos valores de menor a mayor
        """
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
    
    def get_lista_jugadores_ordenada_por_clave_desc(self, lista, key):
        """  
        recibe una lista de jugadores y una clave (robos_totales, temporadas, etc)\n
        retorna la misma lista ordenada por esos valores de mayor a menor
        """
        if len(lista) < 2:
            return lista
        else:
            copia_lista_jugadores = lista.copy()
            jugador_pivot = copia_lista_jugadores.pop()
            dato_a_comparar_jugador_pivot = jugador_pivot.get_estadistica().get_estadistas_dict()[key]
            anteriores = []
            posteriores = []
            for jugador in copia_lista_jugadores:
                dato_a_comparar_jugador = jugador.get_estadistica().get_estadistas_dict()[key]
                if dato_a_comparar_jugador > dato_a_comparar_jugador_pivot:
                    anteriores.append(jugador)
                elif dato_a_comparar_jugador <= dato_a_comparar_jugador_pivot:
                    posteriores.append(jugador)
            return self.get_lista_jugadores_ordenada_por_clave_desc(anteriores, key) + [jugador_pivot] + self.get_lista_jugadores_ordenada_por_clave_desc(posteriores, key)
    
    def get_lista_jugadores_ordenada_alfabeticamente(self, lista):
        """  
        recibe una lista de jugadores\n
        retorna la misma lista ordenada ordenada alfabeticamente segun los nombres de los jugadores
        """
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
        """  
        retorna el promedio de puntos del equipo, segun el promedio de puntos por partido de cada jugador
        """
        total_puntos_equipo = sum(jugador.get_estadistica().get_promedio_puntos_por_partido() for jugador in self.__lista_jugadores)
        cantidad_jugadores = len(self.__lista_jugadores)
        return total_puntos_equipo / cantidad_jugadores

    def get_lista_nombres_jugadores(self):
        """  
        retorna una lista, solo con los nombres de los jugadores
        """
        return [jugador.get_nombre().lower() for jugador in self.__lista_jugadores]
    
    def get_miembros_salon_de_la_fama(self):
        """  
        retorna la lista de jugadores que sean miembros del Salon de la Fama del Baloncesto
        """
        string = "Miembro del Salon de la Fama del Baloncesto"
        return [jugador.get_nombre().lower() for jugador in self.__lista_jugadores if string in jugador.get_logros()]

    def get_jugadores_destacados(self, clave):
        """ 
        recibe una clave (robos_totales, temporadas, etc)\n
        si la clave recibida existe en el objeto Jugador, retona la lista de jugadores cuyos valores coincidan con el maximo hallado para la clave recibida\n
        si la clave recibida no existe en el objeto Jugador, la funcion retorna None
        """
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
        recibe el id de uno de los jugadores de la lista general\n
        genera un .csv con las estadisticas del jugador asociado a ese id
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
        try:
            with open(f"estadisticas_jugadores/{nombre_archivo}", "w", encoding="utf-8") as nuevo_archivo:
                nuevo_archivo.write(f"{contenido}")
            return f"el archivo \"{nombre_archivo}\" ha sido creado correctamente"
        except:  
            return None

    def generar_nombre_unico_archivo(self, nombre_generico, es_json=False):
        """ 
        genera un nombre unico para nombrar un archivo
        recibe un string que sera parte del nombre del archivo\n
        recibe un parametro opcional, un boolean, para definir si la extension sera .csv o .json
        retorna una cadena compuesta por dicho string + la fecha unix del momento de la ejecucion de la funcion + un hash aleatorio + la extension que corresponda\n
        """
        nombre_generico = nombre_generico.replace(" ","_").lower()
        timestamp = int(time.time() * 1000) # timestamp en milisegundos

        # uuid -> modulo de Python
        # uuid4() -> metodo de uuid que genera un identificador único universal (UUID-Universally Unique Identifier) de forma aleatoria
        # genera un id del tipo 550e8400-e29b-41d4-a716-446655440000, por lo que reemplazo los "-" por ""
        unique_id = str(uuid.uuid4()).replace("-", "")

        # nombre_archivo = f"{nombre_generico}__{timestamp}_{unique_id}.csv"
        nombre_archivo = f"{nombre_generico}__{timestamp}_{unique_id}"
        if es_json:
            nombre_archivo += ".json"
        else:
            nombre_archivo += ".csv"
            
        return nombre_archivo

    def crear_csv(self, nombre_archivo, contenido):
        """  
        genera un archivo .csv\n
        recibe un string que sera parte del nombre del archivo\n
        recibe un 2do string que sera el contenido del archivo\n
        retorna True si se pudo crear el archivo, False en caso contrario 
        """
        nombre_archivo = self.generar_nombre_unico_archivo(nombre_archivo)
        try:
            with open(f"estadisticas_jugadores/{nombre_archivo}", "w", encoding="utf-8") as nuevo_archivo:
                nuevo_archivo.write(f"{contenido}")
            return f"el archivo \"{nombre_archivo}\" ha sido creado correctamente"
        except:  
            return None
        
    def crear_json(self, nombre_archivo, contenido):
        """  
        genera un archivo .json\n
        recibe un string que sera parte del nombre del archivo\n
        recibe un 2do string que sera el contenido del archivo\n
        retorna True si se pudo crear el archivo, False en caso contrario 
        """
        nombre_archivo = self.generar_nombre_unico_archivo(nombre_archivo, True)
        try:
            with open(f"estadisticas_jugadores/{nombre_archivo}", "w", encoding="utf-8") as nuevo_archivo:
                json.dump(contenido, nuevo_archivo, indent=4, ensure_ascii=False)
            return f"el archivo \"{nombre_archivo}\" ha sido creado correctamente"
        except:  
            return None


if __name__ == "__main__":
    pass