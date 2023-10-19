import re 
from utils import *
limpiar_consola()

texto = "QUEVEDOQUEVEDOQUEVEDOQUEVEDOQUEVEDOQUEVEDOQUEVEDOQUEVEDO || BZRP Music Sessions # 50;LFC || BZRP Music Sessions # 52;Los Redondos || BZRP Music Sessions # 77;"

# print(re.findall(r"[a-zA-z ]{1,10} [|]{2} [a-zA-z ]{3,} # [0-9]{2}", texto))
print(re.findall(r"([a-zA-z ]+ [|]{2}) [a-zA-z ]{1,100} # ([0-9]{2})", texto))
