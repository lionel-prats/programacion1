""" 
4) Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
"""

direccion = {
    "nombre_calle": "directorio",
    "altura": "4059",
    "localidad": "caba",
    "codigo_postal": "1407",
    "partido": "caba",
    "provincia": "buenos aires",
}

nombre_calle = direccion.get("nombre_calle", "no hay datos")
altura = direccion.get("altura", "no hay datos")

mensaje = f"\ncalle: {nombre_calle}\naltura: {altura}" 

print(mensaje)