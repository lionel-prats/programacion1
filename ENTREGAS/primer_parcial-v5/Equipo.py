""" 
Fecha: 31-10-2023
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Parcial nro. 1
"""

# IMPORTANTE: para la creacion de archivos funcione hay que crear la carpeta /estadisticas_jugadores en la raiz del proyecto
# IMPORTANTE: crear la carpeta /db en la raiz del proyecto para que funcione la parte de base e datos

import sqlite3
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

                get_valor_buscado_jugador = getattr(jugador.get_estadistica(), getter) # almaceno en memoria (?) el valor del dato buscado para el jugador iterado
                
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

    def get_lista_jugadores_ordenada_suma_estadisticas(self, tupla_getters: tuple):
        """  
        hasattr valida si un metodo existe en una clase
        recibe el nombre de la clase y el del metodo a buscar 
        retorna True si el metodo existe, False en caso contrario
        """
        
        lista_errores = []

        for getter in tupla_getters: 
            if not hasattr(Estadistica, getter):
                lista_errores.append(f"{getter}")
        if lista_errores:
            return {"errores": tuple(lista_errores)}
        else:

            lista_return = []
            maximo_total = 0 # aca voy a almacenar el maximo total hallado de las sumas obtenidas por cada jugador iterado
            primer_jugador = True # flag para almacenar la suma del primer jugador en la primera iteracion
            
            # recorro el listado original de jugadores para armar la lista que va a terminar retornando la funcion
            for jugador in self.__lista_jugadores:
                total_jugador = 0 # acumulador que contendra el total del jugador iterado
                jugador_diccionario = {"nombre": jugador.get_nombre()} # incializo el diccionario para un jugador, con su nombre
                
                # recorro la tupla de getters para obtenerr los valores de cada tipo de estadistica del jugador iterado y obtener el total para dicho jugador
                for getter in tupla_getters:
                    getter_almacenado_en_memoria = getattr(jugador.get_estadistica(), getter)
                    dato = getter_almacenado_en_memoria()
                    jugador_diccionario[getter[4:]] = dato # agrego al diccionario del jugador el atributo del tipo de estadistica iterado y el valor correspondiente
                    total_jugador += dato # acumulo y obtengo el total del jugador iterado
                    
                # bloque para hallar la suma maxima de entre todos los jugadores
                if primer_jugador:
                    maximo_total = total_jugador
                    primer_jugador = False
                elif total_jugador > maximo_total:
                    maximo_total = total_jugador
                
                jugador_diccionario["total"] = total_jugador # agrego el total hallado al diccionario del jugador iterado
                lista_return.append(jugador_diccionario) # appendeo la lista a retornar con el diccionario del jugador iterado

            # ordeno la lista a retornar, de mayor a menor, segun el atributo "total"
            lista_return = self.get_lista_diccionarios_ordenada_por_clave_desc(lista_return, "total", "DESC")
            
            # itero la lista a retornar, para obtener el porcentaje equivalente a total, para cada jugador, y agregar el dato a cada diccionario de jugador
            for jugador in lista_return:
                jugador["porcentaje"] = round(jugador.get("total") / maximo_total * 100, 2)
            
            return lista_return

    def get_lista_diccionarios_ordenada_por_clave_desc(self, lista, key, order = "ASC"):
        """  
        recibe una lista de diccionarios y una clave (valor int|float) del mismo\n
        tambien puede recibir un 3er parametro opcional que determina si el ordenamiento es ASC o DESC (default ASC)
        retorna una nueva lista con los mismos elementos de la recibida,\n
        pero ordenada segun la clave y el sentido recibidos
        """
        if len(lista) < 2:
            return lista
        else:
            copia_lista = lista.copy()
            jugador_pivot = copia_lista.pop()
            dato_a_comparar_jugador_pivot = jugador_pivot.get(key)
            anteriores = []
            posteriores = []
            for jugador in copia_lista:
                dato_a_comparar_jugador = jugador.get(key)
                if dato_a_comparar_jugador > dato_a_comparar_jugador_pivot:
                    if order == "DESC":
                        anteriores.append(jugador)
                    else:
                        posteriores.append(jugador)
                elif dato_a_comparar_jugador <= dato_a_comparar_jugador_pivot:
                    if order == "DESC":
                        posteriores.append(jugador)
                    else:
                        anteriores.append(jugador)
                    
            return self.get_lista_diccionarios_ordenada_por_clave_desc(anteriores, key, order) + [jugador_pivot] + self.get_lista_diccionarios_ordenada_por_clave_desc(posteriores, key, order)

    def get_tablas_db(self):
        """ 
        retorna un diccionario con la informacion de la db\n
        cada propiedad representa una tabla en la base de datos
        siendo la clave el nombre de la tabla y el valor una tupla con los nombres de los campos de esa tabla
        """
        return  {
                    "jugadores":(
                                    "nombre",
                                    "posicion",
                                    "temporadas",
                                    "puntos_totales",
                                    "promedio_puntos_por_partido",
                                    "rebotes_totales",
                                    "promedio_rebotes_por_partido",
                                    "asistencias_totales",
                                    "promedio_asistencias_por_partido",
                                    "robos_totales",
                                    "bloqueos_totales",
                                    "porcentaje_tiros_de_campo",
                                    "porcentaje_tiros_libres",
                                    "porcentaje_tiros_triples",
                                    "logros"
                                )
                } 
    
    def create_table(self, nombre_tabla):
        """  
        crea la tabla recibida por parametro en la db dream_team.db\n
        recibe el nombre de la tabla
        """
        db = self.get_tablas_db()
        if nombre_tabla not in db.keys():
            return False 
        else:

            # si el archivo .db no existe, automaticamente se crea en el path especificado
            with sqlite3.connect("db/dream_team.db") as conexion:
                try:
                    query = f""" 
                        create table if not exists {nombre_tabla}(
                            id integer primary key autoincrement,
                            nombre text,
                            posicion text,
                            temporadas integer,
                            puntos_totales integer,
                            promedio_puntos_por_partido real,
                            rebotes_totales integer,
                            promedio_rebotes_por_partido real,
                            asistencias_totales integer,
                            promedio_asistencias_por_partido real,
                            robos_totales integer,
                            bloqueos_totales integer,
                            porcentaje_tiros_de_campo real,
                            porcentaje_tiros_libres real,
                            porcentaje_tiros_triples real,
                            logros text,
                            created_at text,
                            updated_at text
                        )
                    """
                    conexion.execute(query)
                    return f"La tabla \"{nombre_tabla}\" se ha creado correctamente"
                except sqlite3.OperationalError:
                    return f"La tabla \"{nombre_tabla}\" ya existe"

    def insert_db(self, nombre_tabla: str, data_insert):
        tabla_existe = self.create_table(nombre_tabla)
        if not tabla_existe:
            print(f"\nError: la tabla \"{nombre_tabla}\" no existe en la DB.")
            return
        
        query = f"INSERT INTO {nombre_tabla} ("
        query += ",".join(data_insert[0].keys())
        query += ") values ("
        for i in range (0, len(data_insert[0].keys())):
            query += "?,"
        query = query[:-1]
        query += ")"

        lista_values_inserts = []
        for jugador in data_insert:
            lista_aux = []
            for v in jugador.values():
                lista_aux.append(v) 
            lista_values_inserts.append(tuple(lista_aux))

        with sqlite3.connect("db/dream_team.db") as conexion:
            try:
                for values in lista_values_inserts:
                    conexion.execute(query, values)
                conexion.commit() # hace el insert en la tabla
                return True
            except:
                return False
    
    def crear_tabla_posiciones(self):
        """ 
        si ya existe la tabla posiciones, la borra\n
        luego crea la tabla posiciones y hace 5 inserts para las cinco posiciones del basketball
        """
        with sqlite3.connect("db/dream_team.db") as conexion:
            try:

                query = "DROP TABLE IF EXISTS posiciones"
                conexion.execute(query)

                query = """
                    CREATE TABLE posiciones (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        posicion TEXT
                    )
                """
                conexion.execute(query)

                conexion.execute("INSERT INTO posiciones (posicion) VALUES (?)", ("Ala-Pivot",))
                conexion.execute("INSERT INTO posiciones (posicion) VALUES (?)", ("Alero",))
                conexion.execute("INSERT INTO posiciones (posicion) VALUES (?)", ("Base",))
                conexion.execute("INSERT INTO posiciones (posicion) VALUES (?)", ("Escolta",))
                conexion.execute("INSERT INTO posiciones (posicion) VALUES (?)", ("Pivot",))
                conexion.commit()

                return True
    
            except sqlite3.OperationalError as e:
                return False
    


if __name__ == "__main__":
    pass
    # equipo = Equipo("dream_team.json")
    # print(equipo.crear_tabla_posiciones())

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/primer_parcial-v4
# python main.py

