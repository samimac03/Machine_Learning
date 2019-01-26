import numpy as np

class board:

    def reset(self):
        self.moves = 0
        self.done = False
        self.turn = 1
        self.state = [0,0,0,0,0,0,0,0,0]
        self.repeat = 0
        self.wl = ""
        return self.state

    def display(self):
        print self.state[0], " ",self.state[1]," ", self.state[2]
        print self.state[3], " ",self.state[4]," ", self.state[5]
        print self.state[6], " ",self.state[7]," ", self.state[8]

    def test(self, action):
        self.reward = 0
        self.done = False
        if self.state[action] == self.state[(action+3)%9] \
        and self.state[action] == self.state[(action+6)%9]:
            self.reward = 100
            self.done = True
            self.wl = "win"
            #self.display()
        x = 0
        if (action % 3) == action:
            x = 0
        else:
            if (action % 6) == 0:
                x = 3
            else:
                x = 6
        if self.state[action] == (self.state[(action+1)%3]+x) \
        and self.state[action] == (self.state[(action+2)%3]+x):
            self.reward = 100
            self.done = True
            #self.display()
            self.wl = "win"



        if action == 2 or action == 4 or action == 6:
            if self.state[2] == self.state[4] \
            and self.state[2] == self.state[6]:
                self.reward = 100
                self.done = True
            #    self.display()
                self.wl = "win"

        if action%4 == 0:
            if self.state[0] == self.state[4] \
            and self.state[0] == self.state[8]:
                self.reward = 100
                self.done = True

                self.wl = "win"

        return self.done, self.reward, self.wl

    def step(self, action):
        self.reward = 0

        if self.state[action] != 0:
            self.reward = -100
            self.repeat = self.repeat+1

        else:
            self.state[action] = self.turn
            self.reward = 100
            self.done, self.reward, self.wl = self.test(action)

            self.moves = self.moves + 1
            self.turn = self.turn *-1

        if self.moves == 8:
            self.done = True
            self.wl = "draw"
            self.reward = 100

        return self.state, self.reward, self.done, self.wl, self.repeat
