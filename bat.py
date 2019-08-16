import pyglet


class Bat(pyglet.sprite.Sprite):

    def __init__(self, rot, *args, **kwargs):
        super(Bat, self).__init__(*args, **kwargs)
        self.rotation = rot

    #Funcão para rodar os bastoes
    def click(self, rot):
        if self.rotation == 0:
            self.rotation = rot

        elif self.rotation == rot:
            self.rotation = 0

