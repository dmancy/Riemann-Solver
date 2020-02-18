import numpy as np
import math
import matplotlib.pyplot as plt

from Solution import Solution
import Find
from Plot_Wave import plot_wave
from State import State

class Riemann:
    """Definition of a 1D Riemann Problem:
    - W_left       : Left state
    - W_right      : Right state
    - W_left_star  : Left star region
    - W_right_star : Right star region
    - gamma        : Heat capacity ratio
    - P_star       : Pressure in region Left star and Right star
    - U_star       : Velocity in region Left star and Right star"""
    

    def __init__(self, rho_l, u_l, p_l, rho_r, u_r, p_r, gamma): 
            """Constructor of a Riemann Problem"""
            self.W_left = State("Left", gamma, rho_l, u_l, p_l)
            self.W_right = State("Right", gamma, rho_r, u_r, p_r)
            self.gamma = gamma
            self.P_star = Find.Find_P(self.W_left, self.W_right, gamma)
            self.U_star = Find.Find_U(self.W_left, self.W_right, self.P_star, gamma)

            if (self.P_star < self.W_right.pressure):
                #Rarefaction wave
                rho_star_r = self.W_right.rho * (self.P_star/self.W_right.pressure)**(1/gamma)
                self.W_right_star = State("Right star", gamma, rho_star_r, self.U_star, self.P_star)
            else:
                #Shock wave
                rho_star_r = self.W_right.rho * (self.P_star/self.W_right.pressure + (gamma-1)/(gamma+1))/((gamma-1)/(gamma+1) * self.P_star/self.W_right.pressure + 1)
                self.W_right_star =  State("Right star", gamma, rho_star_r, self.U_star, self.P_star)


            if (self.P_star < self.W_left.pressure):
                #Rarefaction wave
                rho_star_l = self.W_left.rho * (self.P_star/self.W_left.pressure)**(1/gamma)
                self.W_left_star =  State("Left star", gamma, rho_star_l, self.U_star, self.P_star)
            else:
                #Shock wave
                rho_star_l = self.W_left.rho * (self.P_star/self.W_left.pressure + (gamma-1)/(gamma+1))/((gamma-1)/(gamma+1) * self.P_star/self.W_left.pressure + 1)
                self.W_left_star =  State("Left star", gamma, rho_star_l, self.U_star, self.P_star)



    def eval_sampling_point(self, sampling_point):
            """Compute the state at a given sampling point x/t"""
            return Solution(self, sampling_point)

    def plot_time(self, X, x0, t, string):
            """Plot the repartition of density, velocity and pressure at a given time t, on a mesh X, where the origin of the discontinuity is in x0. Save raw data in a file."""

            f = open("../output/{}.txt".format(string), "w")
            f.write('%12s'%"x")
            f.write('%15s'%"rho")
            f.write('%15s'%"ux")
            f.write('%15s'%"p\n")


            Pressure = [Solution(self, (x-x0)/t).pressure for x in X]
            Velocity = [Solution(self, (x-x0)/t).velocity for x in X]
            Density = [Solution(self, (x-x0)/t).rho for x in X]

            for i in range(len(X)):
                f.write('%12.5E'%X[i])
                f.write('%15.5E'%Density[i])
                f.write('%15.5E'%Velocity[i])
                f.write('%15.5E'%Pressure[i])
                f.write("\n")


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

    def plot_diagram(self, X, x0, t2):
            """Plot the x-t diagram with the characteristics"""

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            axis = plt.gca()

            gamma = self.gamma
            if (self.P_star > self.W_left.pressure):
                #Left shock
                Speed_Shock = self.W_left.velocity - self.W_left.c * ((gamma+1)/(2*gamma) * (self.P_star/self.W_left.pressure) + (gamma-1)/(2*gamma))**.5
                plot_wave(Speed_Shock, X, x0, 0, 2, "Left Shock Wave")
            else:
                #Left expansion wave
                c_star_l  = self.W_left.c * (self.P_star/self.W_left.pressure)**((gamma-1)/(2*gamma))
                Speed_HL = self.W_left.velocity - self.W_left.c
                Speed_TL = self.U_star - c_star_l
                plot_wave(Speed_TL, X, x0, 0, 2, "Tail of the Left Expansion Wave")
                plot_wave(Speed_HL, X, x0, 0, 2, "Head of the Left Expansion Wave")

            if (self.P_star > self.W_right.pressure):
                #Right Shock
                Speed_Shock = self.W_right.velocity + self.W_right.c * ((gamma+1)/(2*gamma) * (self.P_star/self.W_right.pressure) + (gamma-1)/(2*gamma))**.5
                plot_wave(Speed_Shock, X, x0, 0, 2, "Right Shock Wave")
            else:
                #Right expansion wave
                c_star_r  = self.W_right.c * (self.P_star/self.W_right.pressure)**((gamma-1)/(2*gamma))
                Speed_HR = self.W_right.velocity + self.W_right.c
                Speed_TR = self.U_star + c_star_r
                plot_wave(Speed_TR, X, x0, 0, 2, "Tail of the Right Expansion Wave")
                plot_wave(Speed_HR, X, x0, 0, 2, "Head of the Right Expansion Wave")

            if (self.U_star != 0):
                plot_wave(self.U_star, X, x0, 0, 2, "Contact Surface")

            plt.grid()
            ax.spines['left'].set_position('center')
            ax.legend()
            plt.xlabel("Location x")
            plt.ylabel("Time t")
            


