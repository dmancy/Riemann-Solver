import numpy as np
import matplotlib.pyplot as plt

from State import State
from Solution import Solution
from Riemann import Riemann


def General_Riemann_Problem(rho_l, u_l, p_l, rho_r, u_r, p_r, gamma, sampling_point): 
    """return the state (rho, u, p) of the Riemann problem at x/t = sampling_point"""

    Riemann_Problem = Riemann(rho_l, u_l, p_l, rho_r, u_r, p_r, gamma) 

    W_Solution = Solution(Riemann_Problem, sampling_point)

    return (W_Solution.rho, W_Solution.velocity, W_Solution.pressure)

