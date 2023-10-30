import sys
import re  
from Estadistica import Estadistica
from Equipo import Equipo

class Menu:
    def __init__(self, lista_jugadores, lista_jugadores_destacados, menus) -> None:
        self.lista_jugadores = lista_jugadores
        self.lista_jugadores_destacados = lista_jugadores_destacados
        self.menus = menus

    def loop(self, menu: str):
        """
        """
        inicio = True
        limpiar_consola()
        while True:
            opcion_seleccionada = -1
            while opcion_seleccionada == -1:

                opcion_seleccionada = self.menu_principal(self.lista_jugadores, self.lista_jugadores_destacados, menu) 
                
                limpiar_consola()
            
            if opcion_seleccionada in ("c", "C"): 
                print("Hasta la próxima", "\n")
                sys.exit()         

            if opcion_seleccionada in ("v", "V"): 
                self.loop("menu_1") 
                
            if menu not in ["menu_2", "menu_3"]:
                match opcion_seleccionada:
                    case "a" | "A":
                        self.loop("menu_2")
                    case "b" | "B":
                        self.loop("menu_3")

            if menu == "menu_2":
                regex = r"^\d+$" # 1 o mas digitos
                dato_valido = self.validar_dato(regex, opcion_seleccionada)
                if dato_valido:
                    cantidad_jugadores = len(self.lista_jugadores)
                    if int(opcion_seleccionada) in range(1, cantidad_jugadores + 1):
                        limpiar_consola() 
                        indice_jugador = int(opcion_seleccionada) - 1
                        jugador = self.lista_jugadores[indice_jugador] 
                        print(f"Estadísticas de {jugador.get('nombre')} (nro. de orden {opcion_seleccionada})", "\n")
                        for k, v in jugador.get("estadisticas").items():
                            print(f"{k.replace('_', ' ')}: {v}")
                    else:
                        print(f"\"{opcion_seleccionada}\" no es un índice válido. Intente nuevamente.")
                else:
                    print(f"\"{opcion_seleccionada}\" no es un índice válido. Intente nuevamente.")
            if(menu == "menu_3"):
                if(len(opcion_seleccionada) < 3):
                    print_de_salida = "Debe ingresar al menos 3 caracteres."
                else:
                    print_de_salida = f"Logros de jugadores encontrados con \"{opcion_seleccionada}\":\n\n"
                    coincidencia = False
                    for jugador in self.lista_jugadores:
                        nombre_jugador = jugador.get("nombre")
                        if re.search(opcion_seleccionada, nombre_jugador, re.IGNORECASE):
                            coincidencia = True
                            print_de_salida += f"{jugador.get('nombre')}:\n"
                            for logro in jugador.get("logros"): 
                                print_de_salida += f"- {logro}\n"
                            print_de_salida += "\n"
                    print_de_salida = print_de_salida[:-2]
                    if not coincidencia:
                        print_de_salida = f"No hay coincidencias con \"{opcion_seleccionada}\". Intenta nuevamente."            
                print(print_de_salida)
            self.separador()

    def menu_principal(self, lista_jugadores, lista_jugadores_destacados, menu: str):
        """ 
        """
        self.imprimir_menu(lista_jugadores, lista_jugadores_destacados, menu)
        opcion_ingresada = input("Opción: ")
        # validacion = re.search(r"^[a-cA-C]{1}$", opcion_ingresada)
        validacion = re.search(self.menus[menu]["regex"], opcion_ingresada)
        if not validacion:
            return -1 
        return opcion_ingresada

    def imprimir_menu(self, lista_jugadores, lista_jugadores_destacados, menu: str):

        listado_jugadores_formateado = self.formatear_lista_jugadores(lista_jugadores)
        listado_jugadores_destacados_formateado = self.formatear_lista_jugadores_destacados(lista_jugadores_destacados, "rebotes_totales")

        print("Listado de jugadores:", "\n")
        print(listado_jugadores_formateado)
        self.separador()
        print(listado_jugadores_destacados_formateado)
        self.separador()
        print("Menú de opciones:")
        print(self.menus[menu]["menu"])

    def separador(self):
        print("\n-----\n")

    def formatear_lista_jugadores(self, lista_jugadores):
        render_lista_jugadores = ""
        for jugador in lista_jugadores:
            nro_orden = lista_jugadores.index(jugador) + 1
            nombre = jugador.get('nombre')
            posicion = jugador.get('posicion')
            puntos_por_partido = f"{jugador.get('estadisticas').get('promedio_puntos_por_partido')} puntos por partido"
            render_lista_jugadores += f"{nro_orden}. {nombre} - {posicion} || {puntos_por_partido}\n"
        return render_lista_jugadores[:-1]

    def formatear_lista_jugadores_destacados(self, lista_jugadores_destacados, key):
        texto = f"Jugador/es con la mayor cantidad de {key.replace('_', ' ')}:\n"
        for jugador in lista_jugadores_destacados:
            nombre = jugador.get("nombre")
            dato = jugador.get("estadisticas").get(key)
            texto += f"{lista_jugadores_destacados.index(jugador) + 1}. {nombre}: {dato}\n"
        return(texto[:-1])

    def validar_dato(self, regex, dato, search = False):
        if search and re.search(regex, dato, re.IGNORECASE):
            return True
        elif re.match(regex, dato):
            return True
        return False 

    def limpiar_consola():
        import os
        if os.name in ["ce", "nt", "dos"]: # windows
            os.system("cls")
        else: # linux o mac
            os.system("clear")

def limpiar_consola():
    import os
    if os.name in ["ce", "nt", "dos"]: # windows
        os.system("cls")
    else: # linux o mac
        os.system("clear")
        
if __name__ == "__main__":

    menus = {
        "menu_1": {
            "menu": """
A Estadísticas completas de un jugador (2 - 3)
B Logros de un jugador (4 - 6)
C Salir
                    """, 
            "regex": r"^[a-cA-C]{1}$",
            "opciones_menu": ("a","A","b","B","c","C")
        },
        "menu_2": {
            "menu": """
Ingresa "V" para volver al menú anterior,
ingresa "C" para salir
o igresa el nro. de orden de un jugador para ver todas sus estadísticas
                    """, 
            "regex": r"^[CcVv]{1}$",
            "regex": r".*",
            "opciones_menu": ("C","c","V","v")
        },
        "menu_3": {
            "menu": """
Ingresa "V" para volver al menú anterior,
ingresa "C" para salir
o ingresa el nombre y/o apellido de un jugador para ver todos sus logros (al menos 3 caracteres)
                    """, 
            "regex": r"^[CcVv]{1}$",
            "regex": r".*",
            "opciones_menu": ("C","c","V","v")
        }
    }
    

    equipo = Equipo()
    lista_jugadores = equipo.get_lista_jugadores()
    lista_jugadores_destacados_rebotes_totales = equipo.get_jugadores_destacados("rebotes_totales")

    menu = Menu(lista_jugadores, lista_jugadores_destacados_rebotes_totales, menus)

    menu.loop("menu_1")
    