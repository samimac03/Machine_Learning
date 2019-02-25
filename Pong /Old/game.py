import pong
import network
import numpy as np
import os
import pygame
import cv2



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
env = pong.Game()
rewards = []
state_size = 5
action_size = 3
total_reward = 0
win = 0
loss = 0
re = 0.0000000000
render = 0
nn = network.DQNagent(state_size, action_size)
for i in range(100000):
    render = 1
    done = False
    state = env.reset(render)
    state = np.reshape(state, [1, state_size])
    while not done:
        action = nn.act(state)
        next_state, reward, done, wl, returns = env.step(action, render)
        next_state = np.reshape(next_state, [1, state_size])
        #reward = reward if not done else -100
        if reward > 0:
            rewards.append(reward)
        total_reward = total_reward + reward
        nn.recall(state, action, reward, next_state, done)
        state = next_state

        if len(rewards) > 100:
            total_reward = total_reward - rewards[0]
            rewards.pop(0)

        if done:

            if wl == "win":
                win = win+1
            else:
                if wl == "loss":
                     loss = loss + 1
            re = re + returns
            print("Returns:{},AvgReturns:{}, Iter:{}".format(returns,re/(i+1), i+1))
            break
    nn.replay(10)

#    if i % 100 == 0:
#        nn._save()

pygame.quit()
