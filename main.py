import numpy as np
import matplotlib.pyplot as plt

from Riemann import Riemann_Computation
from State import State
from Solution import Solution


#Solve of the Riemann Problem
Riemann_problem = Riemann_Computation(8., 0., 480., 1., 0., 1., 5/3)

t = 0.04
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
Y = [Solution(Riemann_problem, x/t).p for x in X] 

Riemann_problem.plot_time(X, t)
