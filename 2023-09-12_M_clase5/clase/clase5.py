# FUNCIONES LAMBDA

# -> las funciones lambda o anonimas son una manera abreviada de escribir una funcion simple. 
# -> segun la documentacion de python "... son solo una notacion abreviada si eres demasiado perezoso para definir una funcion"

print ("\n---------- FUNCIONES LAMBDA ----------\n")

def sumar(a, b):
    return a + b

sumar_lambda = lambda a, b: a + b

print(sumar_lambda(10, 8))

# con lambda es comun usar metodos y funciones propias de python como map y filter

# -----------------------------------------------------------------------------------------------

# OPERADORES TERNARIOS (mas conocidos en python como EXPRESIONES CONDICIONALES) 

print ("\n---------- OPERADORES TERNARIOS ----------\n")

mayor = lambda a, b: f"{a}.1 es mayor" if a > b else f"{b}.2 es mayor"
print(mayor(26,26)) 

# if 8 > 4 ? True : False
print(True if 8 > 9 else False)

input_nombre_usuario = "None"
input_nombre_usuario = None
print(input_nombre_usuario if input_nombre_usuario else "No está definido")

# -----------------------------------------------------------------------------------------------

# LISTAS ANIDADAS

print ("\n---------- LISTAS ANIDADAS ----------\n")

matriz = [["Marty", "McFly"], ["Emmett", "Brown"]]

print(matriz[0][0])
print(matriz[0][1])
print(matriz[1][0])
print(matriz[1][1])

print ("----------------------------------------")

for linea in matriz:
    for columna in linea: 
        print(columna)

# -----------------------------------------------------------------------------------------------

# LISTAS ANIDADAS

print ("\n---------- COPIAR LISTAS ----------\n")

array_1 = ["lio", "marian", "rodri"]
array_2 = array_1 # "a array_2 le pusimos un puntero de array_1"

array_1[2] = "saia"

print(array_1)
print(array_2)

array_2[1] = "luigi"
print(array_1)
print(array_2)


# lista_2 es referencia de lista_1, cualquier cambio en una variable en cualquier momento de la ejecuicion impactara en la otra

print("-----")

# EXISTEN 2 TIPOS DE COPIAS POSIBLES: 

# 1) SUPERFICIAL (SHALLOW COPY) -> solamente se copian las referencias a los elementos vontenidos en el objeto
lista_1 = [["Marty", "McFly"], "Emmett", "Biff"]
lista_2 = lista_1.copy() # "a lista_2 le pusimos un puntero de lista_1"

print("shallow copy")
lista_1[0][1] = "Carlos"
print(lista_1)
print(lista_2)
lista_2[0][0] = "Pinocho"
print(lista_1)
print(lista_2)

# 2) PROFUNDA (DEEP COPY) -> si el objeto contiene subojetos estos se copian recursivamente
from copy import deepcopy
lista_3 = [["Marty", "McFly"], "Emmett", "Biff"]
lista_4 = deepcopy(lista_3)

print("deep copy")
lista_3[0][1] = "Carlos"
print(lista_3)
print(lista_4)
lista_4[0][0] = "Pinocho"
print(lista_3)
print(lista_4)

# -----------------------------------------------------------------------------------------------

# VACIAR LISTAS Y DICCIONARIOS

print ("\n---------- VACIAR LISTAS Y DICCIONARIOS ----------\n")

lista_con_elementos = ["monos", "en", "verano"]
print(lista_con_elementos)
puntero_a_lista_con_elementos = lista_con_elementos
print("puntero vvv")
print(puntero_a_lista_con_elementos)
puntero_a_lista_con_elementos[0] = ["gacelas"]
puntero_a_lista_con_elementos[1] = ["sin"]
puntero_a_lista_con_elementos[2] = ["sueter"]
print(lista_con_elementos)
lista_con_elementos.clear()
print(puntero_a_lista_con_elementos)

print("-----")

diccionario_con_elementos =\
{
    "nombre": "peter",
    "apellido": "capusotto"
}
print(diccionario_con_elementos)
diccionario_con_elementos.clear()
print(diccionario_con_elementos)

# -----------------------------------------------------------------------------------------------

# insert()

# el metodo insert() añade un elemento en una posicion o indice determinado 

print ("\n---------- insert() ----------\n")

lista_insert = ["la", "vuelta", "mundo"]
lista_insert.insert(2, ["al", "carajo"])
print(lista_insert)

# -----------------------------------------------------------------------------------------------

# extend()

# el metodo extend() permite añadir una lista a la lista inicial 

print ("\n---------- extend() ----------\n")

lista_extend = ["la", "vuelta", "mundo"]
lista_extend.insert(2, "al")
lista_extend.extend(["en", 80, "dias"])
print(lista_extend)

# -----------------------------------------------------------------------------------------------

# pop()

# el metodo pop() elimina y retorna el elemento ubicado en el indice pasado por parametro; por defecto elimina el ultimo elemento 

print ("\n---------- pop() ----------\n")

lista_pop = ["la", "gran", "bestia", "pop"]
print(lista_pop)
pop_por_defecto = lista_pop.pop()
print(f"por defecto se elimino el ultimo elemento, \"{pop_por_defecto}\"")
print(lista_pop)
pop_especifico = lista_pop.pop(1)
print(f"esta vez le pasamos el indice 1, asi que se elimino \"{pop_especifico}\"")
print(lista_pop)

# -----------------------------------------------------------------------------------------------

# remove()

# el metodo remove() recibe como argumento un objeto y lo borra de la lista

print ("\n---------- remove() ----------\n")

