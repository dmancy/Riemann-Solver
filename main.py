import numpy as np
import matplotlib.pyplot as plt

from Riemann import Riemann_Computation
from State import State
from Solution import Solution


#Solve of the Riemann Problem

#Problem 3
#Riemann_problem = Riemann_Computation(1., -19.59745, 1000., 1., -19.59745, 0.01, 1.4)



#t = 0.012
#N = 1000
#X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
#x0 = 0.3

#Riemann_problem.plot_time(X, x0,  t)

#Problem 2
Riemann_problem = Riemann_Computation(1., -2., 0.4, 1., 2., 0.4, 1.4)

print(Riemann_problem.Left_Wave.type())
print(Riemann_problem.Right_Wave.type())

t = 0.15
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = 0.0

Riemann_problem.plot_time(X, x0,  t)
