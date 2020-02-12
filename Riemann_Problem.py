import numpy as np
import math
import matplotlib.pyplot as plt

from Solution import Solution

class Riemann:
    """Define a Riemann Problem by:
    - the left state W_left
    - the state between the left wave and the contact surface W_left_star
    - the state between the contact surface and the right wave W_right_star
    - the right state W_right
    - the left wave Left_Wave
    - the right eave Right_Wave"""

    def __init__(self, W_left, W_left_star, W_right_star, W_right, Left_Wave, Right_Wave): 
            """Constructor"""

            self.W_left = W_left
            self.W_left_star = W_left_star
            self.W_right_star = W_right_star
            self.W_right = W_right
            
            self.Left_Wave = Left_Wave
            self.Right_Wave = Right_Wave


    def eval_sampling_point(self, sampling_point):
            """Compute the state a a given sampling point x/t"""
            return Solution(self, sampling_point)

    def plot_time(self, X, x0, t):
            """Plot the repartition of density, velocity and pressure at a given time t, on a mesh X, where the origin of the discontinuity is in x0"""
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
            plt.xlim((-.5, .5))

            plt.xlabel("Location x")
            plt.show()


