# class PuertaException(Exception):
#     pass

# def inicializar_lavado():
#     flag_puerta_abierta = True
#     if not flag_puerta_abierta:
#         raise PuertaException()

# nro1_str = input("Ingrese un numero: ")
# nro2_str = input("Ingrese un numero: ")

# # Flujo e control de excepciones
# try:
#     inicializar_lavado()

nro_str = input("Ingrese un numero: ")
nro_int = int(nro_str)

try:
    if nro_int == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    else:
        resultado = nro_int/10 
except ZeroDivisionError as division_por_cero:
    print(division_por_cero)

else:
    print("El resultado es: ", resultado)