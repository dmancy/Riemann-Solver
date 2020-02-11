import numpy as np
import matplotlib.pyplot as plt
from State import State
import Wave
from Riemann_Problem import Riemann

def function_F(W, gamma, P_eval):
    #Evaluation of the function f
    if (P_eval > W.pressure):
        return (P_eval - W.pressure) * (2/((gamma+1) * W.rho) / (P_eval + (gamma-1)/(gamma+1) * W.pressure))**.5
    else:
        return (2*W.c/(gamma-1)) * ((P_eval/W.pressure)**((gamma-1)/(2*gamma)) - 1)


def derivative_F(W, gamma, P_eval):
    #Evaluation of the derivative of f
    if (P_eval > W.pressure):
        return (2/((gamma+1) * W.rho) / (P_eval + (gamma-1)/(gamma+1) * W.pressure))**.5 * (1 - (P_eval - W.pressure)/(2*(P_eval + (gamma-1)/(gamma+1) * W.pressure)))
    else:
        return  1/(W.rho * W.c) * (P_eval/W.pressure)**(-(gamma+1)/(2*gamma))


def Find_P(W_left, W_right, gamma):
    #Find P around the contact surface

    #Acoustic approximation
    P0 = (W_left.pressure * W_right.rho * W_right.c + W_right.pressure * W_left.rho * W_left.c + (W_left.velocity - W_right.velocity) * W_right.rho * W_right.c * W_left.rho * W_left.c)/(W_left.rho * W_left.c + W_right.rho * W_right.c)

    P0 = 0.000001
    epsilon = 1
    count = 0

    while (epsilon > 10**-6 and count < 1000):

        P1 = P0 - (W_right.velocity - W_left.velocity + function_F(W_left, gamma, P0) + function_F(W_right, gamma, P0))/(derivative_F(W_left, gamma, P0) + derivative_F(W_right, gamma, P0))

        epsilon = abs(P1 - P0)/P0
        P0 = P1
        count+= 1

    return P1

def Find_U(W_left, W_right, P_star, gamma):
    #Compute U around the contact surface

    return .5*(W_left.velocity + W_right.velocity) + .5*(function_F(W_right, gamma, P_star) - function_F(W_left, gamma, P_star))




def Riemann_Computation(rho_l, u_l, p_l, rho_r, u_r, p_r, gamma):
    #Determine the types of waves involved in the Riemann problem as well as conditions between those waves

    W_left = State("Left", gamma, rho_l, u_l, p_l)
    W_right = State("Right", gamma, rho_r, u_r, p_r)

    #Compute P_star and U_star
    P_star = Find_P(W_left, W_right, gamma)
    U_star = Find_U(W_left, W_right, P_star, gamma)

    #Define the right and left waves, as well as the states right and left of the Contact surface
    if (P_star > W_left.pressure):
        #Left shock wave
        rho_star_l = W_left.rho * (P_star/W_left.pressure + (gamma-1)/(gamma+1))/((gamma-1)/(gamma+1) * P_star/W_left.pressure + 1)
        S_L = W_left.velocity - W_left.c * ((gamma+1)/(2*gamma) * (P_star/W_left.pressure) + (gamma-1)/(2*gamma))**.5
        Left_Wave = Wave.Shock(-1, S_L)
        W_left_star = State("Left star", gamma, rho_star_l, U_star, P_star)

    else:
        #Left rarefaction wave
        rho_star_l = W_left.rho * (P_star/W_left.pressure)**(1/gamma)
        c_star_l  = W_left.c * (P_star/W_left.pressure)**((gamma-1)/(2*gamma))
        S_HL = W_left.velocity - W_left.c
        S_TL = U_star - c_star_l

        Left_Wave = Wave.Expansion_Fan(-1, S_TL, S_HL, W_left.c, W_left.velocity, W_left.pressure, W_left.rho)
        W_left_star = State("Left star", gamma, rho_star_l, U_star, P_star)



    if (P_star > W_right.pressure):
        #Right shock wave
        rho_star_r = W_right.rho * (P_star/W_right.pressure + (gamma-1)/(gamma+1))/((gamma-1)/(gamma+1) * P_star/W_right.pressure + 1)
        S_R = W_right.velocity + W_right.c * ((gamma+1)/(2*gamma) * (P_star/W_right.pressure) + (gamma-1)/(2*gamma))**.5

        Right_Wave = Wave.Shock(1, S_R)
        W_right_star = State("Right star", gamma, rho_star_r, U_star, P_star)

    else:
        #Right rarefaction wave
        rho_star_r = W_right.rho * (P_star/W_right.pressure)**(1/gamma)
        c_star_r  = W_right.c * (P_star/W_right.pressure)**((gamma-1)/(2*gamma))
        S_HR = W_right.velocity + W_right.c
        S_TR = U_star + c_star_r

        Right_Wave = Wave.Expansion_Fan(1, S_TR, S_HR, W_right.c, W_right.velocity, W_right.pressure, W_right.rho)
        W_right_star = State("Right star", gamma, rho_star_r, U_star, P_star)

    #Creation of a Riemann instance
    R1 = Riemann(W_left, W_left_star, W_right_star, W_right, Left_Wave, Right_Wave)

    return R1
    
