bits = "0123456789ABCDEF"

def from_decimal(x, base):
  if x == 0: return "0"
  if x < 0: x, base = -x, base * -1
  result = ""
  while x > 0: 
    result += bits[x % base]
    x //= base
  return result

def convert(x, base):
  result = 0
  for i, c in enumerate(x): result += bits.index(c) * (base ** (len(x) - i - 1))
  return result

def binary_to_octet(x):
  x = "".join(["0" * (len(x) % 3), x])
  x = [list(x[i] for i in range(a * 3, 3 * (a + 1))) for a in range(len(x) // 3)]
  return "".join([convert(a, 8) for a in x])

def binary_to_hex(x):
  x = "".join(["0" * (len(x) % 4), x])
  x = [list(x[i] for i in range(a * 4, 4 * (a + 1))) for a in range(len(x) // 4)]
  return "".join([convert(a, 16) for a in x])

print(binary_to_hex("1010100101001001"))  