# Gym Implementation
from gym import Env
from gym.spaces import Box, Discrete
import channel
import numpy as np
import transform


class environment(Env):
    def __init__(self):
        # No of possible actions are 5 (lower frequency - 2 , upper frequency - 2, no actions-1)
        self.action_space = Discrete(5)

        self.actions = np.array([[25, 0], [-25, 0], [0, 25], [0, -25], [0, 0]])
        # Loading Signal and sampling frequency
        self.signal, self.fs = channel.load_channel()

        # Starting State of the agent([lower,upper])
        self.observation_space = Box(low=0.1, high=self.fs / 2, shape=(2,), dtype = np.int32)
        self.state = np.sort(self.observation_space.sample())
        self.dummy = self.state

        self.filter_time_step = 30

    def step(self, action):

        self.filter_time_step -= 1

        # Calculation of the new state
        self.state = np.add(self.state, self.actions[action])

        # Base condition to penalize and reward
        if (self.state[0] >= self.state[1]).all() or (self.state[0] <= 0).all():
            reward = -5

        else:

            reward = transform.butter_bandpass_filter(self.signal, self.state[0], self.state[1],
                                                      self.fs)

        if self.filter_time_step <= 0:
            done = True
        else:
            done = False

        info = {}  # Placeholder - to store all collected info

        return self.state, reward, done, info

    def render(self, mode='human'):
        pass

    def reset(self):
        self.filter_time_step = 30
        self.state = self.dummy
        return self.state
