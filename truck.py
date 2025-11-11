from vehicle import Vehicle

class Truck(Vehicle):

    """
    Класс грузовика, наследуется от Vehicle.

    Атрибуты:
        cargo_capacity (int): Вместимость груза в тоннах
        num_wheels (int): Количество колес
    """
    
    def __init__(self, brand, model, year,cargo_capacity, num_wheels, current_speed=0, max_speed=None):
        super().__init__(brand, model, year, current_speed, max_speed)
        self.cargo_capacity = cargo_capacity
        self.num_wheels = num_wheels

    def info(self):
        super().info()
        print(f"""
cargo_capacity: {self.cargo_capacity}
num_wheels: {self.num_wheels}
                  """)
        
    def load_cargo(self, amount):
        if amount > self.cargo_capacity:
            print("Amount exceeds cargo capacity limit. ")
        else:
            print(f"Successfully loaded {amount} tons. ")