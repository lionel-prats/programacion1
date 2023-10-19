import re 
from utils import *
limpiar_consola()

texto = 'uno 1 dos 2 tres 3 cuatro'

# print(re.split(' ', texto)) 
# print(texto.split(" ")) 
# ['uno', '1', 'dos', '2', 'tres', '3', 'cuatro']

# print(re.split('[0-9]+', texto)) 
# print(re.split('[0-9]', texto)) 
#['uno ', ' dos ', ' tres ', ' cuatro']

# print(re.split('[a-z ]+', texto)) 
#['', '1', '2', '3', '']


bizarrap = "QUEVEDO || BZRP Music Sessions # 52"
# print(re.split("\|{2}|#", bizarrap)) 

fecha = "2023-10-19 03:28:15"
fecha4 = "[\- :]" 
print(re.split(fecha4, fecha)) 

fecha_bla = "2023-10-1\\9 00:00:00"
print(re.split("[\\\]", fecha_bla))
print(re.split(r"[\\]", fecha_bla))