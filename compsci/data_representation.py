bits = "0123456789ABCDEF"

def from_decimal(x, base):
  if x == 0: return "0"
  if x < 0: x, base = -x, base * -1
  result = ""
  while x > 0:
    result = bits[x % base] + result
    x //= base
  return result

def to_decimal(x, base):
  result = 0
  for i, c in enumerate(x): result += bits.index(c) * (base ** (len(x) - i - 1))
  return result