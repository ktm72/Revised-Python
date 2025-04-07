# Object Oriented Programming
# Class: A blueprint for creating objects
# Object: An instance of a class
# Attributes: Variables that belong to the class
# Methods: Functions that belong to the class
class Dog:
  def __init__(self, name, breed, owner):
    self.owner = owner
    self.name = name
    self.breed = breed
    print(self.name + " Dog created")
  # def __del__(self):
  #   print(self.name + "Dog destroyed")
  # def __str__(self):
  #   return "Dog object"
  # def __repr__(self):
  #   return "Dog object representation"

  def bark(self):
    print("Woof! Woof!")
  def wag_tail(self):
    print("Wagging tail")
  def fetch(self, item):
    print(f"Fetching {item}")
  def sit(self):
    print("Sitting")
  def roll_over(self):
    print("Rolling over")
  def play_dead(self):
    print("Playing dead")
  def shake(self):
    print("Shaking hands")
  def jump(self):
    print("Jumping")
  def spin(self):
    print("Spinning")
  def dig(self):
    print("Digging")

class Owner:
  def __init__(self, name, address, phone):
    self.name = name
    self.address = address
    self.phone = phone
    print(self.name + " Owner created")


owner1 = Owner('Alice', '123 Main St', '555-1234')
dog1 = Dog('Buddy', 'Golden Retriever', owner1)
print(dog1.owner.name)
dog1.bark()

owner2 = Owner('Bob', '456 Elm St', '555-5678')
dog2 = Dog('Max', 'Labrador', owner2)
dog2.wag_tail()

owner3 = Owner('Jhon', '789 Oak St', '555-9012')
dog3 = Dog('Charlie', 'Beagle', owner3)
dog3.fetch("ball")
# dog4 = Dog('Rocky', 'Bulldog')
# dog4.sit()
# dog5 = Dog('Daisy', 'Poodle')
# dog5.roll_over()
# dog6 = Dog('Bella', 'German Shepherd')
# dog6.play_dead()