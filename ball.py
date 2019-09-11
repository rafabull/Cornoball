import pyglet
import pymunk
from pymunk import pyglet_util
import math

#class Ball(pyglet.sprite.Sprite):
class Bola:
    def __init__(self, mass, radius, xB, yB):
        self.circle_moment = pymunk.moment_for_circle(mass, 0, radius)
        self.circle_body = pymunk.Body(mass, self.circle_moment)
        self.circle_body.position = xB, yB
        self.circle_shape = pymunk.Circle(self.circle_body, radius)
        self.circle_shape.elasticity = 0.9
        self.circle_shape.friction = 0.9
        self.y = 0

    '''def __init__(self, *args, **kwargs):
        super(Bola, self).__init__(*args, **kwargs)'''

    #atualizando a posicao da bola
    def update(self, dt):
        self.y = self.circle_body.position[1]




