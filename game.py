import pyglet
from pyglet.gl import *
import functions
import ball
import bat

func = functions.Functions()
#posições iniciais

#Bola
xB = 550    #Se alterar, altere a class ball (update)
yB = 47

#Bastoes
xE = 230
yE = 50
xD = 400
yD = 50


class Game:
    #definindo a taxa de atualisacão
    TIME_INTERVAL = 0.05

    #definindo o fundo e caracteristicas da janela
    fundo = pyglet.resource.image('resources/images/fundo.png')

    windowWidth = fundo.width
    windowHeight = fundo.height

    #definindo a imagem de gameover
    go = pyglet.image.load('resources/images/gameOver.gif')
    go = func.ancorar(go, 'center')
    gameOver = pyglet.sprite.Sprite(go, windowWidth // 2, windowHeight // 2)

    #iniciando os elementos do jogo
    def __init__(self):
        self.ball = ball.Ball(pyglet.image.load_animation('resources/images/bola.gif'), xB, yB)

        aux = func.ancorar(pyglet.image.load('resources/images/barra.jpg'), 'esq')
        self.batE = bat.Bat(30, aux, xE, yE,)

        aux = func.ancorar(pyglet.image.load('resources/images/barra.jpg'), 'dir')
        self.batD = bat.Bat(-30, aux, xD, yD)

        self.molaK = 0
        self.molaS = 'Go'

        self.status = 'PLAYING'

    #desenhando na tela os elementos do jogo
    def draw(self):
        self.fundo.blit(0, 0)
        if self.status == 'GAME OVER':
            self.gameOver.draw()

        self.ball.draw()
        self.batE.draw()
        self.batD.draw()

    #verificando status do jogo e mudando pos da bola
    def update(self, dt):
        dt = Game.TIME_INTERVAL

        if self.ball.y < 0:
            self.status = 'GAME OVER'

        else:
            self.atMola(self.molaS)

            self.ball.update(dt)

    #chamando as funcoes para rotacionar os bastoes
    def esq(self):
        self.batE.click(30)

    def dir(self):
        self.batD.click(-30)

    def atMola(self, status):
        if status == 'Press':
            self.molaK += 20

        elif status == 'Go':
            if self.molaK != 0:
                self.ball.interaction(x=None, y=self.molaK)
                print(self.molaK)
            self.molaK = 0



