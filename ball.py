import pyglet
import math

class Ball(pyglet.sprite.Sprite):








    '''GRAVITY_ACC = -1000

    at_ACC = - 100
    x_ACC = 0
    y_ACC = 0
    x_VEL = 0 #ainda n serve pra nd
    y_VEL = 0 #ainda n serve pra nd

    suportX = 0 #define se a variavel esta em um suporte 0 -> reto 1-> não esta
    suportY = 0

    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)

    #atualizando a posicao da bola
    def update(self, dt):
        self.y_VEL = self.y_VEL + (self.GRAVITY_ACC * self.suportY + self.y_ACC)*dt
        self.y = self.y + (self.y_VEL*dt)

        self.x_VEL = self.x_VEL + (self.x_ACC)*dt * self.suportX
        self.x = self.x + (self.x_VEL * dt) * self.suportX'''


    '''def listaPixels(self):
        self.bordas = []
        raio = self.width
        for x in range(int(self.x-raio), int(self.x+raio)):
            self.bordas.append((x, self.y+raio))
            self.bordas.append((x, self.y-raio))'''

