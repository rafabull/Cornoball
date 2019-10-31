import pyglet
import pymunk
from pyglet.gl import *
import functions
import ball
import bat
import obstaculos
from pymunk import pyglet_util

func = functions.Functions()
#posições iniciais

#Bola
xB = 505    #505
yB = 55     #55

#Bastoes
xE = 222
yE = 49
xD = 372
yD = 49

collision_types = {
    "ball": 1,
    "mola": 2,
    "Parede": 3,
    "objects": 4
}

class Game:
    pontos = 0
    vidas = 2
    #defnindo variaveis do pymunk
    space = pymunk.Space()
    space.gravity = (0.0, -500) # -500 é toop

    #definindo a taxa de atualisacão
    TIME_INTERVAL = 0.01
    time = 0

    #definindo o fundo e caracteristicas da janela
    fundo = pyglet.resource.image('resources/images/Arte fundo - baixo.png')

    windowWidth = fundo.width
    windowHeight = fundo.height

    #definindo a imagem de gameover
    go = pyglet.image.load('resources/images/gameOver.gif')
    go = func.ancorar(go, 'center')
    gameOver = pyglet.sprite.Sprite(go, windowWidth // 2, windowHeight // 2)

    #definindo array para objetos que podem colidir
    physicalObjects = []

    # Bordas
    borders = [pymunk.Segment(space.static_body, (495, 45), (515, 45), 1.0),  #tubo/dreita
               pymunk.Segment(space.static_body, (515, 45), (515, 400), 1.0),

               pymunk.Segment(space.static_body, (515, 400), (510, 500), 1.0),  #circulo/topo
               pymunk.Segment(space.static_body, (510, 500), (505, 545), 1.0),
               pymunk.Segment(space.static_body, (505, 545), (495, 570), 1.0),
               pymunk.Segment(space.static_body, (495, 570), (480, 600), 1.0),
               pymunk.Segment(space.static_body, (480, 600), (420, 660), 1.0),
               pymunk.Segment(space.static_body, (420, 660), (350, 693), 1.0),
               pymunk.Segment(space.static_body, (350, 693), (300, 697), 1.0),  #metade do
               pymunk.Segment(space.static_body, (300, 697), (250, 693), 1.0),  #semi circulo
               pymunk.Segment(space.static_body, (250, 693), (180, 660), 1.0),
               pymunk.Segment(space.static_body, (180, 660), (120, 600), 1.0),
               pymunk.Segment(space.static_body, (120, 600), (105, 570), 1.0),
               pymunk.Segment(space.static_body, (105, 570), (95, 545), 1.0),
               pymunk.Segment(space.static_body, (95, 545), (90, 500), 1.0),

               pymunk.Segment(space.static_body, (90, 500), (100, 400), 1.0),  #lado esquerdo
               pymunk.Segment(space.static_body, (100, 400), (130, 200), 1.0),
               pymunk.Segment(space.static_body, (130, 200), (214, 60), 1.0),

               pymunk.Segment(space.static_body, (380, 60), (460, 200), 1.0),  #lado direito
               pymunk.Segment(space.static_body, (460, 200), (495, 400), 1.0),

               pymunk.Segment(space.static_body, (495, 400), (495, 45), 1.0),   #tubo lado esquerdo
               pymunk.Segment(space.static_body, (495, 400), (490, 500), 1.0),
               pymunk.Segment(space.static_body, (490, 500), (485, 540), 1.0),
               pymunk.Segment(space.static_body, (485, 540), (475, 565), 1.0),
               pymunk.Segment(space.static_body, (475, 565), (460, 590), 1.0)
               ]
    removiveis = []


    #iniciando os elementos do jogo
    def __init__(self):
         #adicionando as formas(obstaculos)
        self.Circulo_0 = obstaculos.Circulo(385,583, 39, collision_types)
        self.Circulo_1 = obstaculos.Circulo(257,302, 39, collision_types)
        self.space.add(self.Circulo_0.circulo, self.Circulo_1.circulo)

        self.Triangulo1_0 = obstaculos.Triangulo1(270, 444, 42, collision_types)
        self.Triangulo1_1 = obstaculos.Triangulo1(181, 560, 42, collision_types)
        self.Triangulo1_2 = obstaculos.Triangulo1(413, 385, 42, collision_types)
        self.space.add(self.Triangulo1_0.triangulo1, self.Triangulo1_1.triangulo1, self.Triangulo1_2.triangulo1)

        self.Triangulo2_0 = obstaculos.Triangulo2(210, 121, 40, 90, -40, collision_types)
        self.Triangulo2_1 = obstaculos.Triangulo2(385, 121, -40, 90, 40, collision_types)
        self.space.add(self.Triangulo2_0.triangulo2, self.Triangulo2_1.triangulo2)

        self.Criaremov()

        #Criando os bastoes
        aux = func.ancorar(pyglet.image.load('resources/images/bastao1.png'), 'esq')
        self.batE = bat.Bat(-1, aux, xE, yE)
        self.space.add(self.batE.body, self.batE.shape) #adicionando os elementos a simulação fisica do pymunk
        self.space.add(self.batE.j, self.batE.s)
        self.physicalObjects.append(self.batE)

        aux = func.ancorar(pyglet.image.load('resources/images/bastao-1.png'), 'dir')
        self.batD = bat.Bat(1, aux, xD, yD)
        self.space.add(self.batD.body, self.batD.shape) #adicionando os elementos a simulação fisica do pymunk
        self.space.add(self.batD.j, self.batD.s)
        self.physicalObjects.append(self.batD)

        first = 0
        for line in self.borders:
            line.elasticity = 0.7
            line.group = 1
            if first == 0:
                line.collision_type = collision_types["mola"]
                first += 1
                line.elasticity = 0
            else:
                line.collision_type = collision_types["Parede"]
        self.space.add(self.borders)

        self.status = 'BEGINING'

        h = self.space.add_collision_handler(
            collision_types["mola"],
            collision_types["ball"])
        h.begin = self.iniciando
        
        hobj = self.space.add_collision_handler(
            collision_types["ball"],
            collision_types["objects"]
        )
        hobj.post_solve = self.col_post
        
    def col_post (self, arbiter, space, data):
        self.pontos += 10
        print(self.pontos)

    def iniciando(self, arbiter, space, data):
        self.status = 'BEGINING'
        print(self.status)
        return True

    def Criaremov (self):
        aux = func.ancorar(pyglet.image.load('resources/images/trigira.png'), 'center')
        self.Trigira_0 = obstaculos.Trigira(150, 300, 30, collision_types, aux)
        self.Trigira_1 = obstaculos.Trigira(190, 360, 30, collision_types, aux)
        self.Trigira_2 = obstaculos.Trigira(160, 400, 30, collision_types, aux)
        self.Trigira_3 = obstaculos.Trigira(140, 450, 30, collision_types, aux)
        self.space.add(self.Trigira_0.trigira, self.Trigira_0.trigira_body,
                       self.Trigira_1.trigira, self.Trigira_1.trigira_body,
                       self.Trigira_2.trigira, self.Trigira_2.trigira_body,
                       self.Trigira_3.trigira, self.Trigira_3.trigira_body)

        self.space.add(self.Trigira_0.j, self.Trigira_1.j, self.Trigira_2.j, self.Trigira_3.j)

        # Criando a bola
        self.mass = 1
        self.radius = 9
        aux = func.ancorar(pyglet.image.load('resources/images/bola.png'), 'center')
        self.ball = ball.Bola(self.mass, self.radius, xB, yB, collision_types, aux)
        self.space.add(self.ball.circle_body, self.ball.circle_shape)

        self.removiveis = [self.Trigira_0.trigira, self.Trigira_0.trigira_body,
                       self.Trigira_1.trigira, self.Trigira_1.trigira_body,
                       self.Trigira_2.trigira, self.Trigira_2.trigira_body,
                       self.Trigira_3.trigira, self.Trigira_3.trigira_body,
                       self.Trigira_0.j, self.Trigira_1.j, self.Trigira_2.j, self.Trigira_3.j,
                       self.ball.circle_body, self.ball.circle_shape]

        self.physicalObjects.extend([self.Trigira_0, self.Trigira_1, self.Trigira_2, self.Trigira_3])

    def reset(self):
        self.space.remove(self.removiveis)
        self.physicalObjects.remove(self.Trigira_0)
        self.physicalObjects.remove(self.Trigira_1)
        self.physicalObjects.remove(self.Trigira_2)
        self.physicalObjects.remove(self.Trigira_3)

        self.Criaremov()

        self.status = "BEGINING"

    def time_count(self):
        if self.status == 'BEGINING':
            self.charge_time = self.game_end_time - self.game_start_time
            if self.charge_time > 1:
                self.charge_time = 1
            self.ball.go(self.charge_time)
            self.status = "PLAYING"

    #desenhando na tela os elementos do jogo
    def draw(self):
        self.fundo.blit(0, 0)
        if self.status == 'GAME OVER':
            self.gameOver.draw()

        elif self.status == 'REINICIAR':
            self.gameOver.draw()
            fim = pyglet.text.Label(str("A pontuacao final e: "),
                                       font_name='Arial',
                                       font_size=20,
                                       x = self.windowHeight/2, y = self.windowWidth/2 + 30,
                                       color=(255, 100, 0, 255))
            pontosf = pyglet.text.Label(str(self.pontos),
                                       font_name='Arial',
                                       font_size=20,
                                       x = self.windowHeight/2, y = self.windowWidth/2,
                                       color=(255, 100, 0, 255))
            pontosf.draw()
            fim.draw()

        elif self.status == 'PLAYING' or self.status == 'BEGINING':
            self.ball.draw()
            for obj in self.physicalObjects:
                obj.draw()
            pontos = pyglet.text.Label(str(self.pontos),
                                       font_name='Arial',
                                       font_size=16,
                                       x=570, y=600,
                                       color=(255, 100, 0, 255))
            pontos.draw()
            vidas = pyglet.text.Label(str(self.vidas),
                                       font_name='Arial',
                                       font_size=16,
                                       x=570, y=520,
                                       color=(255, 100, 0, 255))
            vidas.draw()


    #verificando status do jogo e mudando pos da bola
    def update(self, dt):
        dt = Game.TIME_INTERVAL

        self.space.step(dt)
        if self.status == "PLAYING" or self.status == "BEGINING":
            if self.ball.y < 0:
                self.status = 'GAME OVER'
                self.vidas = self.vidas - 1
                if self.vidas <= 0:
                    self.status = 'REINICIAR'


            else:
                self.time += dt
                self.ball.update(dt)
                for obj in self.physicalObjects:
                    obj.update(dt)



