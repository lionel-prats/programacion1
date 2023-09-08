# 14) Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.

def diccionario_numeros(lista_de_numeros: list) -> dict:
    minimo = None
    maximo = None
    total = 0
    for numero in lista_de_numeros:
        
        if not minimo:
            minimo = numero
            maximo = numero
        elif numero < minimo:
            minimo = numero
        elif numero > maximo:
            maximo = numero

        total += numero

    promedio = total / len(lista_de_numeros)

    return {
        "minimo": minimo,
        "maximo": maximo,
        "promedio": promedio
    }

lista_de_numeros = [5, 3, 8, 45, 6]
resultado = diccionario_numeros(lista_de_numeros)

print(lista_de_numeros)
print(resultado)
print(f"minimo: {resultado['minimo']}")
print(f"maximo: {resultado['maximo']}")
print(f"promedio: {resultado['promedio']}")
