bits = "0123456789ABCDEF"

def calculate_offset(x):
  return ("." in str(x) and -1 * (len(str(x)) - 1 - [_ for _ in str(x)].find("."))) or 0

def break_up_float(x): return int(str(x).split(".")[0]), float(f"0.{str(x).split('.')[1]}")

def from_decimal(n, base):
  if n == 0: return "0"
  if n < 0: n, base = -n, base * -1
  [a, b], [x, y], is_float = ["", ""], break_up_float(n) , "." in str(n)
  while x > 0: a, x = bits[x % base] + a, x // base
  while y != 1 and y != 0: b, y = b + str(bits[int(y * base)]), y * base - (1 if y * base > 1 else 0)
  return f"{a}.{b}" if is_float else a

def to_decimal(x, base):
  result, offset, x = 0, calculate_offset(x), str(x).replace(".", "")
  for i, c in enumerate(x): result += bits.index(c) * (base ** (len(x) - i + offset - 1))
  return result

def convert(x, current_base, target_base): return from_decimal(to_decimal(x, current_base), target_base)

def binary_to_octet(x):
  x = "".join(["0" * (len(x) % 3), x])
  x = [list(x[i] for i in range(a * 3, 3 * (a + 1))) for a in range(len(x) // 3)]
  return "".join([convert(a, 2, 8) for a in x])

def binary_to_hex(x):
  x = "".join(["0" * (len(x) % 4), x])
  x = [list(x[i] for i in range(a * 4, 4 * (a + 1))) for a in range(len(x) // 4)]
  return "".join([convert(a, 2, 16) for a in x])

