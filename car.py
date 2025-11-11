from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, current_speed=0, max_speed=None, num_doors, fuel_type):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
