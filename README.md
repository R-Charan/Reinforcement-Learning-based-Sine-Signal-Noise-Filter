# Reinforcement-Learning-based-Sine-Signal-Noise-Filter
A Mini Project that aims to filter various types of noises present in a sine signal with the help of Deep Q Reinforcement Learning algorithm.

Libraries used:
Standard libraries
1. Numpy
2. Scipy

Reinforcement Learning Libraries
1. Keras-rl2
2. TensorFlow
3. OpenAI Gym

Code work Flow:
1. The signal is loaded using the python file **channel.py** from the environment file **environment.py**. 
2. An action is chosen from the set of pre-defined action space based on a Boltzmann policy.
3. Once the specific operation is taken, the reward for the action is calculated in the python file **transform.py**.
4. The DQN defined in the file **rlmodels.py** caucaltes and output the corresponding action and Q-value for that state.
