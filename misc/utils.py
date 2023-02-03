def get_hcf(x, y):
  smaller = x if x < y else y
  for i in range(1, smaller + 1):
      if((x % i == 0) and (y % i == 0)): hcf = i 
  return hcf