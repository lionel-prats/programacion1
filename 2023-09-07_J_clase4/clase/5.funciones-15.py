# 15) Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género. 

def inventario_peliculas_2(peliculas: list[dict]) ->dict:
    inventario_peliculas = {}
    if peliculas:
        for pelicula in peliculas:
            genero = pelicula.get("genero", "sin_genero").lower()
            inventario_peliculas[genero] = inventario_peliculas.get(genero, 0) + 1
    return inventario_peliculas

"""
lista_de_peliculas = [
    {
        "titulo": "Gladiador",
        "genero": "Acción",
        "director": "Ridley Scott"
    },
    {
        "titulo": "Transformers 1",
        "genero": "Ciencia Ficción",
        "director": "Michael Bay"
    },
    {
        "titulo": "300",
        "genero": "Acción",
        "director": "Zack Snyder"
    },
    {
        "titulo": "Matrix",
        "genero": "Ciencia ficción",
        "director": "Lilly Wachowski"
    },
    {
        "titulo": "Forest Gump",
        "genero": "Drama",
        "director": "Robert Zemeckis"
    },
    {
        "titulo": "Jobs",
        "genero": "Biografía",
        "director": "Joshua Michael Stern"
    },
    {
        "titulo": "Zoolander",
        "genero": "Comedia",
        "director": "Ben Stiller"
    },
    {
        "titulo": "El señor de los anillos",
        "genero": "Aventura",
        "director": "Peter Jackson"
    },
    {
        "titulo": "El juego del miedo",
        "genero": "Terror",
        "director": "James Wan"
    },
    {
        "titulo": "Jurasic Park",
        "genero": "Aventura",
        "director": " Steven Spielberg"
    },
    {
        "titulo": "Oppenheimer",
        "genero": "Histórica",
        "director": "Christopher Nolan"
    },
    {
        "titulo": "El código enigma",
        "genero": "Drama",
        "director": "Morten Tyldum"
    },
    {
        "titulo": "El código Da Vinci",
        "genero": "Misterio",
        "director": "Ron Howard"
    }   
]
"""

lista_de_peliculas = [
    {
        "titulo": "Transformers 1",
        "genero": "Ciencia Ficción",
        "director": "Michael Bay"
    },
    {
        "titulo": "300",
        "genero": "",
        "director": "Zack Snyder"
    },
    {
        "titulo": "Jurasic Park",
        "genero": "Aventura",
        "director": " Steven Spielberg"
    },
    {
        "titulo": "Matrix",
        "genero": "Ciencia Ficción",
        "director": "Lilly Wachowski"
    },
    {
        "titulo": "Gladiador",
        "genero": "Acción",
        "director": "Ridley Scott"
    },
    {
        "titulo": "Forest Gump",
        "genero": "Drama",
        "director": "Robert Zemeckis"
    },
    {
        "titulo": "Jobs",
        "genero": "",
        "director": "Joshua Michael Stern"
    },
    {
        "titulo": "El código Da Vinci",
        "genero": "Misterio",
        "director": "Ron Howard"
    },  
    {
        "titulo": "Zoolander",
        "genero": "Comedia",
        "director": "Ben Stiller"
    },
    {
        "titulo": "El señor de los anillos",
        "genero": "Comedia",
        "director": "Peter Jackson"
    },
    {
        "titulo": "El juego del miedo",
        "genero": "Terror",
        "director": "James Wan"
    },
    {
        "titulo": "Oppenheimer",
        "genero": "Comedia",
        "director": "Christopher Nolan"
    },
    {
        "titulo": "El código enigma",
        "genero": "Drama",
        "director": "Morten Tyldum"
    }
]

for pelicula in lista_de_peliculas:
    print(pelicula["genero"])

resultado_2 = inventario_peliculas_2(lista_de_peliculas)

print(resultado_2)