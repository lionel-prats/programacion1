""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Funciones - Ejercicio 1 al 10
"""

import math

def validar_dato(dato:str) -> bool:
    """ 
    valida si el valor recibido es un numero entero (neg, cero o pos)\n
    retorna True si lo es, False en cualquier otro caso
    """
    es_negativo = dato.startswith("-")
    if es_negativo:
        valor_absoluto = dato[1:] 
        if valor_absoluto.isdigit():
            return True
    elif dato.isdigit():
            return True
    return False

nro_ejercicio = input("\nNro. de ejercicio a ejecutar (1 - 10): ")
while not nro_ejercicio.isdigit() or not (int(nro_ejercicio) >= 1 and int(nro_ejercicio) <= 10):  
    nro_ejercicio= input("Nro. de ejercicio a ejecutar (1 - 10): ")

match nro_ejercicio: 

    case "1":

        # Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

        # def validar_dato(dato:str) -> bool:
        #     """ 
        #     valida si el valor recibido es un numero entero (neg, cero o pos)\n
        #     retorna True si lo es, False en cualquier otro caso
        #     """
        #     es_negativo = dato.startswith("-")
        #     if es_negativo:
        #         valor_absoluto = dato[1:] 
        #         if valor_absoluto.isdigit():
        #             return True
        #     elif dato.isdigit():
        #             return True
        #     return False

        def convertidor_celcius_fahrenheit(grados_celcius:float) -> float:
            """ 
            Convierte grados Celcius en grados Fahrenheit\n 
            recibe un valor en grados Celcius\n 
            retorna el equivalente en grados Fahrenheit
            """
            fahrenheit = (grados_celcius * 1.8) + 32 # formula -> f = (c * 1.8) + 32
            return fahrenheit 
    
        print(f"\nEjercicio #1:\n")
        print("""Crear una función que convierta grados Celsius a grados Fahrenheit.\n Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.\n""")

        input_grados_celsius = input("Ingrese una cifra en grados celsius (enteros negativos, cero o enteros positivos): ")
        dato_valido = validar_dato(input_grados_celsius)
        
        while not dato_valido: 
            input_grados_celsius = input("Ingrese una cifra en grados celsius (enteros negativos, cero o enteros positivos): ")
            dato_valido = validar_dato(input_grados_celsius)

        input_grados_celsius = float(input_grados_celsius)

        resultado = convertidor_celcius_fahrenheit(input_grados_celsius)
        
        print(f"\n{input_grados_celsius}°C equivalen a {round(resultado, 2)}°F\n")

    case "2":

        # Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.

        def area_circulo(radio:float) -> float:
            """ 
            calcula el area de un circulo\n 
            recibe el radio del circulo\n 
            retorna el area del circulo correspondiente al radio recibido
            """
            area_circulo = math.pi * (radio ** 2)
            return area_circulo
        
        print(f"\nEjercicio #2:\n")
        print("""Crear una función que calcule el área de un círculo.\n Recibe un parámetro (radio) y devuelve el área del círculo.\n""")

        radio = input("Ingrese el radio de un círculo para calcular su área (enteros positivos): ")
        while not radio.isdigit() or not int(radio) >= 1: 
            radio = input("Ingrese el radio de un círculo para calcular su área (enteros positivos): ")
        
        resultado = area_circulo(int(radio))

        print(f"\nEl área del círculo de radio {radio} es aproximadamente {round(resultado, 2)}\n")
 
    case "3":
        
        # Crear una función que calcule el descuento aplicado a un producto. Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.

        def calcular_descuento(precio:float, precio_con_descuento:float) -> float:
            """ 
            calcula el porcentaje descontado de un precio dado\n 
            recibe el precio original y el precio luego de aplicado el descuento\n 
            retorna el porcentaje equivalente al descuento aplicado 
            """
            porcentaje_descontado = (precio - precio_con_descuento) / precio * 100
            return porcentaje_descontado
        
        print(f"\nEjercicio #3:\n")
        print("""Crear una función que calcule el descuento aplicado a un producto.\n Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.\n""")

        precio_sin_descuento = input("Ingrese el precio sin descuento del producto (sin centavos): ")
        while not precio_sin_descuento.isdigit() or not int(precio_sin_descuento) >= 1: 
            precio_sin_descuento = input("Ingrese el precio sin descuento del producto (sin centavos): ")
        
        precio_con_descuento = input("Ingrese el precio sin descuento del producto (sin centavos): ")
        while not precio_con_descuento.isdigit() or not int(precio_con_descuento) >= 1: 
            precio_con_descuento = input("Ingrese el precio sin descuento del producto (sin centavos): ")
        
        resultado = calcular_descuento(int(precio_sin_descuento), int(precio_con_descuento))

        print(f"\nPrecio sin descuento: ${precio_sin_descuento}")
        print(f"Precio con descuento: ${precio_con_descuento}")
        print(f"Descuento aplicado: {round(resultado, 2)}%\n")

    case "4":

        # Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.

        def calcular_promedio_valores(lista:list) -> float:
            """ 
            calcula el promedio de una serie de valores numericos dados\n 
            recibe una lista de valores numericos\n 
            retorna el promedio de la lista de valores numericos recibidos 
            """
            promedio = sum(lista) / len(lista)
            return promedio

        print(f"\nEjercicio #4:\n")
        print("""Crear una función que calcule el promedio de edad de un grupo de personas.\n Recibe una lista de edades y devuelve el promedio.""")

        lista_edades = []
        while True:
            edad = input("\nIngrese edad para calcular el promedio (de 1 en adelante): ")
            while not edad.isdigit() or not int(edad) >= 1: 
                edad = input("Ingrese edad para calcular el promedio (de 1 en adelante): ")
            lista_edades.append(int(edad))
            finalizar = input("\n¿Quiere finalizar la carga de datos (si-no)?: ")
            while finalizar != "si" and finalizar != "no":
                finalizar = input("\n¿Quiere finalizar la carga de datos (si-no)?: ")
            if finalizar == "si":
                break

        resultado = calcular_promedio_valores(lista_edades)

        lista_edades = list(map(str, lista_edades))
        lista_edades = ", ".join(lista_edades)
        
        print(f"\nListado de edades ingresadas: {lista_edades}")
        print(f"Promedio de edades ingresadas: {resultado}\n")

    case "5":

        # Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.

        def es_numero_primo(numero:int) -> bool:
            """ 
            valida si un numero es primo o no\n 
            recibe un numero\n 
            retorna True si es primo, False si no lo es 
            """
            for i in range(1, numero + 1):
                if i != 1 and i != numero and (numero % i == 0):
                    return False 
            return True

        print(f"\nEjercicio #5:\n")
        print("""Crear una función que determine si un número es primo o no.\n Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.\n""")
        
        while True:
            numero = input("Ingrese un número para saber si es primo o no: ")
            while not numero.isdigit() or not int(numero) >= 1: 
                numero = input("Ingrese un número para saber si es primo o no: ")

            if(es_numero_primo(int(numero))):
                print(f"\n{(numero)} es primo.")
            else:
                print(f"\n{(numero)} no es primo.")

            continuar = input("\n¿Quiere ingresar otro número (si-no)?: ")
            while continuar != "si" and continuar != "no":
                continuar = input("\n¿Quiere ingresar otro número (si-no)?: ")
            if continuar == "no":
                break
            print("\n")

    case "6":

        # Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.

        def area_triangulo(b:float, h:float) -> float:
            """ 
            calcula el area de un triangulo\n 
            recibe base y altura del mismo\n 
            retorna el area del triangulo recibido
            """
            area_triangulo = b * h / 2
            return area_triangulo

        print(f"\nEjercicio #6:\n")
        print("""Crear una función que calcule el área de un triángulo.\n Recibe dos parámetros (base y altura) y devuelve el área.\n""")

        base = input("Ingrese la base de un triángulo para calcular su área (enteros positivos): ")
        while not base.isdigit() or not int(base) >= 1: 
            base = input("Ingrese la base de un triángulo para calcular su área (enteros positivos): ")
        print("\n")

        altura = input("Ingrese la altura de un triángulo para calcular su área (enteros positivos): ")
        while not altura.isdigit() or not int(altura) >= 1: 
            altura = input("Ingrese la altura de un triángulo para calcular su área (enteros positivos): ")
        print("\n")
        
        resultado = area_triangulo(int(base), int(altura))

        print(f"\nBase del triángulo: {round(int(base), 2)}\n")
        print(f"Altura del triángulo: {round(int(altura), 2)}\n")
        print(f"Àrea del triángulo: {round(resultado, 2)}\n")

    case "7":
        
        # Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.

        def obtener_dcm(valor_1:float, valor_2:float) -> float:
            """ 
            retorna el divisor comun mayor entre 2 numeros dados\n 
            recibe 2 numeros 
            """
            divisores_valor_1 = []
            divisores_valor_2 = []
            dcm = None
            for i in range(1, valor_1 + 1):
                if valor_1 % i == 0:
                    divisores_valor_1.append(i)
            for i in range(1, valor_2 + 1):
                if valor_2 % i == 0:
                    divisores_valor_2.append(i)
            for i in divisores_valor_1:
                es_divisor_comun = any(j == i for j in divisores_valor_2)  
                if es_divisor_comun:
                    dcm = i
            return dcm

        print(f"\nEjercicio #7:\n")
        print("""Crear una función que calcule el máximo común divisor de dos números.\n Recibe dos parámetros (números) y devuelve el máximo común divisor.\n""")

        numero_a = input("Ingrese el número A para calcular el DCM (enteros positivos): ")
        while not numero_a.isdigit() or not int(numero_a) >= 1: 
            numero_a = input("Ingrese el número A para calcular el DCM (enteros positivos): ")
        print("\n")
        
        numero_b = input("Ingrese el número B para calcular el DCM (enteros positivos): ")
        while not numero_b.isdigit() or not int(numero_b) >= 1: 
            numero_b = input("Ingrese el número B para calcular el DCM (enteros positivos): ")
        print("\n")

        resultado = obtener_dcm(int(numero_a), int(numero_b))

        print(f"El DCM entre {numero_a} y {numero_b} es {resultado}.\n")     

    case "8":

        # Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.

        def es_numero_par(numero:int) -> bool:
            """ 
            valida si un numero es par o no\n 
            recibe un numero\n 
            retorna True si es par, False si no lo es 
            """
            if numero % 2 == 0:
                return True 
            else:
                return False

        print(f"\nEjercicio #8:\n")
        print("""Crear una función que verifique si un número es par o impar.\n Recibe un número como parámetro y devuelve True si es par o False si es impar.\n""")

        while True:

            numero = input("Ingrese un número para saber si es par o impar (enteros negativos, cero o enteros positivos): ")
            dato_valido = validar_dato(numero)
            
            while not dato_valido: 
                numero = input("Ingrese un número para saber si es par o impar (enteros negativos, cero o enteros positivos): ")
                dato_valido = validar_dato(numero)

            if(es_numero_par(int(numero))):
                print(f"\n{(numero)} es par.")
            else:
                print(f"\n{(numero)} es impar.")

            continuar = input("\n¿Quiere ingresar otro número (si-no)?: ")
            while continuar != "si" and continuar != "no":
                continuar = input("\n¿Quiere ingresar otro número (si-no)?: ")
            if continuar == "no":
                break
            print("\n")

    case "9":
        
        # Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.

        def cantidad_coincidencias(lista:list, elemento) -> int:

            """ 
            retorna la cantidad de apariciones de un elemento en una lista\n 
            recibe una lista y un elemento a buscar 
            """
            cantidad_coincidencias = 0

            for i in lista:
                if i == elemento:
                    cantidad_coincidencias += 1

            return cantidad_coincidencias

        print(f"\nEjercicio #9:\n")
        print("""Crear una función que cuente la cantidad de veces que aparece un elemento en una lista.\n Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.\n""")

        lista = [15, 4, "mono", 4, "mono", True, "mono "]
        
        elemento_a_buscar = "mono "
        
        resultado = cantidad_coincidencias(lista, elemento_a_buscar)

        print("lista de elementos:")
        print(lista)
        print(f"\nElemento a buscar: \"{elemento_a_buscar}\"\n")
        print(f"Coincidencias: {resultado}\n")

    case _:
        
        # Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

        def palabra_mas_larga(lista) -> str:
            """ 
            retorna la palabra de mayor longitud de una lista de palabras dada
            """
            primer_elemento = True
            maxima_longitud = None
            string_mayor_longitud = None

            for i in range(len(lista)):
                if primer_elemento:
                    maxima_longitud = len(lista[i])
                    string_mayor_longitud = lista[i]
                    primer_elemento = False
                elif len(lista[i]) > maxima_longitud:
                    maxima_longitud = len(lista[i])
                    string_mayor_longitud = lista[i]

            return string_mayor_longitud

        print(f"\nEjercicio #10:\n")
        print("""Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.\n""")

        lista = ["baltimore", "fulbito", "lentejas", "superior", "ornalla", "supercalifragilistico", "verde"]
        
        resultado = palabra_mas_larga(lista)

        print("lista de palabras:")
        print(lista)
        print(f"\nPalabra más larga: {resultado}\n")
































