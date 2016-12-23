from vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self):
        self.carry_limit = 0
        self.current_carriage_weight = 0

    def attach_carriage(self, weight):
        if weight <= self.carry_limit:
            self.current_carriage_weight = weight
            return True
        return False

    def detach_carriage(self):
        self.current_carriage_weight = None

    def has_carriage(self):
        if self.current_carriage_weight > 0:
            return True
        return False