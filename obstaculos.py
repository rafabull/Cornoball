import pymunk
import pyglet
import math

class Circulo:
    def __init__(self, x, y, r):
        self.circulo_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.circulo = pymunk.Circle(self.circulo_body, r)
        self.circulo.body.position = x,y
        self.circulo.color = (255, 0, 0, 255)
        self.circulo.elasticity = 0.98
        self.circulo.friction = 0.6

class Triangulo1:
    def __init__(self, x, y, a):
        self.triangulo1_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.triangulo1 = pymunk.Poly(self.triangulo1_body, ((-a,0),(a*math.sqrt(3)/2,-a),(a*math.sqrt(3)/2,a)))
        self.triangulo1.body.position = x, y
        self.triangulo1.color = (255, 0, 0, 255)
        self.triangulo1.elasticity = 0.98
        self.triangulo1.friction = 0.6

class Triangulo2:
    def __init__(self, x, y, b, h):
        self.triangulo2_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.triangulo2 = pymunk.Poly(self.triangulo2_body, ((0,0),(b,0),(0,h)))
        self.triangulo2.body.position = x,y
        self.triangulo2.color = (255, 0, 0, 255)
        self.triangulo2.elasticity = 0.98
        self.triangulo2.friction = 0.6
