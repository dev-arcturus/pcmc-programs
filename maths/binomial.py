from PnC import combinations as cb

degree = int(input("Enter the degree: "))

terms = []

for i in range(degree + 1):
  coeff = cb(degree, i)
  j = degree - i

  coeff = "" if coeff == 1 else coeff
  a = " a" if j == 1 else "" if j == 0 else f" a^{j}"
  b = " b" if i == 1 else "" if i == 0 else f" b^{i}"

  terms.append(f"{coeff}{a}{b}")

print(" + ".join(terms))



