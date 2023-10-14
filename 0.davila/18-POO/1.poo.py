from utils import *

limpiar_consola()

# La POO es una manera de estructurar el codigo 
# un objeto es algo que representa algo del problema que estamos queriendo modelar

# diccionario = {}
# print(type(diccionario))

class Personaje:
    """  
    __init__ 
        -> constructor de la clase
        -> se ejecuta en el momento en que se instancia la clase (momento en el que se construye una referencia a la clase, se construye un nuevo objeto)
    [self] 
        -> hace referencia a la zona de memoria donde fue construido el objeto (instancia de la clase)
        -> todo lo que asocie a self esta siendo guardado en la zona de memoria de este objeto en particular
        -> hace referencia al objeto construido a partir de la clase (instancia de la clase)
    """
    nivel_educativo_minimo = "secundario"
    def __init__(self, id, nombre="", apellido="", edad="") -> None:
        print("desde el constructor")
        self.id = id # crea un atributo id y le asigna el valor id.
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def get_nombre_completo(self):
        # print(f"{nombre} {nombre}")
        return f"{self.nombre} {self.apellido}"
    def get_nivel_educativo(self):
        return self.nivel_educativo_minimo

separador()

gacela = Personaje(1, "Hugo", "Maradona", 37)
# print(gacela.nombre)
print(gacela.get_nombre_completo())
gacela.nombre = "Diego"
# print(gacela.nombre)
# print(gacela.self)
print(gacela.get_nombre_completo())
print(gacela.get_nivel_educativo())

separador()

arquero = Personaje(2, "Sergio", "Romero", 36)
print(type(arquero))
print(arquero.get_nombre_completo())
print(arquero.get_nivel_educativo())

separador()

print(Personaje)
print(Personaje.nivel_educativo_minimo)
# print(Personaje.nombre)

separador()

Personaje.nivel_educativo_minimo = "Universitario"
print(Personaje.nivel_educativo_minimo)
print(gacela.get_nivel_educativo())
print(arquero.get_nivel_educativo())

separador()

gacela.nivel_educativo_minimo= "No terminó la primaria"
print(arquero.get_nivel_educativo())
print(gacela.get_nivel_educativo())
print(Personaje.nivel_educativo_minimo)