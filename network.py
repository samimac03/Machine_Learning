import keras
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *
from keras.models import model_from_json
import random
import os
class DQNagent:

    def __init__(self, state_size, action_size):

        self.stateSize = state_size
        self.actionSize = action_size
        self.memory = deque(maxlen=3000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.eDecay = 0.999999
        self.eMin = 0.01
        self.learningRate = 0.01
        self.model = self._buildModel()
        self.oldX = ""

    def _buildModel(self):
        model = Sequential()
        model.add(Dense(54, input_dim=self.stateSize, activation='relu'))
        model.add(Dense(54, activation='relu'))
        model.add(Dense(self.actionSize, activation='linear'))
        model.compile(loss='mse',optimizer=Adam(lr=self.learningRate))

        json_file = open('/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/tictaktoe/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        self.y = os.listdir("/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/tictaktoe/Weights/")
        print self.y[0]
        loaded_model.load_weights("/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/tictaktoe/Weights/" + self.y[0])
        return model

    def recall(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.actionSize)

        act_values = self.model.predict(state)
        return np.argmax(act_values[0])
    def saveModel(self, i):
        if os.path.isfile(self.oldX):
            os.remove(self.oldX)
        model_json = self.model.to_json()
        with open("/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/tictaktoe/model.json", "w") as json_file:
            json_file.write(model_json)
            self.x = ("/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/tictaktoe/Weights/{}.h5".format(i))
        self.model.save_weights(self.x)
        self.oldX = self.x


    def replay(self, batchSize):
        miniBatch = random.sample(self.memory, batchSize)
        for state, action, reward, next_state, done in miniBatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
            if self.epsilon>self.eMin:
                self.epsilon *= self.eDecay
