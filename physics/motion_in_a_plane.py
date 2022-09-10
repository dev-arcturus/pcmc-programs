from math import degrees, radians, sin, sqrt, atan, cos
from functools import reduce

deg = degrees

class Vector():
  def __init__(self, x=0, y=0, z=0):
      self.x, self.y, self.z = x, y, z

  def scalar(self):
      return [abs(self.x), abs(self.y), abs(self.z)]

  def analytic(self):
      return self.__repr__()

  def mag(self):
      return round(sqrt(reduce(lambda x, y: x + y ** 2, [0, self.x, self.y, self.z])), 2)

  def theta(self):
      return degrees(atan(self.y / self.x))

  def __str__(self):
      [x, y, z] = [self.x, self.y, self.z]
      if z == 0:
          return f'({x}, {y})'
      return f'({x}, {y}, {z})'

  def __repr__(self):
      [x, y, z] = [self.x, self.y, self.z]
      if z == 0:
          return f'{x}î + {y}ĵ'
      return f'{x}î + {y}ĵ + {z}k̂'

  def __add__(self, other):
      return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

  def __sub__(self, other):
      return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

  def __mul__(self, other):
      return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

  def __truediv__(self, other):
      return Vector(self.x / other.x, self.y / other.y, self.z / other.z)


def magn_of_resultant(A: Vector, B: Vector):
  mA, mB = [x.mag() for x in [A, B]]
  return round(sqrt(mA ** 2 + mB ** 2 + 2 * mA * mB * cos(B.theta())), 2)


def get_alpha(A: Vector, B: Vector):
  mA, mB, theta = [*[x.mag() for x in [A, B]], radians(B.theta())]
  return deg(atan(mB * sin(theta) / (mA + mB * cos(theta))))


def dotP(A: Vector, B: Vector, angle: int): return A.mag() * B.mag() * cos(radians(angle))


def crossP(A: Vector, B: Vector):
  return Vector(A.y * B.z - A.z * B.y, A.z * B.x - A.x * B.z, A.x * B.y - A.y * B.x)
