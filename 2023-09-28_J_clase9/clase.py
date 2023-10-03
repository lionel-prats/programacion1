"""  
REGEX pildoras informaticas
https://www.youtube.com/watch?v=qpwn3gRtxCo
"""
import re 

texto = [
"NATHY PELUSO||BZRP Music Sessions#36",
"NATHY PELUSO||BZRP Music Sessions#37",
"NATHY PELUSO||BZRP Music Sessions%36",
"NATHY PELUSO||BZRP Music Sessions&&36",
"NATHY PELUSO||BZRP Music Sessions#40",
]

patron_de_busqueda = r".*ndo$"
patron_de_busqueda = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

nombre = ""
while not re.match(patron_de_busqueda, nombre, re.IGNORECASE):
    nombre = input("escriba un nombre valido de solo letras y espacios: ")

print(nombre)
