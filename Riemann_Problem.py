import numpy as np
import math

class Riemann:


    def __init__(self, W_left, W_left_star, W_right_star, W_right, Left_Wave, Right_Wave): 

            self.W_left = W_left
            self.W_left_star = W_left_star
            self.W_right_star = W_right_star
            self.W_right = W_right
            
            self.Left_Wave = Left_Wave
            self.Right_Wave = Right_Wave
