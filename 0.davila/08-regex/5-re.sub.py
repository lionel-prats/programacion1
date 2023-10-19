import re 
from utils import *
limpiar_consola()

# Borra signos de puntuacion
result = re.sub(r'[.,:]', '', "Buen día. Hoy diremos: nada por aquí, nada por allá")  
print(result)

# Repmpaza abc por xyz
result = re.sub('abc',  'xyz', "abc")   
print(result)

# Eliminalos espacios duplicados
result = re.sub(r'\s+', ' ',   "Hola           mundo        de          hoy")
print("Hola           mundo        de          hoy")
print(result)