# Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

def encuentra_palabra_mas_larga_de_la_lista(lista_de_strings):
    palabra_mas_larga = None
    for palabra in lista_de_strings:
        if not palabra_mas_larga or len(palabra_mas_larga) <= len(palabra):
            palabra_mas_larga = palabra 
    return palabra_mas_larga

lista_de_palabras = ["murcielago", "ornitorrinco", "auto", "pepsi"]

palabra_encontrada = encuentra_palabra_mas_larga_de_la_lista(lista_de_palabras)


print(f"Palabra más larga: {palabra_encontrada}")