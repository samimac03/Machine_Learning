import pygame
import numpy as np

class game:
    def reset(self):
        #self.screen=pygame.display.set_mode([500, 500])
        #self.screen.fill([0, 0, 0])
        self.x1, self.y1, self.z1 = 250,250,50
        self.x2, self.y2, self.z2 = 250,250,850
        self.ballX, self.ballY, self.ballZ = 250,250,450
        self.returns = 0
        if(np.random.rand() > .5):
            self.ballXO = -10
        else:
            self.ballXO = 10
        if(np.random.rand() > .5):
            self.ballYO = -10
        else:
            self.ballYO = 10
        if(np.random.rand() > .5):
            self.ballZO = -10
        else:
            self.ballZO = 10
        self.done = False

        self.ballXold, self.ballYold, self.ballZold = 0,0,0
        self.state = [self.ballXold, self.ballYold, self.ballZold, self.ballX, self.ballY, self.ballZ, self.x1, self.y1]
        return self.state

    def render(self):
        pygame.draw.circle(self.screen, [0,0,0], [self.ballXold,self.ballYold], 10)
        pygame.draw.rect(self.screen, [0,0,0], [self.x1old, self.y1old, 100, 100], 10)
        pygame.draw.rect(self.screen, [0,0,0], [self.x2old, self.y2old, 100, 100], 10)

        #pygame.draw.circle(self.screen, [255,0,0], [self.x1,self.y1], 10)

        pygame.draw.circle(self.screen, [250,100,100], [self.ballX,self.ballY], 10)
        pygame.draw.rect(self.screen, [255,255,255], [self.x1, self.y1, 100, 100], 10)
        pygame.draw.rect(self.screen, [255,255,255], [self.x2, self.y2, 100, 100], 10)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    def step(self, action):
        self.reward = 0
        self.ballXold, self.ballYold, self.ballZold, self.x1old, self.y1old, self.x2old, self.y2old = self.ballX, self.ballY, self.ballZ, self.x1,self.y1, self.x2,self.y2
        self.test(action)
        #self.render()

        self.state = [self.ballXold, self.ballYold, self.ballZold, self.ballX, self.ballY, self.ballZ, self.x1, self.y1]

        return self.state, self.reward, self.done, self.returns

    def test(self, action):
        if(action == 0):
            self.x1 = self.x1 + 10
        if(action == 1):
            self.x1 = self.x1 - 10
        if(action == 2):
            self.y1 = self.y1 + 10
        if(action == 3):
            self.y1 = self.y1 - 10
        if(action == 4):
            self.x1 = self.x1 + 10
            self.y1 = self.y1 + 10
        if(action == 5):
            self.x1 = self.x1 - 10
            self.y1 = self.y1 + 10
        if(action == 6):
            self.x1 = self.x1 - 10
            self.y1 = self.y1 - 10
        if(action == 7):
            self.x1 = self.x1 + 10
            self.y1 = self.y1 - 10
        if(action == 8):
            self.x1 = self.x1
            self.y1 = self.y1

        if(self.ballZ > self.z1-10 and self.ballZ < self.z1+10):
            if(self.ballX > self.x1 and self.ballX < self.x1+100):
                if (self.ballY > self.y1 and self.ballY < self.y1+100):
                    self.ballZO = self.ballZO * -1
                    self.reward = 100
                    self.returns = self.returns + 1
                else:
                    self.reward = self.reward - 5
            else:
                self.reward = self.reward - 5
        else:
            self.reward = self.reward - 10
        self.x2 = self.ballX -25
        self.y2 = self.ballY -25

        if(self.ballZ > self.z2+7 and self.ballZ < self.z2-7):
            if(self.ballX > self.x2 and self.ballX < self.x2+60):
                if (self.ballY> self.y2 and self.ballY < self.y2+60):
                    self.ballZO = self.ballZO * -1

        #print self.ballX - self.x1, self.ballY - self.y1, self.ballZ - 50
        if(self.ballZ > 900):
            self.reward = -100
            self.done = True
        if(self.ballZ < 0):
            self.reward = 100
            self.done = True

        if(self.x1+100 > 500 or self.x1 < -5 or self.y1 > 500 or self.y1 < -5):
            self.reward = -50

        if(self.ballY > 500 or self.ballY < 1):
            self.ballYO = self.ballYO * -1

        if(self.ballX > 500 or self.ballX < 1):
            self.ballXO = self.ballXO * -1

        self.ballX, self.ballY, self.ballZ = self.ballX + self.ballXO, self.ballY + self.ballYO, self.ballZ + self.ballZO
