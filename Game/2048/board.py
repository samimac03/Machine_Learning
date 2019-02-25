import numpy as np
class board:
    def __init__(self):
        self.board  = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.rand(init=True)

    def rand(self, init=False):
        x = np.random.randint(4)
        y = np.random.randint(4)
        if (self.board[x][y]==0):
            if(np.random.randint(4)>0):
                self.board[x][y]=1
            else:
                self.board[x][y]=2
        else:
            self.rand()
        if(init):
            self.rand()

    def render(self):
        for y in range(4):
                print(self.board[0][y],self.board[1][y],self.board[2][y],self.board[3][y])

    def move(self, dir):
        dir = int(dir)

        if(dir == 0):
            rec = 0
            begin = []
            for y in range(4):
                list = []
                begin = self.board[y]
                x = 0
                rec = 0
                for x in range(4):
                    if(self.board[x][y] != 0):
                        list.append(self.board[x][y])

                    if(len(list)>1):
                        if(rec == 0):
                            if(list[len(list)-2] == list[len(list)-1]):
                                list[len(list)-2] += 1
                                list.pop(len(list)-1)
                                rec = 1
                        else:
                            if(len(list) != 2):
                                if(list[len(list)-2] == list[len(list)-1]):
                                    list[len(list)-2] += 1
                                    list.pop(len(list)-1)
                    x += 1
                if(len(list)==0 or len(list)==4):
                    rec += 1
                for a in range(4-len(list)):
                    list.append(0)
                if(begin == list):
                    rec += 1
                for z in range(4):
                    self.board[z][y] = list[z]
            if(rec != 4):
                self.rand()

        if(dir == 1):
            rec = 0
            for y in range(4):
                list = []
                begin = self.board[y]
                x = 0
                rec = 0
                for x in range(4):
                    if(self.board[x][y] != 0):
                        list.append(self.board[x][y])
                    if(len(list)>1):
                        if(rec == 0):
                            if(list[len(list)-2] == list[len(list)-1]):
                                list[len(list)-1] += 1
                                list.pop(len(list)-2)
                                rec = 1
                        else:
                            if(len(list) != 2):
                                if(list[len(list)-2] == list[len(list)-1]):
                                    list[len(list)-1] += 1
                                    list.pop(len(list)-2)
                    x += 1

                if(len(list)==0 or len(list)==4):
                    rec += 1
                for a in range(4-len(list)):
                    list.insert(a,0)
                if(begin == list):
                    rec += 1
                for z in range(4):
                    self.board[z][y] = list[z]
            if(rec != 4):
                self.rand()

        if(dir == 2):
            begin = []
            for x in range(4):
                begin = self.board[x]
                list = []
                y = 0
                rec = 0
                for y in range(4):
                    if(self.board[x][y] != 0):
                        list.append(self.board[x][y])
                    if(len(list)>1):
                        if(rec == 0):
                            if(list[len(list)-2] == list[len(list)-1]):
                                list[len(list)-2] += 1
                                list.pop(len(list)-1)
                                rec = 1
                        else:
                            if(len(list) != 2):
                                if(list[len(list)-2] == list[len(list)-1]):
                                    list[len(list)-2] += 1
                                    list.pop(len(list)-1)
                                    rec = 1
                    y += 1
                if(len(list)==0 or len(list)==4):
                    rec += 1
                for a in range(4-len(list)):
                    list.append(0)
                if(begin == list):
                    rec += 1
                for z in range(4):
                    self.board[x][z] = list[z]
            if(rec != 4):
                self.rand()

        if(dir == 3):
            rec = 0
            begin = self.board
            for x in range(4):
                list = []
                y = 0
                rec = 0
                for y in range(4):
                    if(self.board[x][y] != 0):
                        list.append(self.board[x][y])
                    if(len(list)>1):
                        if(rec == 0):
                            if(list[len(list)-2] == list[len(list)-1]):
                                list[len(list)-1] += 1
                                list.pop(len(list)-2)
                                rec = 1
                        else:
                            if(len(list) != 2):
                                if(list[len(list)-2] == list[len(list)-1]):
                                    list[len(list)-1] += 1
                                    list.pop(len(list)-2)
                    if(begin == self.board):
                        y += 1

                for a in range(4-len(list)):
                    list.insert(a,0)
                for z in range(4):
                    self.board[x][z] = list[z]
                print("")
            if(rec != 4):
                self.rand()
