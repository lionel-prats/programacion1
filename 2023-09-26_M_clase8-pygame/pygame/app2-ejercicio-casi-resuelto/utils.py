def formatear_puntaje(puntaje: str) -> str:
    return puntaje.zfill(4)

def formatear_nombre_jugador(nombre: str) -> str:
    return (nombre.strip().upper()).split()[0]