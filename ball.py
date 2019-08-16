import pyglet


class Ball(pyglet.sprite.Sprite):
    #definindo aceleracoes e velocidades da bola
    GRAVITY_ACC = -200
    at_ACC = - 100
    x_ACC = 0
    y_ACC = 0
    x_VEL = 0 #ainda n serve pra nd
    y_VEL = 0 #ainda n serve pra nd

    suport = 0 #define se a variavel esta em um suporte 0 -> reto 1-> não esta

    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)

    #atualizando a posicao da bola
    def update(self, dt):
        self.y_VEL = self.y_VEL + (self.GRAVITY_ACC*self.suport + self.y_ACC)*dt
        self.y = self.y + self.y_VEL*dt

        self.x = self.x + self.x_VEL * dt

    #definindo funcao para alterar velocidades
    def interaction(self, x, y, sup):
        if x != None:
            self.x_VEL = x
        elif y != None:
            self.y_VEL = y
        if sup != None:
            self.suport = sup

    #def handle_collision_with(self, other_object):
