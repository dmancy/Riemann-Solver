import numpy as np
import matplotlib.pyplot as plt

from Riemann import Riemann_Computation
from State import State
from Solution import Solution



Riemann_problem = Riemann_Computation(5.81, 0, 5*10**5, 1.16, 0, 100*10**3, 1.4)

State = Solution(Riemann_problem, 487.1)

t = 3*10**-3
X = np.linspace(-2,2,1000)
Y = [Solution(Riemann_problem,x/t).u for x in X] 

plt.plot(X,Y)
plt.grid()
plt.xlabel("x")
plt.show()

