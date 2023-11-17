# The python file that defines the environment, the step, the reset for the model.

import transform
import channel
import numpy as np

class environment:
  def __init__(self):

    # No of possible actions are 6 (lower frequecy - 2 , upper frequency - 2, simul -2,no aciton-1)
    self.action_space = np.array([[75, 0], [-75, 0], [75, 75], [-75, -75], [0, 75], [0, -75], [0, 0]])
    self.signal = channel.load_channel() # Channel is the time domain signal 
    #Starting State of the agent([lower,upper])
    self.state = np.array([100, 300]) 
    self.filter_time_step = 180
  
  def step(self, action):
    
    self.state = np.add(self.state, self.action_space[action])
    print("\nnew state", self.state)
        # Confirming reward criterion
    if self.state[0] <= 0 or self.state[0] >= self.state[1]:
        reward = -50
    else:
        reward = transform.butter_bandpass_filter(self.signal, self.state[0], self.state[1], 2_00_000)
    self.filter_time_step -= 10
    if self.filter_time_step == 0:
        done = True
    else:
        done = False
   
    # Reward caluclation

    info ={} #Placeholder - to store all collected info

    return self.state, reward, done, info

  def reset(self):
    self.filter_time_step = 30
    self.state = np.array([100,300])
    self.observation_space = channel.load_channel()
  
    return self.state
