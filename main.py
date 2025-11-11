from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

myCar = Car("Toyota", "Corolla", 2020, 4, "Diezel", max_speed=150)
myTruck = Truck("Volvo", "FH16", 2021, cargo_capacity=25000, num_wheels=8, max_speed=120)
myMotorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, has_sidecar=True, max_speed=200)

vehicles = [myCar, myTruck, myMotorcycle]

for vehicle in vehicles:
    vehicle.start() 
    vehicle.accelerate(60) 
    vehicle.info()
    vehicle.brake(40)
    vehicle.info()
    print()

    myCar.honk()
    myMotorcycle.wheelie()
    myTruck.load_cargo(15000)
    myTruck.info()