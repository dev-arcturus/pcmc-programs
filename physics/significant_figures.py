from re import search

def boolean(condition): return not not condition

def is_float(number):
  try: return boolean(float(number))
  except(ValueError): return False

def safe_float_input(message):
  while True:
    try: 
      number = input(message)
      if is_float(number): return(number)
    except(ValueError): continue

number = safe_float_input("Enter a rational number: ")

count = 0  # number of significant figures
is_decimal = "." in number

for i in range(len(number)):
  x = number[i]
  precedes_non_zeros = boolean(search("[^0\.]", number[i:]))
  procedes_non_zeros = boolean(search("[^0\.]", number[:i]))
  in_between_non_zeros = precedes_non_zeros and procedes_non_zeros

  if x not in "0.": count += 1  # RULE 1
  
  if x == "0":
    if in_between_non_zeros: count += 1  # RULE 2
    if is_decimal and not precedes_non_zeros: count += 1  # RULE 3

print(f"there are {count if is_decimal else 'infinite'} significant figures")
