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
ruta_archivo = f'{ROOT_DIR}heroes.csv'
from data_stark import lista_personajes
# C:\Users\Administrator\Desktop\Python\Python_UTN_LaboI\Archivos
# Archivos

def crear_encabezados(lista_heroes: list, texto: str) -> str:
    for heroe in lista_heroes:
        primer_campo_de_datos = True
        for key in heroe.keys():
            if primer_campo_de_datos:
                texto += f'{key}'
                primer_campo_de_datos = False
            else:
                texto += f',{key}'
        texto += '\n'
        break
    return texto

def crear_datos(lista_heroes: list, texto: str):
    for heroe in lista_heroes:
        primer_campo = True
        for valor in heroe.values():
            if primer_campo:
                texto += f'{valor}'
                primer_campo = False
            else:
                texto += f',{valor}'
        texto += '\n'
    return texto

def crear_csv(path: str, modo: str, lista: list) -> None:
    with open(path, modo) as archivo_heroes:
        texto = ''
        texto = crear_encabezados(lista, texto)
        texto = crear_datos(lista, texto)
            
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
    
if __name__ == '__main__':
    crear_csv(ruta_archivo, 'w', lista_personajes)
    # Cargo el csv original
    lista_nueva_heroes = leer_csv(ruta_archivo, 'r')
    # Creo la ruta destino del archivo que estara filtrado
    OUTPUT_CSV = f'{ROOT_DIR}heroes_F.csv'
    # Filtrar heroinas
    heroinas = list(
        filter(
            lambda heroina: heroina.get("genero", "None") == 'F',
            lista_nueva_heroes
        )
    )
    # Creo el archivo con datos ya filtrados
    crear_csv(OUTPUT_CSV, 'w', heroinas)