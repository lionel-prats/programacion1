import re 

"""  
las RegExp tienen que ser analizadas segun donde las queremos implementar
las regex se basan en ASCII (clave para implementar intervalos)
^ acento circunflexo
([^xxx]) -> circunflexo adentro de los corchetes es negacion del conjunto
(^[xxx]) -> circunflexo adentro de los parentesis pero fuera de los corchetes es que la regEx empieza con ese conjunto
([xxx]+) tiene que haber, al menos, 1 ocurrencia
"""

# cualquier texto(al menos 1 caracter) + "||" + cualquier texto(al menos 1 caracter) + "#" + cualquier numero(al menos 1 digito)
# [a-z]+ -> con "+" indicamos que debe haber al menos 1 ocurrencia 
regex_patron = "([a-zA-Z ]+)\|\|([a-zA-Z ]+)#([0-9]+)"

# datetime -> 2023/10/19 03:28:15
regex_datetime_crudo = "[0-9]{4}/[0-9]{2}/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}"
# lo podemos parsear como queramos
regex_datetime_parseado_1 = "([0-9]{4})/([0-9]{2})/([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2})"
regex_datetime_parseado_2 = "([0-9]{4}/[0-9]{2}/[0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})"

# +/- nros de 4 digitos
# [-] -> al no especificar cantidad de ocurrencias, decimos que "-" puede estar como no estar
regex_nro = "[-][0-9]{4}" 

# nros entre 2 y 4 digitos
regex_nro = "[-][0-9]{2,4}" 

dni = "[0-9]{7,9}" 
if(re.match(dni, "a31367577a")):
    print("es DNI")
else:
    print("dato invalido")