import pygame as pg

class SurfaceManager:

    # no tiene constructor porque no vamos a necesitar instanciarla (solo queremos acceder a sus metodos estaticos)

    @staticmethod # (metodo estatico - puedo invocarlo desde fuera de la clase, sin tener que instanciar la clase)
    def get_surface_from_spritesheet(img_path: str, cols: int, rows: int, step = 1, flip: bool = False)-> list[pg.surface.Surface]:
        sprites_list = list()
        surface_img = pg.image.load(img_path)
        frame_width = int(surface_img.get_width()/cols) # 32 (ej)
        frame_height = int(surface_img.get_height()/rows) # 50 (ej)

        for row in range(rows):
            for column in range(0, cols, step):
                pass
                x_axis = column * frame_width # 0 32
                y_axis = row * frame_height # 0 0

                frame_surface = surface_img.subsurface(x_axis, y_axis, frame_width, frame_height)

                if flip:
                    frame_surface = pg.transform.flip(frame_surface, True, False)
            
            sprites_list.append(frame_surface)

        return sprites_list