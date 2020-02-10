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

    def plot_time(self, X, t):
            Pressure = [Solution(self, x/t).p for x in X]
            Velocity = [Solution(self, x/t).u for x in X]
            Density = [Solution(self, x/t).rho for x in X]

            fig, axs = plt.subplots(3, sharex=True)
            fig.suptitle("Solution of the Riemann problem.")
            axs[0].plot(X, Density)
            axs[1].plot(X, Velocity)
            axs[2].plot(X, Pressure)

            axs[0].grid()
            axs[0].set(ylabel = "Density")
            axs[1].grid()
            axs[1].set(ylabel = "Velocity")
            axs[2].grid()
            axs[2].set(ylabel = "Pressure")

            plt.xlabel("x")
            plt.show()
