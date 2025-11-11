from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar, current_speed=0, max_speed=None):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print("The bike is doing a wheelie!!! ")
    
    def info(self):
        super().info()
        if self.has_sidecar == True:
            print("The motorcycle has a sidecar. ")
        else:
            print("Motorcycle doesn't have a sidecar. ")