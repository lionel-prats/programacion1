import sqlite3

id = 4
with sqlite3.connect("25-SQLite/bd_btf.db") as conexion:
    sentencia = "UPDATE personajes SET nombre = 'jacinto' WHERE id = ?"
    cursor = conexion.execute(sentencia, (id,))
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)