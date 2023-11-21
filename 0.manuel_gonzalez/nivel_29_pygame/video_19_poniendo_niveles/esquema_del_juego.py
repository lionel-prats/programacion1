"""  
ESQUEMA DEL JUEGO ASTEROIDES CON NIVELES
 
while en_juego

    (while en_inicio)

    while en_partida

        (while en_nivel)

        (while en_final)
"""

"""        
en_juego = True
while en_juego:

    num_vidas = 3
    num_nivel = 1

    en_partida = False
    en_inicio = True
    
    while en_inicio:
        pass
        # Evento Entrar: en_partida = True
        
        # Evento Cerrar ventana:
            # en_inicio = False
            # en_juego = False

    while en_partida:

        en_final = False

        # Se crean los asteroides segun el nivel

        en_nivel = True
        while en_nivel:

            # Evento Cerrar ventana:
                # en_nivel = False
                # en_partida = False
                # en_juego = False
            # Eventos Moverse

            
            if #colision:
                num_vidas -= 1
                en_nivel = False
            
            
            if #llegar_arriba:
                num_nivel += 1
                en_nivel = False
            
            if num_vidas == 0:
                en_final = True
            
            if num_nivel > 3:
                en_final = True
            
        while en_final:

            # Evento Cerrar ventana o no jugar mas:
                # en_final = False
                # en_partida  False
                # en_juego = False
            # Evento jugar de nuevo:
                # en_final = False
                # en_partida = False

            
            if # ganado:
                # Mensaje: Se ha ganado
            else:
                # Mensaje: Se ha perdido
"""