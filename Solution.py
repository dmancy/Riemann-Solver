import math
import numpy as np
from Riemann import Riemann_Computation
from State import State


def Solution(Riemann_problem, sampling_point):

        gamma = Riemann_problem.W_right.gamma

        if (sampling_point < Riemann_problem.W_left_star.u):
            #We are on the left from CS

            if (Riemann_problem.W_left_star.p < Riemann_problem.W_left.p):
                #Left fan
                if (sampling_point < Riemann_problem.Left_Wave.SH):
                    return Riemann_problem.W_left

                elif (sampling_point > Riemann_problem.Left_Wave.ST):
                    return Riemann_problem.W_left_star

                else:

                    rho = Riemann_problem.Left_Wave.density(gamma, sampling_point)

                    u = Riemann_problem.Left_Wave.velocity(gamma, sampling_point)
                    p = Riemann_problem.Left_Wave.pressure(gamma, sampling_point)

                    return State("Expansion Fan", gamma, rho, u, p)

            else:
                if(sampling_point < Riemann_problem.Left_Wave.speed):
                    return Riemann_problem.W_left
                else:
                    return Riemann_problem.W_left_star

        else:
            #We are on the right from CS

            if (Riemann_problem.W_right_star.p < Riemann_problem.W_right.p):
                #Right fan
                if (sampling_point > Riemann_problem.Right_Wave.SH):
                    return Riemann_problem.W_right

                elif (sampling_point < Riemann_problem.Right_Wave.ST):
                    return Riemann_problem.W_right_star

                else:

                    rho = Riemann_problem.Right_Wave.density(gamma, sampling_point)

                    u = Riemann_problem.Right_Wave.velocity(gamma, sampling_point)
                    p = Riemann_problem.Right_Wave.pressure(gamma, sampling_point)

                    return State("Expansion Fan", gamma, rho, u, p)
            else:
                if(sampling_point > Riemann_problem.Right_Wave.speed):
                    return Riemann_problem.W_right
                else:
                    return Riemann_problem.W_right_star

