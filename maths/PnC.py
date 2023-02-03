from math import factorial as f

def combinations(n: int, r: int):
  return f(n) // (f(r) * f(n - r))

def permutations(n: int, r: int):
  return f(n) // f(n - r)