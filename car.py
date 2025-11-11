from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year,  num_doors, fuel_type, current_speed=0, max_speed=None):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

        def info(self):
            super().info()
            print(f"""
Number of doors: {num_doors}
fuel_type: {fuel_type}
                  """)
            
myCar = Car("Toyota", "Corolla", 2020, 4, "Diezel", max_speed = 150)
myCar.info()
