'''
La Programación Orientada a Objetos (POO) en Python es un paradigma de programación que se basa en la creación y manipulación de objetos. Los objetos son instancias de clases, y las clases son plantillas que definen las propiedades (atributos) y comportamientos (métodos) que los objetos pueden tener.

Clases y Objetos: En POO, una clase es un plano o una plantilla que define cómo se crean los objetos. Los objetos son instancias de clases y representan cosas o conceptos del mundo real. Por ejemplo, una clase "Coche" podría tener atributos como "color" y "marca", así como métodos como "arrancar" y "detener".

Atributos: Los atributos son variables que almacenan datos en un objeto. Cada objeto tiene sus propios valores de atributos. Por ejemplo, un objeto de la clase "Coche" podría tener el atributo "color" con el valor "rojo" y el atributo "marca" con el valor "Toyota".

Métodos: Los métodos son funciones que están asociadas a una clase y definen el comportamiento de los objetos de esa clase. Los métodos pueden realizar operaciones y manipulaciones en los atributos de un objeto. Por ejemplo, un método "arrancar" en la clase "Coche" podría cambiar el estado del coche de apagado a encendido.

4 PILARES DE POO ------------------------------------------------

Encapsulación: La encapsulación es un principio que implica ocultar los detalles internos de una clase y exponer solo una interfaz pública. En Python, esto se logra utilizando atributos y métodos públicos, privados (que comienzan con un guion bajo) y protegidos (que comienzan con dos guiones bajos).

Herencia: La herencia permite crear nuevas clases basadas en clases existentes, lo que facilita la reutilización de código. Una subclase hereda atributos y métodos de su clase base (superclase) y puede agregar nuevos atributos y métodos o modificar los existentes.

Polimorfismo: El polimorfismo permite que diferentes clases puedan ser tratadas de manera uniforme si implementan métodos con el mismo nombre. Esto facilita la flexibilidad y la extensibilidad del código.

Abstracción: La abstracción es el proceso de simplificar y generalizar objetos y sus propiedades esenciales. Las clases se diseñan para representar conceptos abstractos del mundo real de manera que se puedan entender fácilmente y utilizar en el código.

En Python, la POO es una parte fundamental del lenguaje y se utiliza para modelar problemas y sistemas complejos de manera más clara y estructurada. Permite organizar el código de una manera más modular y facilita la colaboración en proyectos de desarrollo de software.
'''

# 1. Crear e Instanciar una clase
class Usuario:
    nombre = 'Usuario'


alejo = Usuario()
alejo.nombre = 'Alejo' # modificar valor de una propiedad del objeto

facu = Usuario()
facu.nombre = 'Facu' # la propiedad de los otros objetos se conserva

print(alejo.nombre)
print(facu.nombre)


# 2. Métodos son 'funciones' que pertenecen a un objeto (clase)
# El uso que podriamos darle son alterar o modificar una propiedad, retornar el valor de una propiedad, hacer calculos

class Usuario2:
    nombre = 'Usuario'

    # def saludar(self): # primer argumento palabra reservada self para, dentro del método hacer referencia al objeto
        # print(f'Hola, mi nombre es {self.nombre}')
    
    def saludar(self, saludo:str):
        print(f'{saludo}{self.nombre}')


alejo = Usuario2()
alejo.nombre = 'Alejo'

joaco = Usuario2()
joaco.nombre = 'Joaco'

# alejo.saludar()
# joaco.saludar()

alejo.saludar('Buenas, mi nombre es ')

# -----------------------------------------
# 3. Contexto ¿Que objeto controlo en este momento? self nos permite sin tener que diferenciar los objetos de una clase, definir a que objeto nos estamos refiriendo.

class Tela:
    color = 'Blanco'

    def imprimir_color(self):
        print(f'Color: {self.color}')


tela_roja = Tela()
tela_amarilla = Tela()
tela_roja.color = 'Rojo'
tela_amarilla.color = 'Amarillo'

tela_roja.imprimir_color()
tela_amarilla.imprimir_color()

# ---------------------------------------------------------------
# 4. Constructor

# Los "dunder methods" (double underscore methods) en Python son parte de un conjunto de métodos especiales o mágicos que te permiten personalizar el comportamiento de tus clases y objetos. 
# Estos métodos tienen nombres que comienzan y terminan con doble guion bajo (por ejemplo, __init__, __str__, __len__, etc.).

# __init__ es un método especial de inicialización en Python. Es el constructor de una clase y se llama automáticamente cuando se crea un nuevo objeto de esa clase.
# Su función principal es realizar la inicialización de los atributos de un objeto. Puedes pasarle argumentos que se utilizarán para configurar el estado inicial del objeto.
# Es opcional; si no lo defines en tu clase, Python proporciona un constructor predeterminado vacío.
# El constructor debería ser limpio (inicializar valores y no mucho más)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self, saludo):
        '''
        este método sirve para saludar
        '''
        print(f'{saludo}{self.nombre}')


persona =Persona('Alejo')
persona.saludar('Hola de nuevo ')

# ---------------------------------------------------------------
# 5. Herencia

# La herencia permite crear nuevas clases basadas en clases existentes, lo que facilita la reutilización de código. 
# Una subclase hereda atributos y métodos de su clase base (superclase) y puede agregar nuevos atributos y métodos o modificar los existentes.
# Muchas clases pueden heredar de la misma clase (Padre o Madre).
# También existe el concepto de multiple herencia. (misma clase herede de varias)

class Empleado(Persona):
    salario = 0 # propiedad solamente pertenece a la clase Empleado

    def modificar_salario(self, salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)
    
    def saludar(self): # sobreescribir método de la clase padre
        print(f'Hola, soy {self.nombre} y gano ${self.salario}')


# empleado = Empleado() ejecutar para ver el error de herencia
empleado = Empleado('Facu')
# empleado.saludar() # del método padre antes de definir saludar en Empleado

empleado.modificar_salario(1000)
empleado.ver_salario()

# goku = Persona('Goku')
# goku.ver_salario() # para mostrar que el método no existe en la clase Persona

otro_empleado = Empleado('Goku')
otro_empleado.saludar()

# 5.1 Algunas veces, si queremos conservar las funcionalidades existentes de un método, y sólo extenderlo en la clase hija, podemos utilizar super()
# super() retorna una instancia de la clase padre (a través de la cual podemos llamar métodos de la clase padre).
# Con super() podemos extender los métodos de la clase padre aunque hayamos hecho sobreescritura en las clases hijas.

class Empleador(Persona):

    def saludar(self, saludo):
        # si quisiera extender (en vez de reemplazar o sobreescribir) el método y que se ejecute la clase original(Padre) y agregarles nuevas funcionalidades de la subclase
        super().saludar(saludo)


empleador = Empleador('Elon Musk')
empleador.saludar('Soy el empleador, ')

print(isinstance(empleador, Empleador))
print(isinstance(empleador, Persona))
print(issubclass(Empleador, Persona))
print(issubclass(Persona, Empleador))

# 5.2 Otro Ejemplo utilizando super()

class Pagina:
    def __init__(self, footer):
        self.footer = footer

    def imprimir_footer(self):
        print(self.footer)
    

class Legales(Pagina):

    def imprimir_footer(self):
        super().imprimir_footer()


html = Legales('<footer>Derechos reservados</footer>')
html.imprimir_footer()

# En cuales casos no es recomendable utilizar herencia
# Si en una clase hija nos encontramos removiendo métodos de la clase padre o sobreescribiendo varios métodos, quizás no sea recomendable utilizar herencia.

# ---------------------------------------------------------------
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