import pyglet
import pymunk
from pymunk import pyglet_util
import math

#class Ball(pyglet.sprite.Sprite):
class Bola:
    def __init__(self, mass, radius):
        self.circle_moment = pymunk.moment_for_circle(mass, 0, radius)
        self.circle_body = pymunk.Body(mass, self.circle_moment)
        self.circle_body.position = 330, 300
        self.circle_shape = pymunk.Circle(self.circle_body, radius)
        self.circle_shape.elasticity = 0.9
        self.circle_shape.friction = 0.9






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

