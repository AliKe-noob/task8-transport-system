class Vehicle:
    def __init__(self, brand, model, year, current_speed = 0, max_speed = None):
        self.brand = brand
        self.model = model
        self.year = year
        self.current_speed = current_speed
        self.max_speed = max_speed

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
        else:
            self.current_speed += speed

    def brake(self, speed):
        if speed < 0:
            print("Cant brake by negative. ")
        else:
            self.current_speed -= speed
            if self.current_speed < 0:
                self.current_speed = 0


    def info(self, speed):
        print(f"""
Brand = {self.brand}
Model = {self.model}

              """)