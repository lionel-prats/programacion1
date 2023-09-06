""" 
9) Crea un diccionario que contenga las capitales de los países de América del Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
"""

capitales_america_del_sur = {
    "argentina": "buenos aires",
    "bolivia": "la paz",
    "brasil": "brasilia",
    "chile": "santiago de chile",
    "colombia": "bogota",
    "ecuador": "quito",
    "paraguay": "asuncion",
    "peru": "lima",
    "uruguay": "montevideo",
    "venezuela": "caracas"
}

nombre_pais= input("Ingrese el nombre de un pais de america del sur: ").lower()

# capital = capitales_america_del_sur.get(nombre_pais, "El pais ingresado no corresponde America del Sur")
# mensaje = f"\nPais ingresado: {nombre_pais.capitalize()}\nCapital: {capital.capitalize()}" 
# print(mensaje)


# while not nombre_pais in capitales_america_del_sur.keys():
#     mensaje = f"El pais {}"
# else:
#     pass


# if not capitales_america_del_sur.keys(nombre_pais.lower()):
#     mensaje = "El pais ingresado no corresponde America del Sur"
# else:
#     capital = capitales_america_del_sur.get(nombre_pais)
#     mensaje = f"\nPais ingresado: {nombre_pais.capitalize()}\nCapital: {capital.capitalize()}"
# print(mensaje)