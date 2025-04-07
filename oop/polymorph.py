from typing import List
class Car:
  def __init__(self, make, model, year, num_of_doors=4):
    self.make = make
    self.model = model
    self.year = year
    self.num_of_doors = num_of_doors

  def start(self):
    print(f"{self.year} {self.make} {self.model} is starting.")

  def stop(self):
    print(f"{self.year} {self.make} {self.model} is stopping.")

class Motorbike():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def start_bike(self):
    print(f"{self.year} {self.make} {self.model} is starting.")

  def stop_bike(self):
    print(f"{self.year} {self.make} {self.model} is stopping.")


# Create instances of each class
car = Car("Toyota", "Corolla", 2005, 5)
bike = Motorbike("Honda", "CBR", 2020)
# Call methods on each instance
# car.start()
# car.stop()
# bike.start_bike()
# bike.stop_bike()

# vehicles = [car, bike, Car("Honda", "Civic", 2010), Motorbike("Yamaha", "R1", 2021)]

# for vehicle in vehicles:
#   if isinstance(vehicle, Car):
#     print(f"Inspecting {vehicle.make} {vehicle.model} ({type(vehicle).__name__})")
#     vehicle.start()
#   elif isinstance(vehicle, Motorbike):
#     print(f"Inspecting {vehicle.make} {vehicle.model} ({type(vehicle).__name__})")
#     vehicle.start_bike()
#   else:
#     raise Exception ("Object is not a valid vehicle type.")


class Vehicle():
  def __init__(self, make: str, model: str, year: int):
    self.make = make
    self.model = model
    self.year = year
  
  def start(self):
    print(f"{self.year} {self.make} {self.model} is starting.")

  def stop(self):
    print(f"{self.year} {self.make} {self.model} is stopping.")

class Car(Vehicle):
  def __init__(self, make, model, year, num_of_doors=4):
    super().__init__(make, model, year)
    self.num_of_doors = num_of_doors
  
  def start(self):
    print(f"car is starting.")

class Motorbike(Vehicle):
  def brake(self):
    print(f"{self.year} {self.make} {self.model} is braking.")
  # modify the start method to use the parent class's start method
  def start(self):
    print(f"bike is starting.")
    

vehicles: list[Vehicle] = [ Car("Honda", "Civic", 2010), Motorbike("Yamaha", "R1", 2021) ]

for vehicle in vehicles:
  print(f"Inspecting {vehicle.make} {vehicle.model} ({type(vehicle).__name__})")
  vehicle.start()
  # if isinstance(vehicle, Vehicle):
  #   print(f"Inspecting {vehicle.make} {vehicle.model} ({type(vehicle).__name__})")
  #   vehicle.start()
  # else:
  #   raise Exception ("Object is not a valid vehicle type.")
  if isinstance(vehicle, Motorbike):
    vehicle.brake()
  else:
    vehicle.stop()