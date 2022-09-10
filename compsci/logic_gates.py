def AND(x, y):
  return x and y

def OR(x, y):
  return x or y

def NOT(x):
  return not x

def NAND(x, y):
  return NOT(AND(x, y))

def XOR(x, y):
  return AND(OR(x, y), NAND(x, y))

def XNOR(x, y):
  return NOT(XOR(x, y))