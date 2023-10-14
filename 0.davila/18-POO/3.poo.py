from utils import *

limpiar_consola()

# class Empleado:
#     nivel_educativo_minimo = "secundario"
#     def __init__(self, id, nombre="", apellido="", edad="") -> None:
#         self.id = id 
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#     def get_nombre_completo(self):
#         return f"{self.nombre} {self.apellido}"
#     def get_nivel_educativo(self):
#         return self.nivel_educativo_minimo

class Personaje:
    __edad = 38
    pais = "Argentina"
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

armani = Personaje()
print(armani)
print(armani.pais)
print(armani.get_edad())
# print(armani.__edad)
print(armani.set_edad(45))
print(armani.get_edad())

separador()

# se crea y guarda en memoria una esopcie de variable suelta, pero que no afecta al objeto
# segun chatGTP "Esto crea un nuevo atributo __edad específico de esa instancia, que no está relacionado con el atributo __edad de la clase Personaje.""
armani.__edad = 15
print(type(armani.__edad))
print(armani.__edad)

print(armani.get_edad())

separador()

armani.pais = "España"
print(armani.pais)
