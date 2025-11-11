# Transport System Project

## Overview
This project implements a simple transport system in Python using object-oriented programming principles. 
It includes a base class `Vehicle` and derived classes `Car`, `Motorcycle`, and `Truck`. 
Each class has its own attributes and methods, demonstrating inheritance, encapsulation, and method overriding.

## Classes

### Vehicle
**Description:** Base class for all vehicles.

**Attributes:**
- `brand` (str): Brand of the vehicle
- `model` (str): Model of the vehicle
- `year` (int): Year of manufacture
- `_current_speed` (int, private): Current speed
- `max_speed` (int): Maximum speed

**Methods:**
- `start()`: Starts the engine
- `stop()`: Stops the engine
- `accelerate(speed)`: Increases speed
- `brake(speed)`: Decreases speed
- `info()`: Prints vehicle information

### Car
**Description:** Inherits from `Vehicle`, represents a car.

**Attributes:**
- `num_doors` (int): Number of doors
- `fuel_type` (str): Type of fuel

**Methods:**
- `info()`: Overrides `Vehicle.info()`, adds car-specific info
- `honk()`: Prints "Honk!" sound

### Motorcycle
**Description:** Inherits from `Vehicle`, represents a motorcycle.

**Attributes:**
- `has_sidecar` (bool): Whether the motorcycle has a sidecar

**Methods:**
- `info()`: Overrides `Vehicle.info()`, prints sidecar information
- `wheelie()`: Prints wheelie action (cannot do wheelie if sidecar is attached)

### Truck
**Description:** Inherits from `Vehicle`, represents a truck.

**Attributes:**
- `cargo_capacity` (int): Maximum cargo capacity in tons
- `num_wheels` (int): Number of wheels

**Methods:**
- `info()`: Overrides `Vehicle.info()`, adds truck-specific info
- `load_cargo(amount)`: Loads cargo if within capacity, prints status

## Usage
```python
from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

myCar = Car("Toyota", "Corolla", 2020, 4, "Diesel", max_speed=150)
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
