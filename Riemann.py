import numpy as np
import matplotlib.pyplot as plt
from State import State
import Wave
from Riemann_Problem import Riemann

def function_F(W, gamma, P_eval):
    #Evaluation of the function
    if (P_eval > W.p):
        return (P_eval - W.p) * (2/((gamma+1) * W.rho) / (P_eval + (gamma-1)/(gamma+1) * W.p))**.5
    else:
        return (2*W.c/(gamma-1)) * ((P_eval/W.p)**((gamma-1)/(2*gamma)) - 1)



def derivative_F(W, gamma, P_eval):
    #Evaluation of the derivative
    if (P_eval > W.p):
        return (2/((gamma+1) * W.rho) / (P_eval + (gamma-1)/(gamma+1) * W.p))**.5 * (1 - (P_eval - W.p)/(2*(P_eval + (gamma-1)/(gamma+1) * W.p)))
    else:
        return  1/(W.rho * W.c) * (P_eval/W.p)**(-(gamma+1)/(2*gamma))


def Find_P(W_left, W_right, gamma):

    #Acoustic approximation
    P0 = (W_left.p * W_left.rho * W_left.c + W_right.p * W_right.rho * W_right.c + (W_left.u - W_right.u) * W_right.rho * W_right.c * W_left.rho * W_left.c)/(W_left.rho * W_left.c + W_right.rho * W_right.c)

    epsilon = 1

    while (epsilon > 10**-6):

        P1 = P0 - (function_F(W_left, gamma, P0) + function_F(W_right, gamma, P0))/(derivative_F(W_left, gamma, P0) + derivative_F(W_right, gamma, P0))

        epsilon = abs(P1 - P0)/P0
        P0 = P1

    return P1

def Find_U(W_left, W_right, P_star, gamma):

    return .5*(W_left.u + W_right.u) + .5*(function_F(W_right, gamma, P_star) - function_F(W_left, gamma, P_star))




def Riemann_Computation(rho_l, u_l, p_l, rho_r, u_r, p_r, gamma):

    W_left = State("Left", gamma, rho_l, u_l, p_l)
    W_right = State("Right", gamma, rho_r, u_r, p_r)
#    W_left.print()
#    W_right.print()

    #Compute P_star and U_star
    P_star = Find_P(W_left, W_right, gamma)
    U_star = Find_U(W_left, W_right, P_star, gamma)

    #Define the right and left waves, as well as the states right and left of the Ccontact_surface

    if (P_star > W_left.p):
        #Left shock wave
        rho_star_l = W_left.rho * (P_star/W_left.p + (gamma-1)/(gamma+1))/((gamma-1)/(gamma+1) * P_star/W_left.p + 1)
        S_L = W_left.c * ((gamma+1)/(2*gamma) * (P_star/W_left.p) + (gamma-1)/(2*gamma))**.5

        Left_Wave = Wave.Shock(-1, S_L)
        W_left_star = State("Left star", gamma, rho_star_l, U_star, P_star)

    else:
        #Left rarefaction wave
        rho_star_l = W_left.rho * (P_star/W_left.p)**(1/gamma)
        c_star_l  = W_left.c * (P_star/W_left.p)**((gamma-1)/(2*gamma))
        S_HL = W_left.u - W_left.c
        S_TL = U_star - c_star_l

        Left_Wave = Wave.Expansion_Fan(-1, S_TL, S_HL, W_left.c, W_left.u, W_left.p, W_left.rho)
        W_left_star = State("Left star", gamma, rho_star_l, U_star, P_star)



    if (P_star > W_right.p):
        #Right shock wave
        rho_star_r = W_right.rho * (P_star/W_right.p + (gamma-1)/(gamma+1))/((gamma-1)/(gamma+1) * P_star/W_right.p + 1)
        S_R = W_right.c * ((gamma+1)/(2*gamma) * (P_star/W_right.p) + (gamma-1)/(2*gamma))**.5

        Right_Wave = Wave.Shock(1, S_R)
        W_right_star = State("Right star", gamma, rho_star_r, U_star, P_star)

    else:
        #Right rarefaction wave
        rho_star_r = W_right.rho * (P_star/W_right.p)**(1/gamma)
        c_star_r  = W_right.c * (P_star/W_right.p)**((gamma-1)/(2*gamma))
        S_HR = W_right.u - W_right.c
        S_TR = U_star - c_star_r

        Right_Shock = Wave.Expansion_Fan(1, S_TR, S_HR, W_right.c, W_right.u, W_right.p, W_right.rho)
        W_right_star = State("Right star", gamma, rho_star_r, U_star, P_star)

    R1 = Riemann(W_left, W_left_star, W_right_star, W_right, Left_Wave, Right_Wave)

    return R1
    




#Riemann_Computation(5.81, 0, 5*10**5, 1.16, 0, 100*10**3, 1.4, 0.5)


	
