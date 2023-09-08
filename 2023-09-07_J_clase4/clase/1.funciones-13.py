# 13) Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.

def diccionario_palabras(lista_de_palabras: list) -> dict:
    diccionario_palabras = {}
    for palabra in lista_de_palabras:
        diccionario_palabras[palabra] = len(palabra)
    return diccionario_palabras

lista_de_palabras = ["murcielago", "ornitorrinco", "auto", "pepsi"]
resultado = diccionario_palabras(lista_de_palabras)

for k, v in resultado.items():
    print(f"La palabra {k} tiene {v} caracteres.")
