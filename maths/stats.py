from random import randint
from math import sqrt

def gen(n=10):
  return [randint(0, 100) for _ in range(n)]

def mean(l: list[int]):
  sum_ = 0
  for x in l: sum_ += x 
  return sum_ / len(l)

def median(l: list[int]):
  leng = len(l)
  l.sort()
  if leng % 2 == 0:
    return (l[leng // 2 - 1] + l[leng // 2]) / 2
  else:
    return l[(leng + 1) // 2 - 1]

def deviation(l: list[int], use_median=False):
  m = mean(l) if use_median else median(l)
  sum_ = 0
  for x in l:
    sum_ += abs(x - m)
  return(sum_ / len(l))

def standard_deviation(l: list[int]):
  m = mean(l)
  sum_ = 0
  for x in l:
    sum_ += abs(x - m)
  return(sqrt(sum_ ** 2 / len(l)))


l = gen()
print(l)
print(deviation(l))