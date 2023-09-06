def sumar(a, b):
    return a + b

lista_programadores = [
    {
        "apellido": "Carvalhosa",
        "nombre": "Luis",
        "edad": 32
    },
    {
        "apellido": "Gonzalo",
        "nombre": "Mariano",
        "edad": 32
    },
    {
        "apellido": "Hernandez",
        "nombre": "Rafael",
        "edad": 23
    },
    {
        "apellido": "Mila",
        "nombre": "Leonardo",
        "edad": 34
    },
    {
        "apellido": "Prats",
        "nombre": "Lionel",
        "edad": 38
    },
    {
        "apellido": "Sosa",
        "nombre": "Alex",
        "edad": 30
    },
    {
        "apellido": "Turcowicz",
        "nombre": "Rodrigo",
        "edad": 35
    },
    {
        "apellido": "Wagner",
        "nombre": "Tomás",
        "edad": 31
    }
]

for programador in lista_programadores:
    print(f"{programador['nombre']} {programador['apellido']}")

tupla_equipos = ("boca", "independiente", "racing", "river", "san lorenzo")

a = range(0, 9)
a = list(a)
a[5] = "Gabriel"
for elemento in a:
    print(elemento)

print(type(lista_programadores))
print(type(lista_programadores[5]))
print(type(lista_programadores[5]["nombre"]))
print(type(lista_programadores[5]["edad"]))
print(type(sumar))
print(type(tupla_equipos))
print(type(a))
print(a)

print(lista_programadores[4].keys())
print(lista_programadores[4].values())
print(lista_programadores[4].get("nacionalidad", "No se ha cargado el dato"))