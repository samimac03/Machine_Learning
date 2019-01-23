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
nn = network.DQNagent(observ, action)
for i in range(5000):
    state = env.reset()
    state = np.reshape(state, [1, 9])
    for moves in range(20):
        action = nn.act(state)
        next_state, reward, done, wl = env.step(action)

        next_state = np.reshape(next_state, [1, 9])
        reward = reward *-1
        nn.recall(state, action, reward, next_state, done)
        state = next_state
        if done:
            if wl == "win":
                win = win+1
            else:
                if wl == "draw":
                     draw = draw + 1
            print("Wins:{} Draws:{}".format(win, draw))
            break
    if i>3:
        nn.replay(39)
env.close()
