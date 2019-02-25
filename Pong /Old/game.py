import pong
import network
import numpy as np
import os
import pygame
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
env = pong.Game()

observ = 4
action = 3
win = 0
loss = 0
re = 0.0000000000
nn = network.DQNagent(observ, action)
for i in range(200000):
    state = env.reset()
    state = np.reshape(state, [1, 4])
    for moves in range(300000):
        action = nn.act(state)
        next_state, reward, done, wl, returns= env.step(action)
        next_state = np.reshape(next_state, [1, 4])
        nn.recall(state, action, reward, next_state, done)
        state = next_state
        if done:

            if wl == "win":
                win = win+1
            else:
                if wl == "loss":
                     loss = loss + 1
            re = re + returns
            print("Returns:{},Avg:{} Iter:{}".format(returns,re/(i+1), i+1))
            print " "
            break
    if i>4:
        nn.replay(50)
    if i % 20 == 0:
        nn.saveModel(i)
pygame.quit()
