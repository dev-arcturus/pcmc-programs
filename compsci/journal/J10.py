l = eval(input("Enter a list: "))
min = max = l[0]

for x in l:
  if x > max:
    max = x
  if x < min:
    min = x

print(max, min)