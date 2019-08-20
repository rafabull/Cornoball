import pyglet


class Bat(pyglet.sprite.Sprite):

    vel_bat = (1/4 * 29) #1/numero de dts necessarios para ativar ou desativar o bastao
    impx = 200
    impy = 300

    def __init__(self, rot, it, *args, **kwargs):
        super(Bat, self).__init__(*args, **kwargs)
        self.rotation = rot
        self.suportingY = 0.86
        self.suportingX = 0.5
        self.interactX = it
        self.interactY = 1
        self.status = "NORMAL"

    #Funcão para rodar os bastoes
    def update(self, dt):
        if self.status == "PRESS":
            #ativando bastao esquerdo
            if self.rotation > 1 and self.rotation <= 30:
                self.rotation -= self.vel_bat


            # ativando bastao direito
            if self.rotation < -1 and self.rotation >= -30:
                self.rotation += self.vel_bat

        else:
            #desativando bastao esquerdo
            if self.rotation > 0 and self.rotation < 30:
                self.rotation += self.vel_bat


            # desativando bastao direito
            if self.rotation < 0 and self.rotation > -30:
                self.rotation -= self.vel_bat


