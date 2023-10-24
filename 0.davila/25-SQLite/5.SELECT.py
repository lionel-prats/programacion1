import sqlite3

with sqlite3.connect("25-SQLite/bd_btf.db") as conexion:
    cursor = conexion.execute(f"SELECT * FROM personajes")
    for fila in cursor:
        print(fila)