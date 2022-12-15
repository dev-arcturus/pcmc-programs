from sets import *

S = create((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

A = create((1, 3, 0))
B = create((7, 8, 6))

def P(A: set):
  if not is_subset(A, S): raise Exception
  return len(A) / len(S)

print(P(intersection(A, B)))