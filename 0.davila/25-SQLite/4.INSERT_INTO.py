import sqlite3

with sqlite3.connect("25-SQLite/bd_btf.db") as conexion:
    try:
        keys = "nombre, apellido, anio"
        values1 = ("Marty", "MacFly", "1968")
        values2 = ("Lionel", "Prats", "1985")

        conexion.execute(f"insert into personajes({keys}) values(?, ?, ?)", values1)
        conexion.execute(f"insert into personajes({keys}) values(?, ?, ?)", values2)
        
        conexion.commit() # hace el insert en la tabla

        print("insert realizado correctamente")
    except:
        print("Error")