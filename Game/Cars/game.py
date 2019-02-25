import math
import numpy as np
import pygame


class game:
    def __init__(self, cars):
        self.FPS = 30
        self.WIDTH = 650
        self.HEIGHT = 450
        self.clock = pygame.time.Clock()
        self.cars = []
        self.x = np.random.randint(250,self.WIDTH)
        self.y = np.random.randint(250,self.HEIGHT)
        self.draw(init = True)
        for i in range(cars-1):
            self.cars.append(car(self.x, self.y))
            self.x = np.random.randint(250,self.WIDTH)
            self.y = np.random.randint(250,self.HEIGHT)
            #self.x %= 30

        self.cars.append(car(self.x, self.y ,player = True))
    #def map_gen(self):

    def input(self):
        key = pygame.key.get_pressed()
        if not (key[pygame.K_w]) and (self.cars[len(self.cars)-1].acc > 0):
            self.cars[len(self.cars)-1].acc = 0
        if not (key[pygame.K_s]) and (self.cars[len(self.cars)-1].acc < 0):
            self.cars[len(self.cars)-1].acc = 0

        if(self.cars[len(self.cars)-1].acc > self.cars[len(self.cars)-1].max_acc):
            self.cars[len(self.cars)-1].acc -= .2
        if(self.cars[len(self.cars)-1].acc < -(self.cars[len(self.cars)-1].max_acc)):
            self.cars[len(self.cars)-1].acc += .2
        if key[pygame.K_w]:
            self.cars[len(self.cars)-1].acc += .2

        if key[pygame.K_s]:
            self.cars[len(self.cars)-1].acc -= .2

        if key[pygame.K_a]:
            self.cars[len(self.cars)-1].rotation -= 5

        if key[pygame.K_d]:
            self.cars[len(self.cars)-1].rotation += 5


        self.cars[len(self.cars)-1]._move()
        players = []
        for car in self.cars:
            players.append([car.x,car.y,car.player])
        for car in self.cars:
            car.ai(players)

    def draw(self, init = False):
        self.clock.tick(self.FPS)
        if init:
            self.screen=pygame.display.set_mode([self.WIDTH, self.HEIGHT])
            pygame.init()
        self.screen.fill([0,0,0])

        for car in self.cars:
            cur = pygame.Surface((10,20))
            cur.set_colorkey([0,0,0])
            cur.fill(car.color)

            rect = cur.get_rect()
            rect.center = [car.x,car.y]

            new = pygame.transform.rotate(cur, car.rotation)
            rect = new.get_rect()

            rect.center = [car.x,car.y]
            self.screen.blit(new, rect)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pygame.display.flip()



class car:
    def __init__(self, x, y, player = False):
        self.player = player
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.acc = 0
        self.max_torq = 10
        self.max_acc = 2
        self.rotation = 0
        self.color = [np.random.randint(255),np.random.randint(255),np.random.randint(255)]
        self.oldX = self.x
        self.oldY = self.y

    def _move(self):
        self.oldX = self.x
        self.oldY = self.y
        if (self.acc > self.max_acc):
            self.acc -= .2
        if (self.acc < (-self.max_acc + .005)):
            self.acc += .2
        if(self.acc < -.1 or self.acc > .1):
            if(self.velX > 0):
                self.velX -= 1
            else:
                self.velX += 1
            if(self.velY > 0):
                self.velY -= 1
            else:
                self.velY += 1
        if self.rotation < 0:
            self.rotation = self.rotation%-360
        else:
            self.rotation = self.rotation%360
        if self.acc == 0:
            if self.velX > 0.2:
                self.velX -= 0.1
            elif self.velX < -0.2:
                self.velX += .1
            else:
                self.velX = 0
            if self.velY > 0.2:
                self.velY -= .1
            elif self.velY < -0.2:
                self.velY += .1
            else:
                self.velY = 0

        if self.velX < 3 and self.velX > -3:
            self.velX += (np.sin(np.radians(self.rotation))) * -self.acc

        if self.velY < 3 and self.velY > -3:
            self.velY += (np.cos(np.radians(self.rotation))) * -self.acc
        self.x += self.velX
        self.y += self.velY
    def ai(self, players):
        if not self.player:
            for x, y, name in players:
                if name:
                    self.targetX = self.x - x
                    self.targetY = self.y - y
                    a = self.targetX**2 + self.targetY**2
                    c = self.targetX**2 + self.targetY-10**2
                    b = -10

                    self.rotation = ((a+b-c)/((2)*(a**.5)*(b**.5)))
                    self.rotation = math.acos(self.rotation)
                    print(self.targetX, self.targetY, self.rotation)
                    self.acc = .1
                    self._move()
g = game(2)
def main():
    g.input()
    g.draw()
while(__name__ == '__main__'):
    main()
py.quit()
