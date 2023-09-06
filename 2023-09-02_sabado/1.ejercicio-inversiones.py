# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertir
Las posibles franquicias son las siguientes: 
# Apple,
# Dunkin Donnuts, 
# Ikea o 
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

El programa tendra precargado un menú de opciones en el que debemos programar lo siguiente

1.Cargar voto, está opción agregara a las listas un voto en especifico pidiendo los siguientes datos
    nombre del encuestado.
    edad (no menor a 18)
    genero (Masculino - Femenino - Otro)
    voto (APPLE, DUNKIN, IKEA, TACO)   
    
2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 anios.
3-Genero que predomina en la empresa.
4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su genero no sea Femenino y su edad se encuentre 
entre los 18 y 30.
5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
6-Salir
'''

# lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "Jose", "Marta",
#             "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]
lista_nombres = []

# lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
#             32, 22, 29, 27, 19, 49, 27, 22, 29, 27]
lista_edades = []

# Femenino = 8
# masculino = 9
# otro = 3
# lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", 
#                 "Otro", "Marta", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", 
#                 "Femenino", "Masculino", "Femenino"]
# lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Otro", 
#                 "Otro", "Marta", "Masculino", "Otro", "Femenino", "Otro", "Femenino", "Otro", "Masculino", 
#                 "Femenino", "Masculino", "Femenino"]
lista_generos = []

# lista_votos = ["APPLE", "DUNKIN", "IKEA", "APPLE", "TACO", "DUNKIN", "TACO", "APPLE", "TACO", "APPLE",
#             "IKEA", "APPLE", "DUNKIN", "DUNKIN", "APPLE", "IKEA", "APPLE", "DUNKIN", "IKEA", "TACO"]    
lista_votos = []    

#PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS

while True:

    print("\n1-Cargar Voto\n2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 anios\n3-Genero que predomina en la empresa.\n4-Porcentaje de empleados que no votaron por APPLE, siempre y cuando su genero no sea Femenino y su edad se encuentre entre los 18 y 30.\n5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados\n6-Salir")

    opcion = input("Ingrese una opción 1-6: ")
    while opcion == None or not opcion.isdigit() or not (int(opcion) >= 1 and int(opcion) <=6):
        opcion = input("Error - opcion incorrecta - Vuelva a ingresar una opción 1-6: ")
    opcion = int(opcion)

    # Carga de datos
    """ 
    1.Cargar voto, está opción agregara a las listas un voto en especifico pidiendo los siguientes datos
    nombre del encuestado.
    edad (no menor a 18)
    genero (Masculino - Femenino - Otro)
    voto (APPLE, DUNKIN, IKEA, TACO)    
    """
    if opcion == 1:

        while True:

            # ingreso el nombre del encuestado
            nombre = input("Nombre (solo letras): ") 
            while not nombre.isalpha(): # "".isalpha() == False -> (solo admite caracteres alfabeticos)
                nombre = input("Error - Debe ingresar un nombre válido: ")
            lista_nombres.append(nombre)
            
            # ingreso el nombre del encuestado
            edad = input("Edad (a partir de 18 años): ") 
            while not edad.isdigit() or int(edad) < 18: 
                edad = input("Error - Debe ingresar una edad válida (a partir de 18 años): ")
            lista_edades.append(int(edad))
            
            # ingreso el genero del encuestado
            genero = input("Género ('Femenino' | 'Masculino' | 'Otro'): ") 
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = input("Error - género incorrecto. Ingrese nuevamente el género ('Femenino' | 'Masculino' | 'Otro'): ")
            lista_generos.append(genero)
            
            # ingreso el voto del encuestado
            """ 
            # Apple,
            # Dunkin Donnuts, 
            # Ikea o 
            # Taco Bell. 
            """
            voto = input("Voto ('APPLE' | 'DUNKIN' | 'IKEA' | 'TACO'): ") 
            while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA" and voto != "TACO":
                voto = input("Error - voto incorrecto. Ingrese nuevamente el voto ('APPLE' | 'DUNKIN' | 'IKEA' | 'TACO'): ")
            lista_votos.append(voto)
            
            # pregunto al usuario si quiere ingresar los datos de un encuestado mas
            continuar = input("Desea continuar ingresando datos? (si | no): ")
            while continuar != "si" and continuar != "no":
                continuar = input("Error - respuesta incorrecta. Desea continuar ingresando datos? (si | no): ")
            if(continuar == "no"):
                break
    
    # 2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 anios.
    elif opcion == 2:
        print("\n")

        total_encuestados = len(lista_nombres)
        if total_encuestados:

            print(lista_nombres)
            print(lista_edades)
            print(lista_generos)
            print(lista_votos)
            print("\n")

            votos_apple_hasta_35 = 0
            for i in range(total_encuestados):
                edad = lista_edades[i]
                voto = lista_votos[i]
                if(voto == "APPLE" and edad <= 35):
                    print(f"Votante = {edad} | {voto}")
                    votos_apple_hasta_35 += 1
            print(f"2- Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 anios: {votos_apple_hasta_35}.\n")
        else:
            print(f"No hay datos para analizar.\n")

        print("\n-------------------------------------------")
            
    # 3-Genero que predomina en la empresa.
    elif opcion == 3:
        
        print("\n")
        total_encuestados = len(lista_nombres)
        if total_encuestados:
            
            print(lista_nombres)
            print(lista_edades)
            print(lista_generos)
            print(lista_votos)
            
            contador_genero_femenino = 0
            contador_genero_masculino = 0
            contador_genero_otro = 0
            for i in range(total_encuestados):
                genero = lista_generos[i]
                match genero:
                    case "Femenino":
                        contador_genero_femenino += 1
                    case "Masculino":
                        contador_genero_masculino += 1
                    case _:
                        contador_genero_otro += 1

            if(contador_genero_femenino > contador_genero_masculino):
                if(contador_genero_femenino > contador_genero_otro):
                    print(f"\n3- Entre los votantes predomina el genero Femenino ({contador_genero_femenino}).")
                elif(contador_genero_otro > contador_genero_femenino):
                    print(f"\n3- Entre los votantes predomina el genero Otro ({contador_genero_otro}).")
                else:
                    print(f"\n3- Entre los votantes predominan los generos Femenino y Otro ({contador_genero_femenino}).")
            elif(contador_genero_masculino > contador_genero_femenino):
                if(contador_genero_masculino > contador_genero_otro):
                    print(f"\n3- Entre los votantes predomina el genero Masculino ({contador_genero_masculino}).")
                elif(contador_genero_otro > contador_genero_masculino):
                    print(f"\n3- Entre los votantes predomina el genero Otro ({contador_genero_otro}).")
                else:
                    print(f"\n3- Entre los votantes predominan los generos Masculino y Otro ({contador_genero_masculino}).")
            else:
                if(contador_genero_otro > contador_genero_femenino):
                    print(f"\n3- Entre los votantes predomina el genero Otro ({contador_genero_otro}).")
                elif(contador_genero_femenino > contador_genero_otro):
                    print(f"\n3- Entre los votantes predominan los generos Femenino y Masculino ({contador_genero_femenino}).")
                else:
                    print(f"\n3- Entre los votantes hay paridad de genero ({contador_genero_femenino}).")
            
            print(f"Femenino = {contador_genero_femenino}")
            print(f"masculino = {contador_genero_masculino}")
            print(f"otro = {contador_genero_otro}")
        else:
            print(f"No hay datos para analizar.\n")

        print("\n-------------------------------------------")

    # 4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su genero no sea Femenino y su edad se encuentre entre los 18 y 30.
    elif opcion == 4:
        
        print("\n")
        total_encuestados = len(lista_nombres)
        if total_encuestados:

            print(lista_nombres)
            print(lista_edades)
            print(lista_generos)
            print(lista_votos)

            votos_no_apple_genmasc_genotro_18_30 = 0
            for i in range(total_encuestados):
                edad = lista_edades[i]
                genero = lista_generos[i]
                voto = lista_votos[i]
                if voto != "APPLE" and genero != "Femenino" and (edad >= 18 and edad <= 35):
                    print(f"Votante = {genero} | {edad} | {voto}")
                    votos_no_apple_genmasc_genotro_18_30 += 1
            porcentaje_votos_no_apple_genmasc_genotro_18_30 = votos_no_apple_genmasc_genotro_18_30 / total_encuestados * 100
            print(f"4- Porcentaje de empleados que no votaron por APPLE, siempre y cuando su genero no sea Femenino y su edad se encuentre entre los 18 y 30 ({votos_no_apple_genmasc_genotro_18_30} de {total_encuestados}): {porcentaje_votos_no_apple_genmasc_genotro_18_30}%.\n")
        else:
            print(f"No hay datos para analizar.\n")

        print("\n-------------------------------------------")

    # 5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados 
    elif opcion == 5:
        print("\n")
        total_encuestados = len(lista_nombres)
        if total_encuestados:

            print(lista_nombres)
            print(lista_edades)
            print(lista_generos)
            print(lista_votos)

            total_edades = 0
            for i in range(total_encuestados):
                total_edades += lista_edades[i]

            edad_promedio = total_edades / total_encuestados
            
            lista_nombres_buscados = []
            lista_edades_buscados = []
            lista_votos_buscados = []
            for i in range(total_encuestados):
                nombre = lista_nombres[i]
                edad = lista_edades[i]
                voto = lista_votos[i]
                if (voto == "IKEA" or voto == "TACO") and edad > edad_promedio:
                    lista_nombres_buscados.append(nombre)  
                    lista_edades_buscados.append(edad)  
                    lista_votos_buscados.append(voto)  
            
            if(len(lista_nombres_buscados)):
                print(f"5- Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados ({edad_promedio:.2f} anios):")
                print("ORDEN | NOMBRE | EDAD | VOTO")
                
                for i in range(len(lista_nombres_buscados)):
                    nombre = lista_nombres_buscados[i]
                    edad = lista_edades_buscados[i]
                    voto = lista_votos_buscados[i]
                    print(f"{i + 1} | {nombre} | {edad} | {voto}")
            else:
                print(f"5- Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados ({edad_promedio:.2f} anios): No existe ningun caso")
        else:
            print(f"5- No hay datos para analizar.\n")
        
        print("\n-------------------------------------------")

    elif opcion == 6:
        print("Adios")
        break
    else:
        print("\nOpcion incorrecta (1-6)\n")