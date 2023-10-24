import sqlite3

# si el archivo .db no existe, automaticamente se crea en el path especificado
with sqlite3.connect("25-SQLite/bd_btf.db") as conexion:
    try:
        sentencia = """ create table personajes(
                            id integer primary key autoincrement,
                            nombre text,
                            apellido text,
                            anio real
                        )
                    """
        conexion.execute(sentencia)
        print("Se creo la tabla personajes")
    except sqlite3.OperationalError:
        print("La tabla personajes ya existe")