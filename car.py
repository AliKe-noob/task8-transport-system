from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year,  num_doors, fuel_type, current_speed=0, max_speed=None):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def info(self):
        super().info()
        print(f"""
Number of doors: {self.num_doors}
fuel_type: {self.fuel_type}
                  """)
        
    def honk(self):
        print("The car made 'Honk!' sound. ")