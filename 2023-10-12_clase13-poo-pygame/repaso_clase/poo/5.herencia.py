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

# 5. Herencia

# La herencia permite crear nuevas clases basadas en clases existentes, lo que facilita la reutilización de código. 
# Una subclase hereda atributos y métodos de su clase base (superclase) y puede agregar nuevos atributos y métodos o modificar los existentes.
# Muchas clases pueden heredar de la misma clase (Padre o Madre).
# También existe el concepto de multiple herencia. (misma clase herede de varias)

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

separador()

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

separador()


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

separador()

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