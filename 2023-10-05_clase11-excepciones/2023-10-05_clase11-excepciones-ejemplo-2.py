nro1_str = input("Ingrese un numero: ")
nro2_str = input("Ingrese un numero: ")

# Flujo e control de excepciones
try:
    nro1_int = int(nro1_str)
    nro2_int = int(nro2_str)
    resultado = nro1_int / nro2_int

# podemos agrupar excepciones
except (ZeroDivisionError, ValueError) as error_cero:
    print("No se puede dividir por cero o no se puede convertir a entero", "Descripcion: {0}".format(error_cero))

except Exception as error_desconocido:
    print("Ocurrio un error desconocido", "Descripcion: {0} - Tipo {1}".format(error_desconocido, type(error_desconocido)))

# Aca vengo si lo que esta dentro del try no genero ningun error
else:
    print("El resultado es: {0}".format(resultado))

# Este bloque se ejecuta siempre
finally:
    pass 

# Flujo normal
print("Fuera del try (despues)")