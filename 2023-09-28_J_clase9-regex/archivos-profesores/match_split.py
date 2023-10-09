import re


textos = [
    "NATHY PELUSO||BZRP Music Sessions#36",
    "NATHY PELUSO||BZRP Music Sessions#37",
    "NATHY PELUSO||BZRP Music Sessions%36",
    "NATHY PELUSO||BZRP Music Sessions#3600000",
    "NATHY PELUSO||BZRP Music Sessions#4",
    "NATHY PELUSO||BZRP Music Sessions#"
]

#! EJEMPLO MATCH 01
patron_de_busqueda = '^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{1,2}$'
for texto in textos:
    if re.match(patron_de_busqueda, texto):
        print(texto)


fechas = [
    "2023/08/28 10:00:00 JM",# <- ESTE
    "2023/09/30 20:30:15 JM", 
    "2023/08/28 10:00:00 AM",# <- ESTE
    "2023/12/28 10:00:00 PM",
    "2023/01/28 10:00:00 FM"
]

#! EJEMPLO MATCH 02
patron_busqueda_fecha =\
    '(^2023/[0-1]{1}[^8]{1}/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} (AM|PM)$)'

print('\nPatron fecha AM o PM')
patron_fecha = '[\d]{4}/[\d]{2}/[\d]{2}'
patron_hora = '[0-9]{2}:[0-9]{2}:[0-9]{2}'
patron_tiempo = '(AM|PM)'
patron_completo = f'^{patron_fecha} {patron_hora} {patron_tiempo}$'

for fecha in fechas:
    if re.match(patron_completo, fecha):
        print(fecha)

#! EJEMPLO MATCH 03
patron_fecha_neg = '[\d]{4}/[0-1]{1}[^8]{1}/[0-9]{2}'
patron_fecha_negado = f'^{patron_fecha_neg} {patron_hora} {patron_tiempo}$'

print('\nPatron fecha AM o PM Negando mes 8')
for fecha in fechas:
    if re.match(patron_fecha_negado, fecha):
        print(fecha)

#! EJEMPLO SPLIT

texto = 'uno 1 dos 2 tres 3 cuatro # cinco ! seis'
patron = '[\s]{1}[^a-z]{1}[\s]{1}'

print(re.split(patron, texto))