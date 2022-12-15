s = input("Enter a word or phrase: ")

if s == s[::-1]:
  print("Its a palindrome")

s_ = ""

for c in s:
  if c.islower():
    s_ += c.upper()
  else:
    s_ += c.lower()

print(s_)