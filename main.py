import numpy as np
import matplotlib.pyplot as plt

from Riemann import Riemann_Computation
from State import State
from Solution import Solution


#Solve of the Riemann Problem

#Problem 1
Riemann_problem = Riemann_Computation(1.0, 0.75, 1.0, 0.125, 0.0, 0.1, 1.4)


t = 0.2
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = -0.2

Riemann_problem.plot_time(X, x0,  t)

#Problem 1
#Riemann_problem = Riemann_Computation(8., 0, 480, 1., 0., 1., 5/3)


#t = 0.04
#N = 1000
#X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
#x0 = 0.0

#Riemann_problem.plot_time(X, x0,  t)


#Problem 2
#Riemann_problem = Riemann_Computation(1., -2., 0.4, 1., 2., 0.4, 1.4)


#t = 0.15
#N = 1000
#X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
#x0 = 0.0

#Riemann_problem.plot_time(X, x0,  t)


#Problem 3
#Riemann_problem = Riemann_Computation(1., -19.59745, 1000., 1., -19.59745, 0.01, 1.4)



#t = 0.012
#N = 1000
#X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
#x0 = 0.3

#Riemann_problem.plot_time(X, x0,  t)
