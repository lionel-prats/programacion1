""" 
Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.
"""

info_pelicula = {
    "titulo": "reliquias de la muerte I",
    "director": "utn pirata",
    "anho": "2023"
}

print(info_pelicula.get("titulo", "La clave titulo no existe."))