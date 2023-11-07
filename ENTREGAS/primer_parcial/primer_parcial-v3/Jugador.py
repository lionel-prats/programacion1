""" 
Fecha: 31-10-2023
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Parcial nro. 1
"""

# IMPORTANTE: para la creacion de archivos funcione hay que crear la carpeta /estadisticas_jugadores en la raiz del proyecto

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
        """  
        retorna el nombre del jugador
        """
        return self.__nombre
    
    def set_nombre(self, nombre):
        """  
        setea el nombre del jugador
        """
        self.__nombre = nombre

    def get_posicion(self):
        """  
        retorna la posicion del jugador
        """
        return self.__posicion
    
    def set_posicion(self, posicion):
        """  
        setea la posicion del jugador
        """
        self.__posicion = posicion
    
    def get_estadistica(self):
        """  
        retorna el atributo __estadistica del jugador (instancia de Estadistica)
        """
        return self.__estadistica
    
    def set_estadistica(self, estadistica):
        """  
        setea el atributo __estadistica del jugador (instancia de Estadistica)
        """
        self.__estadistica = estadistica
    
    def get_logros(self):
        """  
        retorna el atributo __logros del jugador
        """
        return self.__logros
    
    def set_logros(self, logros):
        """  
        setea el atributo __logros del jugador
        """
        self.__logros = logros