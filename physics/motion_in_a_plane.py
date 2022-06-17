from math import degrees, sin, sqrt, atan, cos
from functools import reduce


class Vector():
  def __init__(self, x=0, y=0, z=0):
    if x == 0: raise Exception('x cannot be 0')
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
    return [self.x + other.x, self.y + other.y]

  def __sub__(self, other):
    return [self.x - other.x, self.y - other.y]
  
  def __mul__(self, other):
    return [self.x * other.x, self.y * other.y]
  
  def __truediv__(self, other):
    return [self.x / other.x, self.y / other.y]
  
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

def get_alpha(A: Vector, B: Vector):
  mA, mB, theta = [*[x.get_magnitude() for x in [A, B]], B.get_theta()]
  return degrees(atan(mB * sin(theta) / (mA + mB * cos(theta))))

print(get_alpha(Vector(1, 1), Vector(2, 1)))