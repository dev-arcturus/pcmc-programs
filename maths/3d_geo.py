from utils import random_list
from math import sqrt

class Point():
  def __init__(self, x: float, y: float, z: float):
    self.x, self.y, self.z = self.coords = x, y, z

  def __repr__(self) -> str:
    return f"{self.coords}"

def gen_point():
  x, y, z = random_list(3, 10)
  return Point(x, y, z)

def distance_between(p1: Point, p2: Point):
  x1, y1, z1 = p1.coords
  x2, y2, z2 = p2.coords

  return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), 2)

a, b = gen_point(), gen_point()

print(a, b, distance_between(a, b))