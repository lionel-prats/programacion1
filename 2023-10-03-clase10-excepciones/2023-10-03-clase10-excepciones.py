import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

def castear_dato_a_float(dato):
    """  
    recibe un dato y si es posible lo retorna casteado a float\n 
    [dato] -> dato a intentar castear a float\n
    return -> (float) dato casteado a float (si es posible), (bool) False si no se puede castear 
    """
    if type(dato) == int or type(dato) == str and dato.replace(".", "", 1).isdigit():
        return float(dato)
    elif type(dato) == float:
        return dato
    return False


# print(-10%10) # 10 * -1 = -10, al -10 [0]
# print(-9%10)  # 10 * -1 = -10, al -10 [0]
# print(-8%10)  # 10 * -1 = -10, al -10 [0]
# print(-7%10)  # 10 * -1 = -10, al -10 [0]
# print(-6%10)  # 10 * -1 = -10, al -10 [0]
# print(-5%10)  # 10 * -1 = -10, al -10 [0]
# print(-4%10)  # 10 * -1 = -10, al -10 [0] 
# print(-3%10)  # 10 * -1 = -10, al -10 [0]
# print(-2%10)  # 10 * -1 = -10, al -10 [0]
# print(-1%10)  # 10 * -1 = -10, al -10 [0]





# dividendo_str = input("Ingrese un numero: ")

# input("Presione una tecla para continuar...")
# diccionario = {"nombre": "Marta"}
# print(diccionario["apellido"])

# lista = [1,2,3]
# print(lista[10])

# print(4/0)

# documentacion oficial - excepciones incorporadas en el lenguaje
# https://docs.python.org/3/library/exceptions.html

# ---------------------------------------------------

# contador = 5
# try:
#     for i in range (contador, -5, -1):
#         print(10/i)
# except:
#     print("No se puede dividir por cero")

# ---------------------------------------------------

# try:
#     dividendo_str = input("Ingrese un numero: ")
#     dividendo_int = int(dividendo_str)
#     resultado = 100 / dividendo_int
#     print(f"El resultado es: {resultado}")
# except:
#     print("ocurrio un error")

# print("estoy fuera del try")

# ---------------------------------------------------

# try:
#     dividendo_str = input("Ingrese un numero: ")
#     dividendo_int = int(dividendo_str)
#     resultado = 100 / dividendo_int
#     print(f"El resultado es: {resultado}")
# except Exception as mi_error:
#     print("")
#     print(mi_error)
#     print(type(mi_error))
# print("estoy fuera del try")

# ---------------------------------------------------

try:
    dividendo_str = input("Ingrese un numero: ")
    dividendo_int = int(dividendo_str)
    resultado = 100 / dividendo_int
    print(f"El resultado es: {resultado}")
except ValueError as error_1:
    print("El valor ingresado no se puede convertir a entero")
    print("Tipo de error: ", error_1)
except ZeroDivisionError as error_2:
    print("No se puede dividir por cero")
    print("Tipo de error: ", error_2)
except Exception as error_3:
    print("No se que falló pero algo salió mal")
    print("Tipo de error: ", error_3)

print("\nestoy fuera del try")