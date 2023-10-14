from utils import *

limpiar_consola()

class Personaje:
    tipo = "HOLA"
    def __init__(self, nombre="") -> None:
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

# aux_personaje1 = Personaje()
aux_personaje2 = Personaje("Juana")
aux_personaje2.__nombre = "xxxxx"
aux_personaje2.gargiulo = 15

print(aux_personaje2.get_nombre())
print(aux_personaje2.__nombre)
print(aux_personaje2.get_nombre())
print(aux_personaje2.gargiulo)

separador()

aux_personaje2.set_nombre("yyyyy")
print(aux_personaje2.get_nombre())

separador()

resultado = aux_personaje2.gargiulo * 2 + 15
print(type(aux_personaje2.gargiulo))
print(resultado)