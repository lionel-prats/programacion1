# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/2023-09-19_M_clase7
# python clase.py

from utils import (limpiar_consola, separador)
limpiar_consola()
print("\n\n")

"""  

"""

print("<ul>\n\t<li>\n\t\t<a>")

print(
"""
<ul>
    <li>
        <a>
            <i class="fas fa-user"/>
        </a>
    </li>
</ul>
"""
)

# ---------- strip() ----------

print("\n----- strip() linea 28 -----\n")
cadena1 = "     Hola      mundo    "
print(cadena1)
print(cadena1.strip())

# ---------- strip()  ----------

print("\n----- strip() linea 35 -----\n")
print(cadena1)
print(cadena1.lstrip())
print(cadena1.rstrip())
print(cadena1.strip())

# ---------- strip()  ----------

list = [17, 5, 10, 8]
print(list)
list.sort()
print(list)

a = "5"
print(id(a))
a = "8"
print(id(a))



def modificar_texto(texto: str) -> str:
    texto = "Chau"
    return texto 

mi_texto = "Hola"

modificar_texto(mi_texto)

print(mi_texto)

def modificar_lista(lista: list) -> list:
    lista[0] = "Chau"
    lista = ["Chau"]
    return lista 

lista = ["Hola"]

modificar_lista(lista)

print(lista)

separador()

print("GARCIA")
print("GARCIA".lower())
print("GARCIA".capitalize())
print("GArcIA".upper())

replace = "Juan Pablo, Juan Ignacio y Juan Perez son hinchas de Boca"
print(replace)
replace = replace.replace("Juan", "Gaston", 2)
print(replace.replace("Gaston", "Juan", 1))

print("ß HoLa".casefold())
print("ñ".casefold())

print("ß".casefold() == "ss")
print("ß".lower() == "ss")

alfabeto_griego = "a;;b;c;d;e;f;g"
print(alfabeto_griego.split(";"))
alfabeto_griego2 = "id=1&name=lionel&surname=prats"
print(alfabeto_griego2.split("&"))
print(alfabeto_griego2)
print("3.14".split("."))
print("3.14".split())
print("3.14".split("4"))

value = "15.6"
if value.replace(".", "", 1).isdigit():
    value = float(value)

print(type(value))

separador()

response = ["124887", "11", "0", "", "-35°11'15\""]
texto = ";"
print(texto.join(response))
print("|".join(response))
print(texto)

separador()

cadena10 = "314"
print(cadena10.zfill(6))
cadena10 = int(cadena10)
cadena10 += 15000
cadena10 = str(cadena10)
print(cadena10.zfill(6))
cadena10 = int(cadena10)
cadena10 += 1000000
cadena10 = str(cadena10)
print(cadena10.zfill(6))

separador()

print(f"'AC010BO' isalpha() ? {'AC010BO'.isalpha()}")
print(f"'Directorio' isalpha() ? {'Directorio'.isalpha()}")
print(f"'Directorio 4059' isalpha() ? {'Directorio 4059'.isalpha()}")

separador()

print(f"'AC010BO' isalnum() ? {'AC010BO'.isalnum()}")
print(f"'Directorio' isalnum() ? {'Directorio'.isalnum()}")
print(f"'Directorio 4059' isalnum() ? {'Directorio 4059'.isalnum()}")

separador()

cadena_20 = "verificacion"
print(cadena_20.count("i"))
print(cadena_20.count("cio"))

separador()

cadena_30 = "Hola Hola Hola"
print(cadena_30.lower().count("hola"))

separador()

cadena_40 = "Hola MUNDO"
print(cadena_40.replace("mundo", "PLANETA"))
print(cadena_40.lower().replace("mundo", "PLANETA"))

separador()

nombre_usuario = "JUAN"
edad_usuario = 35
cadena_50 = "Nombre: {1}, Edad: {0}"
print(cadena_50.format(edad_usuario, nombre_usuario))

separador()

nombre_usuario2 = "Carolina"
edad_usuario2 = 25
print("El usuario es {1} {1} {1} {1} y tiene {0} años".format(edad_usuario2, nombre_usuario2))

separador()

nombre_usuario3 = "Delfina"
edad_usuario3 = 19
print("El usuario es {} y tiene {} años".format(edad_usuario3, nombre_usuario3, "parametro_3"))

separador()

nombre_usuario3 = "Delfina"
edad_usuario3 = 19
print("El usuario es {} y tiene {} años".format(edad_usuario3, nombre_usuario3, "parametro_3"))

separador()

gacela = "Nicanor"
carpincho = 61
print( "El usuario es {nombre} y tiene {edad} años".format(nombre = gacela, edad = carpincho) )

separador()

name = "William"
age = 47
print( f"""
El usuario 
es {name} 
y tiene 
{age} años
""")

separador()

cadena_60 = "supercalifragilisticoespialidoso"
print(f"'{cadena_60}' tiene {len(cadena_60)} caracteres")

separador()

# slice

cadena_70 = "hola como va? hacemos un break, les parece?"
print(cadena_70[0:4])
print(cadena_70[:10000])
print(cadena_70[-4])
print(cadena_70[4:9])
print(len(cadena_70[1:10000]))
print(cadena_70[-4:-8])
print(cadena_70[3:50:4])

for letra in cadena_70:
    print(letra)