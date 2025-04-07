# This script demonstrates the use of classes and inheritance in Python.
# It defines a base class `Person` and two derived classes `Student` and `Teacher`.
# Each class has its own attributes and methods, showcasing how to use inheritance and method overriding.
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Hello, my name is {self.name}.")

class Student(Person):
  def __init__(self, name, student_id):
    super().__init__(name)
    self.student_id = student_id

  def study(self):
    print(f"{self.name} is studying.")

class Teacher(Person):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

  def teach(self):
    print(f"{self.name} is teaching {self.subject}.")

person1 = Person("Alice")
person1.greet()
student1 = Student("Bob", "S123")
student1.greet()
student1.study()
teacher1 = Teacher("Charlie", "Math")
teacher1.greet()
teacher1.teach()


class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model
    self.speed = 0

  def accelerate(self, amount):
    self.speed += amount
    print(f"{self.make} {self.model} accelerates to {self.speed} km/h")

class SportsCar(Car):
  def accelerate(self, amount):
    self.speed += amount * 2
    print(f"{self.make} {self.model} accelerates to {self.speed} km/h with turbo boost!")

class Truck(Car):
  def accelerate(self, amount):
    self.speed += amount * 0.5
    print(f"{self.make} {self.model} accelerates to {self.speed} km/h with heavy load!")

class ElectricCar(Car):
  def __init__(self, make, model, battery_capacity):
    super().__init__(make, model)
    self.battery_capacity = battery_capacity

  def charge(self, amount):
    self.battery_capacity += amount
    print(f"{self.make} {self.model} charges to {self.battery_capacity} kWh")

  def accelerate(self, amount):
    self.speed += amount * 1.5
    print(f"{self.make} {self.model} accelerates to {self.speed} km/h with electric power!")

# Create instances of each class
car = Car("Toyota", "Corolla")
sports_car = SportsCar("Porsche", "911")
truck = Truck("Ford", "F-150")
electric_car = ElectricCar("Tesla", "Model S", 100)
# Call methods on each instance
car.accelerate(20)
sports_car.accelerate(30)
truck.accelerate(10)
truck.accelerate(10)