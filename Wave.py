class Shock:

    def __init__(self, speed):
        self.S = speed

    def type(self):
        return 'Shock'

    def location(self, t):
        return self.S * t

class Contact_Surface:

    def __init__(self, speed):
        self.U_star = speed

    def type(self):
        return 'Contact Surface'

    def location(self, t):
        return self.U_star * t

class Expansion_Fan:

    def __init__(self, speed_tail, speed_head):
        self.ST = speed_tail
        self.SH = speed_head

    def type(self):
        return 'Expansion Fan'

    def location(self, t):
        return (ST*t, SH*t)
