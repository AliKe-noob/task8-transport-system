class Vehicle:

    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        brand (str): Марка транспортного средства
        model (str): Модель
        year (int): Год выпуска
        _current_speed (int): Текущая скорость (инкапсулирована)
        max_speed (int): Максимальная скорость
    """

    def __init__(self, brand, model, year, max_speed = None):
        self.brand = brand
        self.model = model
        self.year = year
        self.__current_speed = 0
        self.max_speed = max_speed

    def start(self):
        print("The engine started.")

    def stop(self):
        if self.__current_speed == 0:
            print("The engine never started. ")
        else:
            print("The engine stopped. ")

    def accelerate(self, speed):
        if speed < 0:
            print("Can't accelerate negatively. ")
        else:
            self.__current_speed += speed

    def brake(self, speed):
        if speed < 0:
            print("Cant brake by negative. ")
        else:
            self.__current_speed -= speed
            if self.__current_speed < 0:
                self.__current_speed = 0


    def info(self):
        print(f"""
Brand = {self.brand}
Model = {self.model}
Year = {self.year}
current_speed = {self.__current_speed}
max_speed = {self.max_speed}
              """)
        
#Testing
#car = Vehicle("Toyota", "Corolla", "2020", max_speed = 150)
#car.info()
#car.start()
#car.accelerate(100)
#car.info()
#car.brake(50)
#car.info()
#car.stop()