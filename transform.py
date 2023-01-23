from scipy.signal import hilbert, butter, lfilter,sosfilt
from scipy.stats import gmean
from scipy import mean
import numpy as np
# from statistics import mean
constant =  1.73699

def butter_bandpass(lowcut, highcut, fs, order=8):
    return butter(order, [lowcut, highcut], fs=fs, btype='bandpass',output='sos')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=8):
    
    y= butter_bandpass(lowcut, highcut, fs, order=order)

    output = sosfilt(y, data)

    hilbert_transform = hilbert(output)


    squared_envelope = np.abs(hilbert_transform) ** 2
     
    gmean_signal = gmean(squared_envelope,axis=-1)
  
    mean_signal = mean(squared_envelope, axis =-1)
    
    # print((mean_signal)) 
    RS = float((mean_signal/gmean_signal) - constant)

    return RS