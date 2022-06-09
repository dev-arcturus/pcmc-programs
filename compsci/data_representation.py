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
  for i, c in enumerate(x):result += bits.index(c) * (base ** (len(x) - i - 1))
  return result

def from_binary(x, base): return from_decimal(to_decimal(x, 2), base)

def binary_to_octet(x):
  x = "".join(["0" * (len(x) % 3), x])
  x = [list(x[i] for i in range(a * 3, 3 * (a + 1))) for a in range(len(x) // 3)]
  return "".join([from_binary(a, 8) for a in x])
