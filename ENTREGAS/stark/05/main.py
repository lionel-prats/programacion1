""" 
Alumno: Lionel Prats 
DNI: 31367577
División: 1H
Nro. legajo: 115678
Stark 05
"""
# IMPORTANTE: para que la creacion de archivos funcione correctamente hay que crear la carpeta /csv en la raiz del proyecto

from biblioteca_stark_05 import(leer_archivo, stark_marvel_app_5)

if __name__ == "__main__":
    lista_heroes = leer_archivo("data_stark.json")
    stark_marvel_app_5(lista_heroes)

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/ENTREGAS/primer_parcial/
# python main.py

"""  
Windods + H dictado automatico
Windods + Alt + R grabacion automatico
Windods + G para ver las grabaciones
"""