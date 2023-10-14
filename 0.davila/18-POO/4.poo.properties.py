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
    def __init__(self, nombre):
        self.__nombre = nombre
    @property
    def nombre(self):
        print("(desde el metodo get_nombre() retorno el valor del atributo privado __name) ", end="")
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        print("el atributo privado __nombre se setea aca adentro, en set_nombre()")
        self.__nombre = nombre

personaje1 = Personaje("Vero")
print(personaje1.nombre)

separador()

personaje1.nombre = "Carolina"
print(personaje1.nombre)