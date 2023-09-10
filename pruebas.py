"""
tengo este diccionario en python
hay alguna forma natuva de obtener el maximo segun edad? 
o la forma mas eficiente de hacerlo?
"""

# personas =\
# [
#     {
#         "nombre": "Lionel",
#         "apellido": "Prats",
#         "edad": "53"
#     },
#     {
#         "nombre": "Sergio",
#         "apellido": "Balestrini",
#         "edad": "53"
#     },
#     {
#         "nombre": "Santiago",
#         "apellido": "Fiorini",
#         "edad": "53"
#     }
# ]

# persona_mayor = max(personas, key = lambda persona: persona["edad"])

# print(persona_mayor)

# print("La persona de mayor edad es:")
# print(f"Nombre: {persona_mayor['nombre']}")
# print(f"Apellido: {persona_mayor['apellido']}")
# print(f"Edad: {persona_mayor['edad']}")

# def listado_mayor_edad():
#     pass

# personas =\
# [
#     {
#         "nombre": "Sionel",
#         "apellido": "PRATS",
#         "edad": "53"
#     },
#     {
#         "nombre": "Sergio",
#         "apellido": "Balestrini",
#         "edad": "55"
#     },
#     {
#         "nombre": "sixntiago",
#         "apellido": "Priorini",
#         "edad": "54"
#     }
# ]

# clave = "apellido"

# max_edad = max(personas, key=lambda persona: persona[clave])[clave]

# # personas_mayores = [persona for persona in personas if persona["edad"] == max_edad]

# print(max_edad)

def formatear(lista, claves_a_formatear):
    for item in lista:
        for clave in claves_a_formatear:
            item[clave] = float(item[clave])
    return lista

personas =\
[
    {
        "nombre": "Sionel",
        "apellido": "PRATS",
        "altura": "55.5",
        "peso": "79"
    },
    {
        "nombre": "Sergio",
        "apellido": "Balestrini",
        "altura": "111.54",
        "peso": "86"
    },
    {
        "nombre": "sixntiago",
        "apellido": "Priorini",
        "altura": "2154.6668",
        "peso": "90"
    }
]

print(personas)
personas = formatear(personas, ["altura", "peso"])
print(personas)

# print(personas)
# for persona in personas:
#     persona["altura"] = float(persona["altura"])
#     persona["peso"] = float(persona["peso"])
# print(personas)