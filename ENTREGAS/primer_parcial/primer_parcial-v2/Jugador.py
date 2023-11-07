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