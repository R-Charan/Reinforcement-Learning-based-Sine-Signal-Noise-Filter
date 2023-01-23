from environement import environment
import numpy as np
from rlmodels import build_agent, build_model
from tensorflow.keras.optimizers import Adam
env = environment()
states = np.shape(env.state)
print(states, " state value")
print("observation space ", np.shape(env.signal))
actions = len(env.action_space)


model = build_model(states,actions)

dqn = build_agent(model, actions)
dqn.compile(Adam(learning_rate = 5e-4) , metrics = ['mae'])
dqn.fit(env, nb_steps=10000, visualize= False, verbose = 1)
dqn.save_weights("/content/drive/MyDrive/Intern/trial/", overwrite = True)
print(env.state)