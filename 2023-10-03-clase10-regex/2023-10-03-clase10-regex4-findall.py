import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

import re 

# texto = " uno 1 dos 2 tres 3 cuatro"
# print(re.findall(" ", texto))
# print(re.findall(" [0-9]+", texto))
# print(re.findall("[a-z ]+", texto))

texto = "Mejores comidas de Italia y qué comer en Italia. #comerenitalia #comidaitaliana #viajeaitalia"

patron = " italia "
patron = " italia[. ]{1}"
lista_palabras_italia = re.findall(patron, texto, re.IGNORECASE)
print(lista_palabras_italia)