# The python file that build the RL models using keras RL and tensorflow Keras.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def build_model(states, actions):
    model = Sequential()
    model.add(Dense(65, activation = 'relu' , input_shape = (1,2)))
    model.add(Dense(24, activation = 'relu'))
    model.add(Flatten())
    model.add(Dense(actions))
    return model

def build_agent(model,actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit = 50000, window_length = 1)
    dqn = DQNAgent(model = model, memory=memory, policy=policy, nb_actions = actions,
                    nb_steps_warmup = 1, target_model_update = 1e-2, gamma = 0.95)

    return dqn
    