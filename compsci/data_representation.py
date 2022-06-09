bits = "0123456789ABCDEF"

def safe_get_index(array, search):
  try: return array.index(search)
  except(ValueError): return None

def calculate_offset(x):
  return (type(x) == "float" and -1 * (len(str(x)) - 1 - safe_get_index([_ for _ in str(x)], "."))) or 0

def from_decimal(x, base):
  if x == 0: return "0"
  if x < 0: x, base = -x, base * -1
  result, x = "", int(str(x).replace(".", ""))
  while x > 0: result, x = bits[x % base] + result, x // base
  return result

def to_decimal(x, base):
  result, offset, x = 0, calculate_offset(x), str(x).replace(".", "")
  for i, c in enumerate(x): result += bits.index(c) * (base ** (len(x) - i + offset - 1))
  return result

print(to_decimal("1010.01", 2))

def convert(x, current_base, target_base): return from_decimal(to_decimal(x, current_base), target_base)

def binary_to_octet(x):
  x = "".join(["0" * (len(x) % 3), x])
  x = [list(x[i] for i in range(a * 3, 3 * (a + 1))) for a in range(len(x) // 3)]
  return "".join([convert(a, 2, 8) for a in x])

def binary_to_hex(x):
  x = "".join(["0" * (len(x) % 4), x])
  x = [list(x[i] for i in range(a * 4, 4 * (a + 1))) for a in range(len(x) // 4)]
  return "".join([convert(a, 2, 16) for a in x])