

from environement import environment
import numpy as np
from rlmodels import build_agent, build_model
from tensorflow.keras.optimizers import Adam

if __name__ == "__main__":

    # Create an object of the environment class
    env = environment()
    # Define the states of the model
    states = np.shape(env.state)
    print(states, " state value")
    print("observation space ", np.shape(env.signal))
    # Define the actions
    actions = len(env.action_space)

    # Build the RL model from rlmodel.py file
    model = build_model(states,actions)

    # Defining the parameters of the Deep Q Network
    dqn = build_agent(model, actions)
    dqn.compile(Adam(learning_rate = 5e-4) , metrics = ['mae'])

    # Running the DQN Model
    dqn.fit(env, nb_steps=10000, visualize= False, verbose = 1)

    # Saving the weights
    dqn.save_weights("/content/drive/MyDrive/Intern/trial/", overwrite = True)
    print(env.state)