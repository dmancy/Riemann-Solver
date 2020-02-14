import math
import numpy as np
from State import State
import matplotlib.pyplot as plt


def plot_wave(speed, X, x0, t1, t2, str_label):
        #Plot a wave on a x-t diagram 
        T = []
        X2 = [] #New X array
        for x in X:
            time = 1/speed * (x-x0) 
            if t1 <= time <= t2:
                T.append(time)
                X2.append(x)

        plt.plot(X2,T, label=str_label)

                