lista_remove = ["la", "isla", "siniestra"]
print(lista_remove)
lista_remove.remove("isla")
print(lista_remove)

# -----------------------------------------------------------------------------------------------

# index()

# el metodo index() recibe como parametro un objeto y devuelve el indice de su primera aparicion

print ("\n---------- index() ----------\n")

lista_index = ["la", "gran", "isla", "siniestra", "y", "la", "isla", "soleada"]
print(lista_index)
print(lista_index.index("isla"))

# -----------------------------------------------------------------------------------------------

# enumerate()

# si necesitamos un indice acompañadp con la lista, que tome valores desde 0 hasta n-1

print ("\n---------- enumerate() ----------\n")

lista_enumerate = ["git init", "git add", "git commit", "git push", "git fetch", "git merge"]
for i, el in enumerate(lista_enumerate):
    print(i, el)

# -----------------------------------------------------------------------------------------------

# zip()

# permite iterar multiples listas a la vez
# por cada iteracion retorna una tupla con el elemento n de cada lista 

print ("\n---------- zip() ----------\n")

lista_nombres = ["lionel", "luis", "rafa"]
lista_edades = [38, 32, 23]
lista_equipos = ["all-boys", "river", "caracas"]

for nombre, edad, equipo in zip(lista_nombres, lista_edades, lista_equipos):
    print(f"{nombre} tiene {edad} años y es hincha de {equipo}")

# -----------------------------------------------------------------------------------------------

# map()

# la funcion map() pasa como parametros a una funcion a cada uno de los elementos de una lista, dando como resultado una nueva lista formada por los elementos que dicha funcion retorna

print ("\n---------- map() ----------\n")

lista_map = ["lionel", "luis", "rafa"]
iterable = map(str.upper, lista_map)
print(iterable)
print(f"print por consola de un iterable -> {iterable}")
for i, el in enumerate(iterable):
    print(i, el)

iterable_casteado_como_lista = list(map(str.upper, lista_map))

print(iterable_casteado_como_lista)

def multiplicar_por_2(numero):
    return numero * 2 

lista_numeros_map = [3, 6, 9]
print(lista_numeros_map)
for i, el in enumerate(map(multiplicar_por_2, lista_numeros_map)):
    print(i, el)

# -----------------------------------------------------------------------------------------------

# filter()

# la funcion filter() filtra una lista de elementos para los que una funcion devuelve True

print ("\n---------- filter() ----------\n")

lista_filter = [17, 71, 18]

iterable_filter = filter(lambda elemento: elemento >= 18, lista_filter)
print(iterable_filter)

print("primera iteracion del iterable vvv")
for i, el in enumerate(iterable_filter):
    print(i, el)
print("segunda iteracion del iterable vvv")
for i, el in enumerate(iterable_filter):
    print(i, el)
print("casteo a lista del iterable vvv")
print(list(iterable_filter))

# -----------------------------------------------------------------------------------------------

# reduce()

# la funcion reduce() se utiliza principalmente para llevar a cabo un calculo acumulativo sobre una lista de valores y retornar el resultado, está incluiida en el módulo functools

print ("\n---------- reduce() ----------\n")

lista_reduce = [17, 71, 18]
from functools import reduce
suma = reduce(lambda x, y: x + y, lista_reduce)
print(lista_reduce)
print(suma)

# -----------------------------------------------------------------------------------------------

# shuffle(lista)

# es un metodo del modulo random que se utiliza para mezclar una lista

print ("\n---------- shuffle(lista) ----------\n")

from random import shuffle
lista_shuffle = [1, 2, 3, 4, 5]
shuffle(lista_shuffle)
print(lista_shuffle)

# -----------------------------------------------------------------------------------------------

# sort()

# el metodo sort() ordena los elementos de menor a mayor por defecto

print ("\n---------- sort() -> de menor a mayor (defecto) ----------\n")

lista_sort_nombres = ["Coca", "Moca", "Boca"]
lista_sort_numeros = [40, 50, 30]
lista_sort_numeros_float = [40.999999, 50.000000001, 30]
lista_sort_numeros_string = ["3", "299", "1999"]

lista_sort_nombres.sort()
lista_sort_numeros.sort()
lista_sort_numeros_float.sort()
lista_sort_numeros_string.sort()

print(lista_sort_nombres)
print(lista_sort_numeros)
print(lista_sort_numeros_float)
print(lista_sort_numeros_string)

print ("\n---------- sort(revert = True) -> de mayor a menor ----------\n")

lista_sort_nombres.sort(reverse = True)
lista_sort_numeros.sort(reverse = True)
lista_sort_numeros_float.sort(reverse = True)
lista_sort_numeros_string.sort(reverse = True)

print(lista_sort_nombres)
print(lista_sort_numeros)
print(lista_sort_numeros_float)
print(lista_sort_numeros_string)

print ("\n---------- sort(key = ...) ----------\n")

# tiene un parametro key para especificar una funcion que se llamara por cada elemento de la lista y su retorno se utilizara para hacer las comparaciones 

lista_sort_key = ["independiente", "boca", "huracan"]

lista_sort_key.sort(key = len)
# el parametro es key, y le estamos asignando el len (largo) de los elementos
# le estamos diciendo "ordená la lista por el largo de las palabras" 
# por defecto la va a ordenar de forma ASC

print(lista_sort_key)

lista_sort_key_2 = ["independiente", "boca", "huracan"]
lista_sort_key_2.sort()
print(lista_sort_key_2)

# buscar metodos para listas
# buscar metodos para diccionarios
# buscar metodos para strings
# buscar building functions (funciones ya armadas para facilitarnos cosas dentro del lenguaje)