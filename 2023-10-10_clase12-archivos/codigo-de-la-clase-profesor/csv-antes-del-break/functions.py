"""
1 - mostrar en consola los primeros N videos
2 - Exportar lista de videos con mas de 20K vistas. [csv]
3 - Exportar lista de videos de mas de 60 min. [csv]
4 - Exportar datos de video con mas vistas. [txt]
5 - Exportar lista de videos. [csv]
6 - Filtrar y exportar videos de milanesas. [json]
7 - Salir
"""
# py -m pip install -r ./Archivos/requirements.txt
ROOT_DIR = './Archivos/'
# C:\Users\Administrator\Desktop\Python\Python_UTN_LaboI\Archivos
# Archivos
heroes = [
        {
            "nombre": "Howard the Duck",
            "identidad": "Howard (Last name unrevealed)",
            "empresa": "Marvel Comics",
            "altura": "79.349999999999994",
            "peso": "18.449999999999999",
            "genero": "M",
            "color_ojos": "Brown",
            "color_pelo": "Yellow",
            "fuerza": "2",
            "inteligencia": ""
        },
        {
            "nombre": "Rocket Raccoon",
            "identidad": "Rocket Raccoon",
            "empresa": "Marvel Comics",
            "altura": "122.77",
            "peso": "25.73",
            "genero": "M",
            "color_ojos": "Brown",
            "color_pelo": "Brown",
            "fuerza": "5",
            "inteligencia": "average"
        },
        {
            "nombre": "Wolverine",
            "identidad": "Logan",
            "empresa": "Marvel Comics",
            "altura": "160.69999999999999",
            "peso": "135.21000000000001",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Black",
            "fuerza": "35",
            "inteligencia": "good"
        },
        {
            "nombre": "Black Widow",
            "identidad": "Natasha Romanoff",
            "empresa": "Marvel Comics",
            "altura": "170.78999999999999",
            "peso": "59.340000000000003",
            "genero": "F",
            "color_ojos": "Green",
            "color_pelo": "Auburn",
            "fuerza": "15",
            "inteligencia": "good"
        },
        {
            "nombre": "Mystique",
            "identidad": "Raven Darkholme",
            "empresa": "Marvel Comics",
            "altura": "178.65000000000001",
            "peso": "54.960000000000001",
            "genero": "F",
            "color_ojos": "Yellow (without irises)",
            "color_pelo": "Red / Orange",
            "fuerza": "15",
            "inteligencia": "good"
        },
        {
            "nombre": "Spider-Man",
            "identidad": "Peter Parker",
            "empresa": "Marvel Comics",
            "altura": "178.28",
            "peso": "74.25",
            "genero": "M",
            "color_ojos": "Hazel",
            "color_pelo": "Brown",
            "fuerza": "55",
            "inteligencia": "high"
        },
        {
            "nombre": "Storm",
            "identidad": "Ororo Munroe",
            "empresa": "Marvel Comics",
            "altura": "180.72",
            "peso": "57.5",
            "genero": "F",
            "color_ojos": "Blue",
            "color_pelo": "White",
            "fuerza": "10",
            "inteligencia": "good"
        },
        {
            "nombre": "Gamora",
            "identidad": "Gamora Zen Whoberi Ben Titan",
            "empresa": "Marvel Comics",
            "altura": "183.65000000000001",
            "peso": "77.769999999999996",
            "genero": "F",
            "color_ojos": "Yellow",
            "color_pelo": "Black",
            "fuerza": "85",
            "inteligencia": "good"
        },
        {
            "nombre": "Thing",
            "identidad": "Ben Grimm",
            "empresa": "Marvel Comics",
            "altura": "183.55000000000001",
            "peso": "225.41999999999999",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "No Hair",
            "fuerza": "85",
            "inteligencia": "good"
        },
        {
            "nombre": "Thor",
            "identidad": "Thor Odinson",
            "empresa": "Marvel Comics",
            "altura": "198.34999999999999",
            "peso": "288.61000000000001",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Blond",
            "fuerza": "100",
            "inteligencia": "good"
        },
        {
            "nombre": "Colossus",
            "identidad": "Piotr Nikolaievitch Rasputin",
            "empresa": "Marvel Comics",
            "altura": "226.13",
            "peso": "225.52000000000001",
            "genero": "M",
            "color_ojos": "Silver",
            "color_pelo": "Black",
            "fuerza": "85",
            "inteligencia": "good"
        },
        {
            "nombre": "Hulk",
            "identidad": "Bruce Banner",
            "empresa": "Marvel Comics",
            "altura": "244.40000000000001",
            "peso": "630.89999999999998",
            "genero": "M",
            "color_ojos": "Green",
            "color_pelo": "Green",
            "fuerza": "100",
            "inteligencia": "high"
        },
        {
            "nombre": "Groot",
            "identidad": "Groot",
            "empresa": "Marvel Comics",
            "altura": "701.12",
            "peso": "4.8200000000000003",
            "genero": "M",
            "color_ojos": "Yellow",
            "color_pelo": "",
            "fuerza": "85",
            "inteligencia": "good"
        },
        {
            "nombre": "Daredevil",
            "identidad": "Matt Murdock",
            "empresa": "Marvel Comics",
            "altura": "183.68000000000001",
            "peso": "90.450000000000003",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Red",
            "fuerza": "15",
            "inteligencia": "good"
        },
        {
            "nombre": "Nick Fury",
            "identidad": "Nicholas Joseph Fury",
            "empresa": "Marvel Comics",
            "altura": "185.88",
            "peso": "99.280000000000001",
            "genero": "M",
            "color_ojos": "Brown",
            "color_pelo": "Brown / White",
            "fuerza": "15",
            "inteligencia": "good"
        },
        {
            "nombre": "Punisher",
            "identidad": "Frank Castle",
            "empresa": "Marvel Comics",
            "altura": "183.25999999999999",
            "peso": "90.900000000000006",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Black",
            "fuerza": "20",
            "inteligencia": "good"
        },
        {
            "nombre": "Star-Lord",
            "identidad": "Peter Jason Quill",
            "empresa": "Marvel Comics",
            "altura": "188.25",
            "peso": "79.209999999999994",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Blond",
            "fuerza": "20",
            "inteligencia": "good"
        },
        {
            "nombre": "Deadpool",
            "identidad": "Wade Wilson",
            "empresa": "Marvel Comics",
            "altura": "188.0",
            "peso": "95.319999999999993",
            "genero": "M",
            "color_ojos": "Brown",
            "color_pelo": "No Hair",
            "fuerza": "35",
            "inteligencia": "good"
        },
        {
            "nombre": "Captain America",
            "identidad": "Steve Rogers",
            "empresa": "Marvel Comics",
            "altura": "188.00999999999999",
            "peso": "108.94",
            "genero": "M",
            "color_ojos": "blue",
            "color_pelo": "blond",
            "fuerza": "20",
            "inteligencia": "good"
        },
        {
            "nombre": "Ghost Rider",
            "identidad": "Johnny Blaze",
            "empresa": "Marvel Comics",
            "altura": "188.50999999999999",
            "peso": "99.200000000000003",
            "genero": "M",
            "color_ojos": "Red",
            "color_pelo": "No Hair",
            "fuerza": "55",
            "inteligencia": "average"
        },
        {
            "nombre": "Blade",
            "identidad": "Eric Brooks",
            "empresa": "Marvel Comics",
            "altura": "188.44999999999999",
            "peso": "97.400000000000006",
            "genero": "M",
            "color_ojos": "Brown",
            "color_pelo": "Black",
            "fuerza": "30",
            "inteligencia": "good"
        },
        {
            "nombre": "Hawkeye",
            "identidad": "Clint Barton",
            "empresa": "Marvel Comics",
            "altura": "191.00999999999999",
            "peso": "104.93000000000001",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Blond",
            "fuerza": "15",
            "inteligencia": "average"
        },
        {
            "nombre": "Drax the Destroyer",
            "identidad": "Arthur Sampson Douglas",
            "empresa": "Marvel Comics",
            "altura": "193.00999999999999",
            "peso": "306.42000000000002",
            "genero": "M",
            "color_ojos": "Red",
            "color_pelo": "No Hair",
            "fuerza": "80",
            "inteligencia": "average"
        },
        {
            "nombre": "Iron Man",
            "identidad": "Tony Stark",
            "empresa": "Marvel Comics",
            "altura": "198.91",
            "peso": "191.88",
            "genero": "M",
            "color_ojos": "Blue",
            "color_pelo": "Black",
            "fuerza": "85",
            "inteligencia": "high"
        }]


