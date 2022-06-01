from random import random
from math import sqrt

def approx_pi(i: int):
  outside_circle = 0

  for _ in range(i):
    x = random()
    y = random()
    h = sqrt(x**2 + y**2)
    if h > 1: outside_circle += 1

  return (i - outside_circle) / i * 4

# the higher the iteration count, the more precise the approximation and the longer the code will take to run
# degree increases exponentially, an increase in degree would increase the execution time by 10 times
degree = 10

print(approx_pi(10 ** degree))