import sqlite3

id = 4
with sqlite3.connect("25-SQLite/bd_btf.db") as conexion:
    sentencia = "DELETE FROM personajes WHERE id = ?"
    cursor = conexion.execute(sentencia, (id,))