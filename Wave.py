class Shock:

    def __init__(self, side, speed):
        self.speed = speed
        self.side = side

    def type(self):
        return 'Shock'

    def location(self, t):
        return self.speed * t

class Contact_Surface:

    def __init__(self, speed):
        self.U_star = speed

    def type(self):
        return 'Contact Surface'

    def location(self, t):
        return self.U_star * t

class Expansion_Fan:

    def __init__(self, side, speed_tail, speed_head, c_side, velocity_side, pressure_side, density_side):
        self.Side = side # +1 if right, -1 if left
        self.ST = speed_tail
        self.SH = speed_head
        
        self.c_side = c_side
        self.velocity_side = velocity_side
        self.pressure_side = pressure_side
        self.density_side = density_side
        

    def type(self):
        return 'Expansion Fan'

    def location(self, t):
        return (ST*t, SH*t)


    def velocity(self, gamma, sampling_point):
        return 2/(gamma+1) * (- self.Side * self.c_side + (gamma-1)/2*self.velocity_side + sampling_point)
        

    def pressure(self, gamma, sampling_point):
        return self.pressure_side * (2/(gamma+1) - self.Side* (gamma-1)/(gamma+1) * 1/self.c_side * (self.velocity_side - sampling_point))**(2*gamma/(gamma-1))

    def density(self, gamma, sampling_point):
        return self.density_side * (2/(gamma+1) - self.Side* (gamma-1)/(gamma+1) * 1/self.c_side * (self.velocity_side - sampling_point))**(2/gamma-1)

