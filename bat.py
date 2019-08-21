import pyglet
import math
import functions

fc = functions.Functions()


class Bat(pyglet.sprite.Sprite):

    vel_bat = (1/4 * 29) #1/numero de dts necessarios para ativar ou desativar o bastao
    impx = 200
    impy = 300

    def __init__(self, rot, it, *args, **kwargs):
        super(Bat, self).__init__(*args, **kwargs)
        self.rotation = rot
        self.bordas = []
        self.listaPixels()

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
                self.listaPixels()

            # ativando bastao direito
            if self.rotation < -1 and self.rotation >= -30:
                self.rotation += self.vel_bat
                self.listaPixels()

        else:
            #desativando bastao esquerdo
            if self.rotation > 0 and self.rotation < 30:
                self.rotation += self.vel_bat
                self.listaPixels()

            # desativando bastao direito
            if self.rotation < 0 and self.rotation > -30:
                self.rotation -= self.vel_bat
                self.listaPixels()

    def listaPixels(self):
        rot = self.rotation
        sentido = fc.sinal(rot)
        for i in range(self.x, (self.x + self.width * sentido + 1), sentido):
            self.bordas.append((i, self.y+(i - self.x)*math.cos(rot)))


