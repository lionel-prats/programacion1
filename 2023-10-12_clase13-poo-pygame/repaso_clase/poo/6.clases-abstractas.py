def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
def separador():
    print("\n---------------\n")

limpiar_consola()
separador()

# 6. Clases Abstractas

# la clase Entidad hereda de ABC y los métodos atacar y defenderse se marcan como abstractos mediante el decorador @abstractmethod. 
# Esto asegura que cualquier subclase de Entidad debe proporcionar implementaciones concretas para estos métodos.
# NO puedes crear instancias de Entidad directamente, ya que es una clase abstracta. Esto fomenta la creación de subclases con comportamiento específico.

from abc import ABC, abstractmethod
from random import randint

class Entidad(ABC):
    def __init__(self, vida, mana):
        self.vida = vida
        self.mana = mana

    @abstractmethod
    def atacar(self):
        'Ataque base al enemigo'
        pass

    @abstractmethod
    def defenderse(self):
        'Defensa base del jugador'
        pass

class Jugador(Entidad):
    def __init__(self, vida, mana, arma):
        super().__init__(vida, mana)
        self.arma = arma # una clase Arma

    def atacar(self):
        # Implementa la lógica de ataque del jugador aquí
        pass

    def defenderse(self):
        # Implementa la lógica de defensa del jugador aquí
        pass

class Enemigo(Entidad):
    def __init__(self, vida, mana, nombre, nivel):
        super().__init__(vida, mana)
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self):
        # Implementa la lógica de ataque del enemigo aquí
        pass

    def defenderse(self):
        # Implementa la lógica de defensa del enemigo aquí
        pass


class Soldado(Enemigo):
    def __init__(self, nivel):
        super().__init__(200*nivel, 20*nivel, 'Soldado', nivel) # nivel puede ser un num random


class Arquero(Enemigo):
    def __init__(self, nivel):
        super().__init__(100*nivel, 10*nivel, 'Arquero', nivel)

soldado = Soldado(2)
print(soldado.nombre, soldado.vida, soldado.mana, sep='\n')


# Ejemplo Dungeon Crawler
lista_enemigos = [
    Arquero(randint(1, 5)), 
    Soldado(randint(1, 5)), 
    Arquero(randint(1, 5)), 
    Soldado(randint(1, 5))
    ]

for enemigo in lista_enemigos:
    print(enemigo.nombre, enemigo.nivel)
    print(enemigo.vida, enemigo.mana)