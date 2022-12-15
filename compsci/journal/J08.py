n = int(input("Enter number of terms: "))

series = [0, 1]

for i in range(2, n+1):
  a, b = series[-2:]
  series.append(a+b)

print(series)
