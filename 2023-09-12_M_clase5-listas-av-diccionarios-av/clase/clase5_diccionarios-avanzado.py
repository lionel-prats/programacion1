# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/2023-09-12_M_clase5/clase
# python clase5_diccionarios-avanzado.py

import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")
# -----------------------------------------------------------------------------------------------

# diccionario anidado

print ("\n---------- DICCIONARIOS ANIDADOS ----------\n")

diccionario = {
    'name' : 'Marty',
    'addr': {
        'number': 9303,
        'street':'Lyon Drive'
    }
}
print(diccionario['addr']['number'], diccionario['addr']['street'])

# -----------------------------------------------------------------------------------------------

# recorrer diccionarios

print ("\n---------- RECORRER DICCIONARIOS ----------\n")

diccionario = {
    'name' : 'Marty', 
    'edad' : 18
}
for clave in diccionario:
    print(clave, diccionario[clave])

# -----------------------------------------------------------------------------------------------

# copiar diccionarios

print ("\n---------- COPIAR DICCIONARIOS - shallow copy ----------\n")

diccionario = {
    'edad' : 18,
    'name' : ['Marty','Mcfly']
}
diccionario_copia = diccionario.copy()
diccionario_copia = diccionario.copy()
diccionario['name'][0] = "Lionel"
diccionario['name'][1] = "Prats"
diccionario['edad'] = 38
print(diccionario)
print(diccionario_copia)
# en este ejemplo, en diccionario_copia, se modifica el subobjeto de typo list asociado a "name", pero no el asiciado a "edad"

# -----------------------------------------------------------------------------------------------

# copiar diccionarios

print ("\n---------- COPIAR DICCIONARIOS - deep copy ----------\n")

from copy import deepcopy
diccionario_deep = {
    'edad' : 18,
    'name' : ['Marty','Mcfly']
}
diccionario_deep_copia = deepcopy(diccionario_deep)
diccionario_deep['name'][0] = "Lionel"
diccionario_deep['name'][1] = "Prats"
diccionario_deep['edad'] = 38
print(diccionario_deep)
print(diccionario_deep_copia)

# -----------------------------------------------------------------------------------------------

# get()
print ("\n---------- get() ----------\n")

diccionario = {
    'name' : 'Marty', 
    'edad' : 18
}
print(diccionario.get('name','NO NAME')) # Marty

print(diccionario.get('nombre','NO NAME')) # NO NAME
# print(diccionario["nombre"]) # ERROR

# -----------------------------------------------------------------------------------------------

# keys()

print ("\n---------- keys() ----------\n")

# El método keys() devuelve una lista con todas las claves del diccionario.

diccionario = {
    'name' : 'Marty', 
    'edad' : 18
}
print(list(diccionario.keys()))
# ['name', 'edad']

# -----------------------------------------------------------------------------------------------

# values()

print ("\n---------- values() ----------\n")

# El método values() devuelve una lista con todos los valores del diccionario.

diccionario = {
    'name' : 'Marty', 
    'edad' : 18
}
print(diccionario.values())
print(list(diccionario.values()))
# ['Marty', 18]

# -----------------------------------------------------------------------------------------------

# items()

print ("\n---------- items() ----------\n")

# El método items() devuelve una lista con las claves y valores del diccionario. Si se convierte en lista se puede acceder utilizando el índice.

diccionario = {
    'name' : 'Marty', 
    'edad' : 18
}
print(diccionario.items())
print(list(diccionario.items()))
# [('name', 'Marty'), ('edad', 18)]

# -----------------------------------------------------------------------------------------------

# pop()

print ("\n---------- pop() ----------\n")

# El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Dará un error si se intenta eliminar una key que no existe. Pero se puede pasar un segundo parámetro que es el valor a devolver si la key no se ha encontrado. En este caso si no se encuentra no habría error.

diccionario = {
    'name' : 'Marty', 
    'edad' : 18
}

edad_eliminada = diccionario.pop('edad')
print(edad_eliminada) # 18
print(diccionario) # {'name': 'Marty'}

# apellido_eliminado = diccionario.pop('apellido')
# print(apellido_eliminado) # ERROR
apellido_eliminado = diccionario.pop('apellido', "NO EXISTE CLAVE 'APELLIDO'") # ERROR
print(apellido_eliminado) # NO EXISTE CLAVE 'APELLIDO'

# -----------------------------------------------------------------------------------------------

# update()

print ("\n---------- update() ----------\n")

# El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.

diccionario = {
    'name' : 'Lionel', 
    'apellido' : 'Pratz', 
    'edad' : 29
}

diccionario.update({
    'apellido' : 'Prats',
    'nacionalidad' : 'Argentino',
    'edad' : 38
})
print(diccionario)

# -----------------------------------------------------------------------------------------------

# clear()

print ("\n---------- clear() ----------\n")

# El método clear() elimina todo el contenido del diccionario.

diccionario_con_elementos =\
{
    "nombre": "peter",
    "apellido": "capusotto"
}
print(diccionario_con_elementos)
diccionario_con_elementos.clear()
print(diccionario_con_elementos)