ruta_archivo = f'{ROOT_DIR}heroes.csv'

def crear_csv(path: str, modo: str, lista: list) -> None:
    with open(path, modo) as archivo_heroes:
        texto = ''
        campos = True

        for heroe in lista:
            primer_campo = True
            primer_campo_de_datos = True
            if campos:
                for key in heroe.keys():
                    if primer_campo_de_datos:
                        texto += f'{key}'
                        primer_campo_de_datos = False
                    else:
                        texto += f',{key}'
                campos = False
                texto += '\n'
            
            for valor in heroe.values():
                if primer_campo:
                    texto += f'{valor}'
                    primer_campo = False
                else:
                    texto += f',{valor}'
            texto += '\n'
        print(texto)
        archivo_heroes.write(texto)

def leer_csv(path: str, modo: str) -> list[dict]:
    lista_de_renglones = []
    lista_de_heroes = []

    with open(path, modo) as mi_csv:
        lista_de_renglones = mi_csv.readlines().copy()
        lista_claves = lista_de_renglones[0].replace('\n', '').split(',')

        for linea in lista_de_renglones[1:]:
            lista_datos_de_heroe = linea.replace('\n', '').split(',')
            heroe_actual = {}
            for i in range(len(lista_claves)):
                par_clave_valor = {lista_claves[i] : lista_datos_de_heroe[i]}
                heroe_actual.update(par_clave_valor)
            lista_de_heroes.append(heroe_actual)

    return lista_de_heroes.copy()
    

lista_nueva_heroes = leer_csv(ruta_archivo, 'r')
print(lista_nueva_heroes[:3])