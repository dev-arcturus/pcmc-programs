from random import randint
from math import pi

def random_list(len, n):
  lst = []
  for i in range(len):
    lst.append(randint(0, n))
  return lst

def format_angle(theta: float):
  dtheta = theta * 180 / pi
  theta = round(theta, 2)
  dtheta = round(dtheta, 2)
  return f"about {dtheta}° or {theta} rad"