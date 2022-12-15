n = int(input("Enter a number: "))
n2 = str(n)

if n2 == n2[::-1]:
  print("Its a palindrome")
else:
  print("It isnt a palindrome")


sum = 0

for x in n2:
  sum+= int(x) ** len(n2)

if sum == n:
  print("Its an armstrong number")
else:
  print("It isnt an armstrong number")

sum = 0

for i in range(1, n):
  if n%i == 0:
    sum += i

if n == sum:
  print("Its a perfect number.")
else:
  print("It isnt a perfect number.")