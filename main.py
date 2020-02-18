import numpy as np
import matplotlib.pyplot as plt

from State import State
from Solution import Solution
from Riemann import Riemann
from General_Riemann import General_Riemann_Problem


#Solve of the Riemann Problem

#Problem 1
Riemann_problem = Riemann(8., 0, 480, 1., 0., 1., 5/3)

t = 0.04 
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = 0.0

Riemann_problem.plot_time(X, x0,  t, "RS1")
#Riemann_problem.plot_diagram(X, x0, 1)


#Problem 2
Riemann_problem = Riemann(1., -2., 0.4, 1., 2., 0.4, 1.4)

t = 0.15
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = 0.0

Riemann_problem.plot_time(X, x0,  t, "RS2")
#Riemann_problem.plot_diagram(X, x0, 1)


#Problem 3
Riemann_problem = Riemann(1., -19.59745, 1000., 1., -19.59745, 0.01, 1.4)

t = 0.012
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = 0.3

Riemann_problem.plot_time(X, x0,  t, "RS3")
#Riemann_problem.plot_diagram(X, x0, 1)

plt.show()
