"""  
la clase Rect nos permite almacenar en los objetos de esta clase las coordenadas y las medidas de rectangulos,
para, por ejemplo, poder dibujarlos en la ventana del juego
"""

from pygame import Rect # importo solo la clase Rect

# objeto de la clase Rect (objeto de pygame para guardar coordenadas rectangulares)
mi_rectangulo = Rect(400, 300, 50, 50)

# print(dir(Rect))
"""  
lista con atriubutos y metodos de la clase Rect
['__bool__', '__class__', '__contains__', '__copy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__safe_for_unpickling__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'bottom', 'bottomleft', 'bottomright', 'center', 'centerx', 'centery', 'clamp', 'clamp_ip', 'clip', 'clipline', 'collidedict', 'collidedictall', 'collidelist', 'collidelistall', 'collideobjects', 'collideobjectsall', 'collidepoint', 'colliderect', 'contains', 'copy', 'fit', 'h', 'height', 'inflate', 'inflate_ip', 'left', 'midbottom', 'midleft', 'midright', 'midtop', 'move', 'move_ip', 'normalize', 'right', 'scale_by', 'scale_by_ip', 'size', 'top', 'topleft', 'topright', 'union', 'union_ip', 'unionall', 'unionall_ip', 'update', 'w', 'width', 'x', 'y']
"""

print(mi_rectangulo) # <rect(400, 300, 50, 50)>
print(mi_rectangulo.x) # 400
print(mi_rectangulo.y) # 300

mi_rectangulo.x += 100
print(mi_rectangulo) # <rect(500, 300, 50, 50)>


mi_rectangulo.width += 10
mi_rectangulo.height += 10
print(mi_rectangulo) # <rect(500, 300, 60, 60)>

otro_rectangulo = Rect(560, 300, 50, 50)

print(mi_rectangulo.colliderect(otro_rectangulo))
mi_rectangulo.x += 5
print(mi_rectangulo.colliderect(otro_rectangulo))

# cd /Users/User/Desktop/utn/cuatrimestre1/programacion_1/0.manuel_gonzalez/nivel_29_pygame/video_20_clase_rect
# python teoria1.py