# Reinforcement-Learning-based-Sine-Signal-Noise-Filter
A Mini Project that aims to filter various types of noises present in a sine signal with the help of Deep Q Reinforcement Learning algorithm.

## Libraries used:
### Standard libraries
1. Numpy
2. Scipy

### Reinforcement Learning Libraries*
1. Keras-rl2
2. TensorFlow
3. OpenAI Gym

## Code work Flow:
1. The signal is loaded using the python file **channel.py** from the environment file **environment.py**. 
2. An action is chosen from the set of pre-defined action space based on a Boltzmann policy.
3. Once the specific operation is taken, the reward for the action is calculated in the python file **transform.py**.
4. The DQN defined in the file **rlmodels.py** calculates and outputs the corresponding action and Q-value for that state.

## The Environment:
Two approches have been tried out in defining the environment. One method was defining all quantiites using only numpy arrays without any use gym library and the other environment file has all its variables defined with the help of gym library.

## Results:

### The actual signal
<img width="290" alt="Actual Signal" src="https://user-images.githubusercontent.com/83712618/214195612-0169b438-f95f-4a11-bee0-c53a94c0ac38.png">

### The noisy signal after adding random noise.
<img width="278" alt="Noisy signal" src="https://user-images.githubusercontent.com/83712618/214195691-013e38b7-1b83-47de-9867-2ace265d1ad4.png">

### The output after running the algorithm
<img width="277" alt="RL output" src="https://user-images.githubusercontent.com/83712618/214195732-728806d8-b5c1-482c-a6fa-e1f69702b8c5.png">
