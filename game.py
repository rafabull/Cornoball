import pyglet
from pyglet.gl import *
import functions
import ball
import bat

func = functions.Functions()
#posições iniciais

#Bola
xB = 250
yB = 500

#Bastoes
xE = 230
yE = 50
xD = 400
yD = 50

class Game:
    #definindo a taxa de atualisacão
    TIME_INTERVAL = 0.01
    time = 0

    #definindo o fundo e caracteristicas da janela
    fundo = pyglet.resource.image('resources/images/fundo.png')

    windowWidth = fundo.width
    windowHeight = fundo.height

    #definindo a imagem de gameover
    go = pyglet.image.load('resources/images/gameOver.gif')
    go = func.ancorar(go, 'center')
    gameOver = pyglet.sprite.Sprite(go, windowWidth // 2, windowHeight // 2)

    #definindo array para objetos que podem colidir
    physicalObjects = []

    #iniciando os elementos do jogo
    def __init__(self):
        self.ball = ball.Ball(pyglet.image.load_animation('resources/images/bola.gif'), xB, yB)

        aux = func.ancorar(pyglet.image.load('resources/images/barra.jpg'), 'esq')
        self.batE = bat.Bat(30, 1, aux, xE, yE)
        self.physicalObjects.append(self.batE)

        aux = func.ancorar(pyglet.image.load('resources/images/barra.jpg'), 'dir')
        self.batD = bat.Bat(-30, -1, aux, xD, yD)
        self.physicalObjects.append(self.batD)

        self.molaK = 0
        self.molaS = 'St'

        self.status = 'BEGINING'


    #desenhando na tela os elementos do jogo
    def draw(self):
        self.fundo.blit(0, 0)
        if self.status == 'GAME OVER':
            self.gameOver.draw()

        elif self.status == 'PLAYING' or self.status == 'BEGINING':
            self.ball.draw()
            for obj in self.physicalObjects:
                obj.draw()

    #verificando status do jogo e mudando pos da bola
    def update(self, dt):
        dt = Game.TIME_INTERVAL

        if self.status == "PLAYING":
            if self.ball.y < 0:
                self.status = 'GAME OVER'
            else:
                self.time += dt

                self.ball.update(dt)
                self.batE.update(dt)
                self.batD.update(dt)

                for obj in self.physicalObjects:
                    self.collision(self.ball, obj)

                self.ball.interaction(None, None, 1, 1)

        elif self.status == "BEGINING":
            self.atMola(self.molaS)
            self.batE.update(dt)
            self.batD.update(dt)

    def atMola(self, status):
        if status == 'Press':
            self.molaK += 40

        elif status == 'Go':
            if self.molaK != 0:
                self.ball.interaction(None, self.molaK, None, 1)
            self.molaK = 0
            self.status = "PLAYING"


    def collision(self, obj1, obj2):
        if obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x \
                and obj1.y < obj2.y + obj2.height and obj1.height + obj1.y > obj2.y:
            obj1.handle_collision_with(obj2)

