import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

# crear una clase
class Usuario: 
    nombre: "Usuario"

alejo = Usuario()
alejo.nombre = "Alejo"

joaco = Usuario()
joaco.nombre = "Joaco"

print(alejo.nombre)
print(joaco.nombre)

class Usuario2:
    nombre = "Valor fijo"
    def saludar(self, saludo):
        print(f"{saludo}{self.nombre}")

alejo = Usuario2()
print(alejo.nombre)
alejo.saludar("Hola soy ")
alejo.nombre = "Alejo"
alejo.saludar("Hola soy ")
