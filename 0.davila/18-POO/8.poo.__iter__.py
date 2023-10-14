from utils import *
limpiar_consola()

class Personaje:
   def __init__(self, id, nombre, apellido, edad) -> None:
      self.id = id
      self.nombre = nombre
      self._lista= [10, 20, 30, 40, 50]
      # self._lista= [id, nombre, apellido, edad]

   # permite que el objeto sea iterable, lo que habilita a usarlo por ejemplo en bucles tipo for.
   # nos va a dejar hacer que una lista nuestra sea iterable, que nosotros la podamos recorrer
   # en general el __iter__ lo vamos a ver implementado para permitir que desde afuera se pueda recorrer alguna lista de las que nuestro objeto conserva
   def __iter__(self):
      for i in self._lista:
         yield i - 5
         # print(i)
         # yield i
         # yield self._lista[i]
      # for index in range(len(self._lista)):
      #    yield self._lista[index]
     
aux = Personaje(0, 'Marty', 'McFly', 18)

contador = 0

# esta sintaxis ejecuta el metodo magico __iter__ (si no esta declarado en la clase explota el programa)
for elemento in aux:
   print(elemento)

print(aux._lista)