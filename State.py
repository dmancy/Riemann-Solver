import math

class State:
    """Define the state of an area by:
    - gamma
    - density rho
    - velocity u
    - pressure p
    - Temperature T
    - sound speed c"""

    def __init__(self, title, gam, density, velocity, pressure):
        """Constructor"""
        self.name = title
        self.gamma = gam
        self.R = 287.058
        self.rho = density
        self.u = velocity
        self.p = pressure
        self.T = self.p/(self.R * self.rho)
        self.c = math.sqrt(self.gamma * self.R * self.T)

    def print(self):
        print("State : {} \nDensity : {} \nVelocity : {} \nPressure : {} \nTemperature : {} \nSound speed : {}\n".format(self.name, self.rho, self.u, self.p, self.T, self.c))
