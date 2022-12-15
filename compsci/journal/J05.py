import math

x = int(input("Enter a no.: "))
n = int(input("Enter no. of terms: "))
sum = 0

for i in range(n+1):
  sum+= x ** i

print(sum)
sum = 0

for i in range(n+1):
  if i%2 == 0: sign = 1
  else: sign = -1
  sum += sign * x ** i

print(sum)
sum = 0

for i in range(1, n+1):
  if i%2 == 0: sign = -1
  else: sign = 1
  sum += sign * x ** i / i

print(sum)
sum = 0

for i in range(1, n+1):
  if i%2 == 0: sign = 1
  else: sign = -1
  sum += sign * x ** i / math.factorial(i)

print(sum)