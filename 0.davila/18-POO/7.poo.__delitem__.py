from utils import *
limpiar_consola()

class Personaje:
   def __init__(self, presidente, ministro_economia, periodista, ayudante) -> None:
      self._lista= [presidente, ministro_economia, periodista, ayudante]

   # aparentemente este metodo permite realizar algunas acciones propieas de las listas sobre algun atributo del tipo list dentro de la clase (la buena practica seria utilizarlo para eliminar algun item de un atributo del tipo list)
   def __delitem__(self, index):
      # return index
      # return del self._lista[index]
      # return len(self._lista)
      return self._lista.append("Mengueche")
      return self._lista.pop(index)

personaje = Personaje("Fernandez", 'Massa', 'Feinmann', "Carlitos")
print(personaje._lista)

# esta sintaxis ejecuta el metodo magico __delitem__ (si no esta declarado en la clase explota el programa)
del personaje[1] 
print(personaje._lista)

separador()

lista = ["juan", "maro"]
print("maro" in lista)
print("cabe" in lista)
del lista[0]
print(lista)

separador()