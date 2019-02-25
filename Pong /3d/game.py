import pong
import network
import numpy as np
import os
import pygame
import cv2
from PIL import ImageGrab as ig


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
env = pong.game()

observ = 8
action = 9
win = 0
loss = 0
re = 0.0000000000
nn = network.DQNagent(observ, action)
for i in range(200000):
    state = env.reset()
    state = np.reshape(state, [1, 8])
    for moves in range(500000):
        action = nn.act(state)
        next_state, reward, done, returns= env.step(action)
        next_state = np.reshape(next_state, [1, 8])
        nn.recall(state, action, reward, next_state, done)
        state = next_state
        if done:
            re = re + returns
            print("Returns:{},Avg:{} Iter:{}".format(returns,re/(i+1), i+1))
            print " "
            break
    if i>5:
        nn.replay(50)
pygame.quit()
