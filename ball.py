import pyglet


class Ball(pyglet.sprite.Sprite):
    #definindo aceleracoes e velocidades da bola

    GRAVITY_ACC = -200

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
        self.x = self.x + (self.x_VEL * dt) * self.suportX


    #definindo funcao para alterar velocidades
    def interaction(self, x, y, supx, supy):
        if x != None:
            self.x_VEL = x
        if y != None:
            self.y_VEL = y
            print(self.y_VEL)
        if supx != None:
            self.suportX = supx
        if supy != None:
            self.suportY = supy

    def handle_collision_with(self, obj):
        self.interaction(obj.interactX, obj.interactY, obj.suportingX, obj.suportingY)
