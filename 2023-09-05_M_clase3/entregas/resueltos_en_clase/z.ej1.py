""" 
python z.ej1.py

Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".
"""
import pprint

dias_de_la_semana = {
    "lunes": 1,
    "martes": 2,
    "miercoles": 3,
    "jueves": 4,
    "viernes": 5,
    "horarios_disponibles": {
        "manana": "10-12",
        "tarde": "15-17",
        "noche": "20-21",
        "instructores": ["Graciela", "Mariana", "Pablo"]
    }
}

# dias_de_la_semana["sabado"] = 6
# dias_de_la_semana["domingo"] = 7

# pp = pprint.PrettyPrinter(indent = 1)
# pp.pprint(dias_de_la_semana)

clave_a_buscar = "domingo"

print("\n")
print(dias_de_la_semana.get(clave_a_buscar, f"no se cargo el dia {clave_a_buscar}"))
print("\n")
print(dias_de_la_semana.get("horarios_disponibles"))