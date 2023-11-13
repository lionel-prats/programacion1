import os
class Auxiliar:
    def limpiar_consola():
        """  
        limpia la consola
        """
        # os.system('cls' if os.name == 'nt' else 'clear')
        if os.name in ["ce", "nt", "dos"]: # windows
            os.system("cls")
        else: # linux o mac
            os.system("clear")