import numpy as np
import matplotlib.pyplot as plt

from Riemann import Riemann_Computation
from State import State
from Solution import Solution



#Riemann_Computation(5.81, 0, 5*10**5, 1.16, 0, 100*10**3, 1.4, 0.5)
Riemann_problem = Riemann_Computation(5.81, 0, 5*10**5, 1.16, 0, 100*10**3, 1.4)

State = Solution(Riemann_problem, 1000000000)

State.print()
