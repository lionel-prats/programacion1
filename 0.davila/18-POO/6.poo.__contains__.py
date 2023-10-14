from utils import *
limpiar_consola()

class Personaje:
   def __init__(self, id, nombre, apellido, edad) -> None:
      self.id = id # crea un atributo id y le asigna el valor id.
      self.nombre = nombre
      self._lista= [id,nombre,apellido,edad]

   def __contains__(self, item):
      # return item
      # return item == self.nombre
      # return 8 * 4 - 10 == 2 * 11
      return item in self._lista

personaje_A = Personaje(0, 'Lionel', 'Prats', 38)

# 1) esta sintaxis ejecuta el metodo magico __contains__ (si no esta declarado en la clase explota el programa)
print("Lionel" in personaje_A) # True
# 2) __contains__ retorna True o False en todos los casos
# 3) la idea es aplicar algun tipo de logica adentro, que se resuelva como True o False

separador()

lista = ["juan", "maro"]
print("maro" in lista)
print("cabe" in lista)