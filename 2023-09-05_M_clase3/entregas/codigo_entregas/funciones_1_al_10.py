import math

nro_ejercicio = input("\nNro. de ejercicio a ejecutar (1 - 10): ")
while not nro_ejercicio.isdigit() or not (int(nro_ejercicio) >= 1 and int(nro_ejercicio) <= 10):  
    nro_ejercicio= input("Nro. de ejercicio a ejecutar (1 - 10): ")

match nro_ejercicio: 

    case "1":

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

        print(f"\nEjercicio #6:\n")
        print("""Crear una función que calcule el área de un triángulo.\n Recibe dos parámetros (base y altura) y devuelve el área.\n""")

    case "7":
        
        print(f"\nEjercicio #7:\n")
        print("""Crear una función que calcule el máximo común divisor de dos números.\n Recibe dos parámetros (números) y devuelve el máximo común divisor.\n""")

    case "8":

        print(f"\nEjercicio #8:\n")
        print("""Crear una función que verifique si un número es par o impar.\n Recibe un número como parámetro y devuelve True si es par o False si es impar.\n""")

    case "9":
        
        print(f"\nEjercicio #9:\n")
        print("""Crear una función que cuente la cantidad de veces que aparece un elemento en una lista.\n Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.\n""")

    case _:
        
        print(f"\nEjercicio #10:\n")
        print("""Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.\n""")
































