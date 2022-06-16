from math import sqrt, atan, cos
from functools import reduce


class Vector():
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z

  def analytic_form(self):
    return self.__repr__()
  
  def get_magnitude(self):
    return round(sqrt(reduce(lambda x, y: x + y ** 2, [self.x, self.y, self.z])), 2)

  def get_theta(self):
    return atan(self.y / self.x)

  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return [x, y]

  def __sub__(self, other):
    x = self.x - other.x
    y = self.y - other.y
    return [x, y]
  
  def __mul__(self, other):
    x = self.x * other.x
    y = self.y * other.y
    return [x, y]
  
  def __truediv__(self, other):
    x= self.x / other.x
    y = self.y / other.y
    return [x, y]
  
  def __str__(self):
    [x, y, z] = [self.x, self.y, self.z]
    if z == 0: return f'({x}, {y})'
    return f'({x}, {y}, {z})' 

  def __repr__(self):
    [x, y, z] = [self.x, self.y, self.z]
    if z == 0: return f'{x}î + {y}ĵ'
    return f'{x}î + {y}ĵ + {z}k̂'

def get_magnitude_of_resultant_vector(A: Vector, B: Vector):
  mA, mB = [x.get_magnitude() for x in [A, B]]
  return round(sqrt(mA ** 2 + mB ** 2 + 2 * mA * mB * cos(B.get_theta())), 2)