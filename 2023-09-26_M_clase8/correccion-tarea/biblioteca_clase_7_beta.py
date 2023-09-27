# python biblioteca_clase_7_beta.py
import os
from urllib.parse import urlparse

def limpiar_consola():
    """ 
    ACCION: limpia la consola\n
    PARAMETROS: None\n
    RETURN: None
    """
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
    print("\n\n") 

def separador():
    print("\n\n") 

# 1)
# Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
def convertir_en_mayusculas(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return string.upper()

# 2)
# Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
def convertir_en_minusculas(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return string.lower()

# 3)
# Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
def concatenar_strings(string_1: str, string_2: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    # return f"{string_1} {string_2}"
    return string_1 + " " + string_2
    # return "{0} {1}".format(string_1, string_2)

# 4)
# Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
def calcular_largo_string(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return len(string)

# 5)
# Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
def obtener_cantidad_de_coincidencias(string: str, caracter: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return string.count(caracter)

# 6)
# Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
def buscar_coincidencias(string: str, caracter: str) -> list:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return list(filter(lambda palabra: palabra.find(caracter) != -1, string.split(" ")))

# 7)
# Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
def eliminar_espacios(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return string.strip()
    return string.replace(" ", "")
    return "".join((filter(lambda caracter: caracter != " ", string)))

# 8)
# Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
def obtener_diccionario_datos(nombre: str, apellido: str) -> dict:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return {
        "nombre": eliminar_espacios(nombre).capitalize(),
        "apellido": eliminar_espacios(apellido).capitalize()
    }

limpiar_consola()
respuesta = obtener_diccionario_datos("Lionel", "Prats")
print(respuesta)
separador()

# 9)
# Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
def convertir_lista_de_nombres_en_texto(lista: list[str]) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return "\n".join(lista)

# 10)
# Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
# Por ejemplo Facundo Falcone: f.falcone@utn-fra.com.ar
def generar_email(nombre: str, apellido: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return f"{convertir_en_minusculas(eliminar_espacios(nombre)[0])}.{convertir_en_minusculas(eliminar_espacios(apellido))}@utn-fra.com.ar"

# 11)
# Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
def generar_leyenda(lista: list[str]) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    # print(lista)
    # print(lista[:-1])
    # print(", ".join(lista[:-1]))
    # print(", ".join(lista[:-1]) + " y ")
    # print(", ".join(lista[:-1]) + " y " + lista[-1])
    return ", ".join(lista[:-1]) + " y " + lista[-1]

# 12)
# Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 
def formatear_nro_tarjeta():
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    nro_tarjeta = input("Ingrese los 16 dígitos de su tarjeta: ")
    print("\n")
    if len(nro_tarjeta) != 16:
        return "Cantidad de dígitos incorrecto"
    elif not nro_tarjeta.isdigit():
        return "Solo ingresar dígitos"
    return f"**** **** **** {nro_tarjeta[12:16]}"

# 13)
# Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".
def get_username(url: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return url.split("@")[0]

# 14)
# Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
def obtener_dominio(email: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return email.split(".")[1]

def obtener_dominio_pro(url: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    url_parseada = urlparse(url)
    # print(url_parseada)
    # print(url_parseada.scheme)
    # print(url_parseada.netloc)
    # print(url_parseada.path)
    # print(url_parseada.params)
    # print(url_parseada.query)
    # print(url_parseada.fragment)
    return url_parseada.netloc
    
# 15)
# Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
def filtrar_alfabeticos(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    respuesta = ""
    for caracter in string:
        if caracter.isalpha() or caracter == " ":
            respuesta += caracter
    return respuesta

# 16)
# Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
def obtener_acronimo(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    lista = string.split(" ")
    respuesta = ""
    for palabra in lista:
        respuesta += palabra[0]
    return convertir_en_mayusculas(respuesta)

# 17)
# Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".
def completar_byte(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return string.zfill(8)

# 18)
# Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
def invertir_mayusculas_y_minusculas(string: str) -> str:
    return string.swapcase()

# 19)
# Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
def contar_digitos(cadena: str) -> str:
    cantidad_digitos = sum(1 for caracter in cadena if caracter.isdigit())
    return f"contiene {cantidad_digitos} digito{'' if cantidad_digitos == 1 else 's' }"

# 20)
# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
def formatear_lista_emails(lista: list[str]) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    return ";".join(lista)

# 21)
# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
def obtener_diccionario(string: str) -> str:
    """
    ACCION:\n
    PARAMETROS:\n
    RETURN:\n
    """
    lista = string.split()
    diccionario = {}
    for palabra in lista:
        palabra = convertir_en_minusculas(palabra)
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario
    
