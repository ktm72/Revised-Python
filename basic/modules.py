from math import sqrt, pi
import kansas

def circle_area(radius):
  return pi * radius ** 2

def circle_circumference(radius):
  return 2 * pi * radius

def circle_diameter(radius):
  return 2 * radius

def circle_radius(area):
  return sqrt(area / pi)

def circle_properties(radius):
  return {
    'area': circle_area(radius),
    'circumference': circle_circumference(radius),
    'diameter': circle_diameter(radius),
    'radius': radius
  }

print(f"Circle properties for radius 5: {circle_properties(5)}")

import random as rdm

# for item in dir(rdm):
#   if not item.startswith('_'):
#     print(item)

print(kansas.flower)
print("Random fun fact about Kansas:")
kansas.randomfunfact()