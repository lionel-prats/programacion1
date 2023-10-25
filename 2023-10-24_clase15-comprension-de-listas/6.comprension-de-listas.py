def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")    
def separador():
    print("\n---------------\n")

limpiar_consola()

lista_personas = [
  {"nombre": "Ignacio", "edad": 38},
  {"nombre": "Sergio", "edad": 39},
  {"nombre": "Alba", "edad": 35},
  {"nombre": "Luis", "edad": 18},
  {"nombre": "Emiliano", "edad": 28},
  {"nombre": "Damian", "edad": 19},
  {"nombre": "Laura", "edad": 33}
]

lista_iniciales_1 = []
for persona in lista_personas:
    if persona.get("nombre")[0].lower() in "aeiou":
        lista_iniciales_1.append(persona.get("nombre"))
print(lista_iniciales_1)

# def formatear_diccionario(diccionario, claves):
#     nuevo_diccionario = [{clave: persona[clave] for clave in claves} for persona in diccionario]
#     return nuevo_diccionario
# claves_a_seleccionar = ["nombre", "edad"]
# print(formatear_diccionario(lista_personas, claves_a_seleccionar))

lista_iniciales_2 = [persona.get("nombre") for persona in lista_personas 
                     if persona.get("nombre")[0].lower() in "aeiou"]
print(lista_iniciales_2)