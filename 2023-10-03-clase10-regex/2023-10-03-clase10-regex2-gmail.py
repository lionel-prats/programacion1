import os
if os.name in ["ce", "nt", "dos"]: # windows
    os.system("cls")
else: # linux o mac
    os.system("clear")

import re 

emails = [
    "pepito@example.com",
    "al_final@fantasi.net",
    "estees@myemail.org",
    "fake@kakemail.com",
    "maria@dreammail.io",
    "peppapig@truchomail.com",
    "super_chino@caramelos.com",
    "batman@gmail.com",
    "teletubbies@chubipapilla.com",
    "t_800@skynet.com",
    "robin@gmail.com",
    "batman_contacto@baticueva.com",
    "dos_caras@yahoo.com",
    "el-jodas@yahoo.com",
    "yo_soy_batman@yosoybatman.com",
    "nosoyunmail",
    "Hola",
    "h@la@chau.net",
]

regex = r'^[a-zA-Z.-_]+@gmail.(com)$'






def validar_correo(correo):
    return re.match(regex, correo)

correos_filtrados = list(filter(validar_correo, emails))

for correo in correos_filtrados:
    print(correo)