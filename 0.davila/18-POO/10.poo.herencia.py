from utils import *
limpiar_consola()

class Persona:
   def __init__(self, id) -> None:
      self.id = id 
   def mostrar(self):
      print(self.id)

   def get_id(self):
      return self.id

class Personaje(Persona):
   def __init__(self, nombre = "") -> None:

      # invoco al constructor de la clase de la que heredo (Persona)
      super().__init__(88)
      
      self.__nombre = nombre
   @property
   def nombre(self):
      return self.__nombre

   def mostrar(self):
      print(self.id * 2)

   # redefino el metodo ya heredado en la clase padre para retornar el id como float en vez de como int
   def get_id(self):
      return float(super().get_id())

aux = Personaje("Lionel") 

print(aux)
print(aux.nombre)
print(aux.id)
aux.mostrar()

separador()

print(aux.get_id())

separador()

   