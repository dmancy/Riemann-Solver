import numpy as np
import math
import matplotlib.pyplot as plt

from Solution import Solution

class Riemann:


    def __init__(self, W_left, W_left_star, W_right_star, W_right, Left_Wave, Right_Wave): 

            self.W_left = W_left
            self.W_left_star = W_left_star
            self.W_right_star = W_right_star
            self.W_right = W_right
            
            self.Left_Wave = Left_Wave
            self.Right_Wave = Right_Wave


    def eval_sampling_point(self, sampling_point):
            return Solution(self, sampling_point)

    def plot_time(self, X, x0, t):
            Pressure = [Solution(self, (x-x0)/t).pressure for x in X]
            Velocity = [Solution(self, (x-x0)/t).velocity for x in X]
            Density = [Solution(self, (x-x0)/t).rho for x in X]

            fig, axs = plt.subplots(3, sharex=True)
            fig.suptitle("Solution of the Riemann problem\nat t = {}s".format(t))
            axs[0].plot(X, Density)
            axs[1].plot(X, Velocity)
            axs[2].plot(X, Pressure)

            axs[0].grid()
            axs[0].set(ylabel = "Density")
            axs[1].grid()
            axs[1].set(ylabel = "Velocity")
            axs[2].grid()
            axs[2].set(ylabel = "Pressure")

            plt.xlabel("Location x")
            plt.show()
