# Python file that loads the signal from the .mat file

import numpy as np
from math import pi
from scipy.io import loadmat
def load_channel():
    # Generate AM-modulated sinusoid
    # N = 256
    # t = np.linspace(0,2,N)

    # # Modulator
    # m = 1 + .2*np.cos(2*pi*t)

    # # Carrier
    # c = np.sin(2*pi*90*t)

    # # Signal is modulator times carrier
    # x = m*c

    signal = loadmat("B-A-1.mat")
    
    return signal['Channel_1'].T

