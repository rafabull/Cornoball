import pyglet
import pymunk
import numpy

class Impulso:
    def __init__(self):
        self.mola = pymunk.Body(body_type=pymunk.Body.KINEMATIC)