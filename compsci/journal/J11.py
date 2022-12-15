# [5, 7, 1, 43, 12, 10]

l = eval(input("Enter a list of numbers: "))
l_ = []
i = 0

while len(l) - len(l_) > 1:
  l_.extend((l[i+1], l[i]))
  i += 2

if len(l) - len(l_) == 1:
  l_.append(l[-1])

print(l_)