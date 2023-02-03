from math import atan
from random import randint as r
from utils import format_angle

class Line():
  def __init__(self, x: float, y: float, c: float):
    self.a = x
    self.b = y
    self.c = c
    self.slope = -1 * self.a / self.b
    self.y_intercept = -1 * self.c / self.b

  def __repr__(self) -> str:
    return f"{self.a}x + {self.b}y + {self.c} = 0"

l1 = Line(r(1, 10), r(1, 10), r(1, 100))
l2 = Line(r(1, 10), r(1, 10), r(1, 100))

def angle_between_lines(l1: Line, l2: Line):
  m1, m2  = l1.slope, l2.slope
  return atan(abs(m1 - m2) / (1 + m1 * m2))

print(l1, l2, sep="\n")

print(format_angle(angle_between_lines(l1, l2)))


