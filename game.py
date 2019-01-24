import tic
import network
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
env = tic.board()

observ = 9
action = 9
win = 0
draw = 0
repeats = 0.0000000
re = 0
def run(state):
    done = False
    while not done:
        repeatO = 0
        action = int(raw_input())
        next_state, reward, done, wl, repeat = env.step(action)
        action = nn.act(state)
        next_state, reward, done, wl, repeat = env.step(action)
        while repeat-repeatO >  0:
            action = nn.act(state)
            if repeat > 20:
                nn.replay(130)
            print repeat
        next_state = np.reshape(next_state, [1, 9])
        nn.recall(state, action, reward, next_state, done)
        state = next_state
        env.display()

nn = network.DQNagent(observ, action)
for i in range(2000):
    state = env.reset()
    state = np.reshape(state, [1, 9])
    for moves in range(30):
        action = nn.act(state)
        next_state, reward, done, wl, repeat = env.step(action)
        next_state = np.reshape(next_state, [1, 9])
        nn.recall(state, action, reward, next_state, done)
        state = next_state

        re = re+1
        repeats = repeats + repeat
        if done:
            if wl == "win":
                win = win+1
            else:
                if wl == "draw":
                     draw = draw + 1
            print("Wins:{} Draws:{} Total:{} Repeat:{}".format(win, draw, win+draw, repeat))
            print("Repeat:{} repeat:{}".format(repeats/(re),repeat))
            print " "
            break
    if i>5:
        nn.replay(52)
        nn.saveModel(i)
for x in range(10):
    state = env.reset()
    state = np.reshape(state, [1, 9])
    done = False
    run(state)
