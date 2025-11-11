from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year,cargo_capacity, num_wheels, current_speed=0, max_speed=None):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.cargo_capacity = cargo_capacity
        self.num_wheels = num_wheels

    def info(self):
        super().info()
        