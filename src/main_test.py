import numpy as np
import matplotlib.pyplot as plt

from State import State
from Solution import Solution
from Riemann import Riemann


#Solve of the Riemann Problem

#Problem 1

#Riemann_problem = Riemann_Computation(1.0, 0.75, 1.0, 0.125, 0.0, 0.1, 1.4)


#t = 0.2
#N = 1000
#X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
#x0 = -0.2

#Riemann_problem.plot_time(X, x0,  t)

#Problem 1
Riemann_problem = Riemann(5.99924, 19.5975, 460.894, 5.99242, -6.19633, 46.0950, 1.4)


t = 0.035
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = -.1

Riemann_problem.plot_time(X, x0,  t, "RS1")
Riemann_problem.plot_diagram(X, x0, 1)


#Problem 2
Riemann_problem = Riemann(1., 0.75, 1.0, .125, 0.0, 0.1, 1.4)

t = 0.2
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = -0.2

Riemann_problem.plot_time(X, x0,  t, "RS2")
Riemann_problem.plot_diagram(X, x0, 1)


#Problem 3
Riemann_problem = Riemann(1., 0.0, 0.01, 1., 0.0, 100., 1.4)

t = 0.035
N = 1000
X = [-.5 + 1./N * (i - 0.5) for i in range(1, N+1)]
x0 = 0.0

Riemann_problem.plot_time(X, x0,  t, "RS3")
Riemann_problem.plot_diagram(X, x0, 1)

plt.show()
