from utils import *
limpiar_consola()

# __lt__ permite sobrecargar el operador < (menor que).

class Personaje:
   def __init__(self, id, nombre, apellido, edad) -> None:
      self.id = id 
      self.nombre = nombre
      self._lista= [id, nombre, apellido, edad]
      
   def __lt__(self, item):
     return self.id < item.id

personaje_A = Personaje(1, 'Marty', 'McFly', 18)
personaje_B = Personaje(0, 'Emmet', 'Brown', 54)
print(personaje_A._lista < personaje_B._lista)