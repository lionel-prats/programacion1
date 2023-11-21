import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
VERDE = (10, 150, 10)
ROJO = (255, 0, 0)
MARRON = (150, 60, 10)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
# print(dir(ventana))
"""  
['__class__', '__copy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_pixels_address', 'blit', 'blits', 'convert', 'convert_alpha', 'copy', 'fill', 'get_abs_offset', 'get_abs_parent', 'get_alpha', 'get_at', 'get_at_mapped', 'get_bitsize', 'get_blendmode', 'get_bounding_rect', 'get_buffer', 'get_bytesize', 'get_clip', 'get_colorkey', 'get_flags', 'get_height', 'get_locked', 'get_locks', 'get_losses', 'get_masks', 'get_offset', 'get_palette', 'get_palette_at', 'get_parent', 'get_pitch', 'get_rect', 'get_shifts', 'get_size', 'get_view', 'get_width', 'lock', 'map_rgb', 'mustlock', 'premul_alpha', 'scroll', 'set_alpha', 'set_at', 'set_clip', 'set_colorkey', 'set_masks', 'set_palette', 'set_palette_at', 'set_shifts', 'subsurface', 'unlock', 'unmap_rgb']
"""

# objeto de la clase Surface
imagen_manzana = pygame.image.load("baldosa_manzana.png").convert_alpha() # <Surface(80x80x32 SW)>
imagen_manzana_rect = imagen_manzana.get_rect()
imagen_manzana_rect.x = 700
imagen_manzana_rect.y = 350

# Datos
personaje_rect = pygame.Rect(400, 200, 50, 50)

manzana = pygame.Surface((50,50))
# print(dir(manzana))
""" 
['__class__', '__copy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_pixels_address', 'blit', 'blits', 'convert', 'convert_alpha', 'copy', 'fill', 'get_abs_offset', 'get_abs_parent', 'get_alpha', 'get_at', 'get_at_mapped', 'get_bitsize', 'get_blendmode', 'get_bounding_rect', 'get_buffer', 'get_bytesize', 'get_clip', 'get_colorkey', 'get_flags', 'get_height', 'get_locked', 'get_locks', 'get_losses', 'get_masks', 'get_offset', 'get_palette', 'get_palette_at', 'get_parent', 'get_pitch', 'get_rect', 'get_shifts', 'get_size', 'get_view', 'get_width', 'lock', 'map_rgb', 'mustlock', 'premul_alpha', 'scroll', 'set_alpha', 'set_at', 'set_clip', 'set_colorkey', 'set_masks', 'set_palette', 'set_palette_at', 'set_shifts', 'subsurface', 'unlock', 'unmap_rgb']
"""
# objeto de la clase Rect, con al ancho y el alto del objeto de la clase Surface manzana
manzana_rect = manzana.get_rect() 



# Bucle principal
jugando = True
while jugando:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Lógica

    imagen_manzana_rect.x += 1
    if imagen_manzana_rect.x > ANCHO:
        imagen_manzana_rect.x = 0 - imagen_manzana_rect.width

    ventana.fill(VERDE)

    pygame.draw.rect(ventana, MARRON, personaje_rect)

    manzana.fill(ROJO)
    ventana.blit(manzana, (600,400))


    ventana.blit(imagen_manzana, imagen_manzana_rect)

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_25_clase_surface
# python clase0.py