class Vehicle:
    def __init__(self, brand, model, year, current_speed = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.current_speed = current_speed

    def start(self):
        print("The engine started.")

    def stop(self):
        if self.current_speed == 0:
            print("The engine never started. ")
        else:
            print("The engine stopped. ")

    def accelerate(self, speed):
        if speed < 0:
            print("Can't accelerate negatively. ")

    def brake(self):

    def info(self, speed):
        print("")