import string, random

class GamateError(BaseException):
   def __init__(self, arg): self.args = arg

def add_matrices(x, y):
  result = []
  for i in x:
    for j in y: result.append(i + j)
  return result

DP1 = input("Enter the first dominant phenotype: ")
RP1 = input("Enter the first recessive phenotype: ")
DP2 = input("Enter the second dominant phenotype: ")
RP2 = input("Enter the second recessive phenotype: ")

if DP1[0] == DP2[0]:
  DP2_ = random.choice([x for x in string.ascii_letters.replace(DP2[0], "")]).upper()
  RP2_ = DP2_.lower()
  print(f"Warning: Second Dominant Phenotype has been set to {DP2_}, as it conflicted with the first\nThe Recessive phenotype has also been changed to {RP2_}")
else:
  DP2_, RP2_ = DP2[0], DP2[0].lower()


GT_OPTS = [DP1[0].upper(), DP1[0].lower(), DP2_, RP2_]

print("\n", "-" * 60)
print(f"\nUse the variables: {', '.join(GT_OPTS[:-1])} and {GT_OPTS[-1]}\n")

GT1, GT2 = None, None

while True:
  try:
    GT1 = input("Enter the first parent's genotype: ")

    for i in range(len(GT1)):
      if i < 2:
        if GT1[i] not in GT_OPTS[:2]: raise GamateError("CHARS")
      elif i < 4:
        if GT1[i] not in GT_OPTS[2:4]: raise GamateError("CHARS")
    

    GT2 = input("Enter the second parent's genotype: ")

    for i in range(len(GT2)):
      if i < 2:
        if GT2[i] not in GT_OPTS[:2]: raise GamateError("CHARS")
      elif i < 4:
        if GT2[i] not in GT_OPTS[2:4]: raise GamateError("CHARS")

    break

  except GamateError:
    print()
    print(
      "Genotypes should be 4 characters long, and only be made up of " 
      f"{', '.join(GT_OPTS[:-1])} and {GT_OPTS[-1]}"
      )
    print()

GT1, GT2 = [[*GT1[0:2]], [*GT1[2:4]]], [[*GT2[0:2]], [*GT2[2:4]]]

GT1, GT2 = add_matrices(*GT1[0:2]), add_matrices(*GT2[0:2])

GTD, GTD_MAP, PTD_MAP = [], {}, {}

for x in GT1:
  for y in GT2:
    a, b = ["".join(sorted([x[i], y[i]])) for i in range(2)]
    GTD.append("".join([a, b]))

for x in GTD:
  if x in GTD_MAP.keys(): GTD_MAP[x] = GTD_MAP[x] + 1
  else: GTD_MAP[x] = 1

for x in GTD_MAP.keys():
  if GT_OPTS[0] in x[:2]: a = DP1
  else: a = RP1
  if GT_OPTS[2] in x[2:4]: b = DP2
  else: b = RP2

  if x == f"{GT_OPTS[0] * 2}{GT_OPTS[2] * 2}" or x == f"{GT_OPTS[1] * 2}{GT_OPTS[3] * 2}": c = "Pure "
  else: c = ""
  
  PTD_MAP[x] = [f"{c}{a} {b} ({x})", GTD_MAP[x]]

print("", "=" * 60, "", sep="\n")

for x in list(PTD_MAP.keys()):
  prefix = PTD_MAP[x][0] + ":"
  print(f"{prefix:<50} {PTD_MAP[x][1] / 16 * 100}%")
