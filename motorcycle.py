from vehicle import Vehicle

class Motorcycle(Vehicle):

    """
    Класс мотоцикла, наследуется от Vehicle.

    Атрибуты:
        has_sidecar (bool): Наличие бокового прицепа
    """

    def __init__(self, brand, model, year, has_sidecar, current_speed=0, max_speed=None):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.has_sidecar = has_sidecar

    def info(self):
        super().info()
        if self.has_sidecar == True:
            print("The motorcycle has a sidecar. ")
        else:
            print("Motorcycle doesn't have a sidecar. ")

    def wheelie(self):
        if self.has_sidecar == False:
            print("The bike is doing a wheelie!!! ")
        else:
            print("Can't, there is a sidecar. ")