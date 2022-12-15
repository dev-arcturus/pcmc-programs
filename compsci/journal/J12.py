l = eval(input("Enter a list: "))

sub = input("substring to find: ")

for i in l:
  if i == sub:
    print("Element found")
    break
else:
  print("not found")