bits = "0123456789ABCDEF"

def convert_decimal(x, base):
  if x == 0: return "0"
  if x < 0: x, base = -x, base * -1
  result = ""
  while x > 0:
    result = bits[x % base] + result
    x //= base
  return result
