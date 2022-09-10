from operator import add
from random import random
from math import sqrt


def approx_pi(i: int):
    outside_circle = 0

    for _ in range(i):
        if sqrt(add(*[random() ** 2 for _ in range(2)])) > 1:
            outside_circle += 1

    return (i - outside_circle) / i * 4


# the higher the degree, the more precise the approximation; degree scales exponentially at O(10^n)
degree = 10

print(approx_pi(10 ** degree))
