from utils import *

limpiar_consola()

# class Empleado:
#     nivel_educativo_minimo = "secundario"
#     def __init__(self, id, nombre="", apellido="", edad="") -> None:
#         self.id = id 
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#     def get_nombre_completo(self):
#         return f"{self.nombre} {self.apellido}"
#     def get_nivel_educativo(self):
#         return self.nivel_educativo_minimo

class Personaje:
    def __init__(self, nombre):
        self.__nombre = nombre
    @property
    def nombre(self):
        print("(desde el metodo get_nombre() retorno el valor del atributo privado __name) ", end="")
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        print("el atributo privado __nombre se setea aca adentro, en set_nombre()")
        self.__nombre = nombre

    # dunder method o metodo magico __str__  
    def __str__(self) -> str:
        return "soy el metodo magico __str__, me ejecuto cada vez que quieren transformar a la instancia de la clase (objeto creado) en string -> print(instancia_clase)"
    # dunder method o metodo magico __len__ -> se ejecuta cada vez que se busca el len() de la instancia de la clase (objeto creado) -> len(instancia_clase)
    def __len__(self) -> int:
        return 15
    # se ejecuta cuando se invoca al objeto de la forma -> aux["algun_valor"] -> es una forma de hacer comportar a nuestro objeto como un diccionario ante el usuario
    def __getitem__(self, index) -> str:
        match index:
            # case "bolainas":
            #     return f"{self.__nombre} (te lo cuento solo porque me pasaste bolainas como argumento)"
            case "nombre":
                return self.__nombre
        return f"El atributo '{index}' no existe en el objeto {self}"
    # se ejecuta cuando se invoca al objeto de la forma -> aux["nombre"] = "Lionel" -> es una forma de hacer comportar a nuestro objeto como un diccionario ante el usuario
    def __setitem__(self, index, valor) -> str:
        match index:
            case "nombre":
                self.__nombre = valor

aux = Personaje("Vero")
separador()
# print(aux)
# separador()
# print(len(aux))
# separador()
# print(aux.nombre)
# print(5, 1, 2, 3, "es", "bolainas", "que", "la", "muerte", aux[("bolainas")])
# print(aux["nombre", "carozo"])
print(aux["nombres"])
print(aux["nombre"])
aux["nombre"] = "Lionel"
print(aux["nombre"])
print(aux.__getitem__("nombre"))
aux.__setitem__("nombre", "dario")
print(aux.__getitem__("nombre"))
separador()