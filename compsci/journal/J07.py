n = int(input("Enter a number: "))

for i in range(2, n):
  if n%i==0:
    prime = False
    break
else:
  prime=True

print(prime)