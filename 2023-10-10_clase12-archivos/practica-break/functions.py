from lista_heroes import lista_heroes

def crear_csv(path: str, modo: str, lista: list) -> None:
    with open(path, modo) as archivo_heroes:
        pass
        texto = ''
        campos = True

        for heroe in lista:
            
            primer_campo_encabezado = True
            if campos:
                for key in heroe.keys():
                    if primer_campo_encabezado:
                        texto += f'{key}'
                        primer_campo_encabezado = False
                    else:
                        texto += f',{key}'
                campos = False
                texto += '\n'
            
            # primer_campo = True
            # for valor in heroe.values():
            #     if primer_campo:
            #         texto += f'{valor}'
            #         primer_campo = False
            #     else:
            #         texto += f',{valor}'
            # texto += '\n'
        # print(texto)
        archivo_heroes.write(texto)

# ROOT_DIR = r".\2023-10-10_clase12\practica-break"
# ruta_archivo = f'{ROOT_DIR}\\heroes.csv'
ruta_archivo = r'C:\Users\User\Desktop\utn\cuatrimestre1\programacion_1\2023-10-10_clase12-archivos\practica-break\heroes.csv'



crear_csv(ruta_archivo, "w", lista_heroes)