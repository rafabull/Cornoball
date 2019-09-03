import pyglet
import pymunk
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
    #defnindo variaveis do pymunk
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

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

    # Bordas
    borders = [pymunk.Segment(space.static_body, (548, 50), (570, 50), 1.0),
               pymunk.Segment(space.static_body, (570, 50), (570, 400), 1.0)]

    #iniciando os elementos do jogo
    def __init__(self):
        self.ball = ball.Ball(pyglet.image.load_animation('resources/images/bola.gif'), xB, yB)

        #Criando os bastoes
        aux = func.ancorar(pyglet.image.load('resources/images/barra.jpg'), 'esq')
        self.batE = bat.Bat(-1, aux, xE, yE)
        self.space.add(self.batE.body, self.batE.shape) #adicionando os elementos a simulação fisica do pymunk
        self.space.add(self.batE.j, self.batE.s)
        self.physicalObjects.append(self.batE)

        aux = func.ancorar(pyglet.image.load('resources/images/barra.jpg'), 'dir')
        self.batD = bat.Bat(1, aux, xD, yD)
        self.space.add(self.batD.body, self.batD.shape) #adicionando os elementos a simulação fisica do pymunk
        self.space.add(self.batD.j, self.batD.s)
        self.physicalObjects.append(self.batD)

        for line in self.borders:
            line.elasticity = 0.7
            line.group = 1
        self.space.add(self.borders)

        self.status = 'BEGINING'
        self.molaS = 'GO'
        self.molaX = 0

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

        self.space.step(dt)
        if self.status == "PLAYING":
            if self.ball.y < 0:
                self.status = 'GAME OVER'
            else:
                self.time += dt

                self.ball.update(dt)
                self.batE.update(dt)
                self.batD.update(dt)


        elif self.status == "BEGINING":
            self.atMola(self.molaS)
            self.batE.update(dt)
            self.batD.update(dt)

    def atMola(self, status):
        if status == 'PRESS':
            self.molaX += 40

        elif status == 'GO':
            if self.molaX != 0:
                impulsoBola = self.molaX
                #chamar função para aplicar impulso na bolinha se ela estiver na posição inicial

            self.molaX = 0
            self.status = "PLAYING"

