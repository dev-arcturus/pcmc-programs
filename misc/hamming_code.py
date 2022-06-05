#! [P.S.] this program still has flaws with regards to multiple errors for the same byte
##        the program labels the parity bits as the corrupt when there are multiple errors
##        but it is working for the most part

from random import randint

def parity(x):
  """
    returns the parity bit for a given number
  """
  if x == 0: return 0
  else: return 0 if x % 2 == 0 else 1


def get_overall_parity(x):
  """
    gets the parity bits for a given array
  """

  count = 0
  for i in x:
    if i == 1: count += 1
  return parity(count)


def get_11bit_chunks(array):
  """
    takes in an array and returns an array of arrays of length 11
  """

  # pads the information with 0s to make its length a multiple of 11
  if len(array) % 11 != 0:
    for _ in range(11 - len(array) % 11): array.insert(0, 0)

  # calculates the number of 11-bit bytes the information would take up
  BYTE_COUNT = len(array) // 11

  # breaks message into an array of 11-bit chunks
  return [list(array[i] for i in range(x * 11, 11 * (x + 1))) for x in range(BYTE_COUNT)]


def construct_16bit_matrix(array):
  """
    takes in an array of length 11 and returns a 16-bit 4x4 matrix with 'None' in place of parity bits
  """

  # here, n is a placeholder for parity bits
  n = None

  x = array

  a = [n, n, n, x[0]]
  b = [n ,x[1],x[2],x[3]]
  c = [n, x[4], x[5], x[6]]
  d = [x[7], x[8], x[9], x[10]]

  return [a, b, c, d]


def get_parities_for_matrix(matrix):
  """
    takes in a 16-bit 4x4 matrix and returns the parity results for each group
  """
  [a, b, c, d] = matrix

  # 2nd and 4th columns
  group1 = [a[3], b[1], b[3], c[1], c[3], d[1], d[3]]
  
  # 3rd and 4th columns
  group2 = [b[2], c[2], d[2], a[3], b[3], c[3], d[3]]
  
  # 2nd and 4th rows
  group3 = [b[1], b[2], b[3], d[0], d[1], d[2], d[3]]

  # 3rd and 4th rows
  group4 = [c[1], c[2], c[3], d[0], d[1], d[2], d[3]]

  groups = [group1, group2, group3, group4]

  return [get_overall_parity(x) for x in groups]


def set_parity_bits(matrix, parities):
  """
    takes in a 16-bit 4x4 matrix and the parity tests and returns a 16-bit 4x4 matrix with parity bits
  """
  [a, b, c, d] = matrix

  a[1] = parities[0]
  a[2] = parities[1]
  b[0] = parities[2]
  c[0] = parities[3]

  # this bit corresponds the overall parity for the matrix
  a[0] = get_overall_parity(a[1:] + b + c + d)

  return [a, b, c, d]


def check_parity_bits(matrix, parities):
  """
    takes in a 16-bit 4x4 matrix and the parity bits and returns:
      - True if the parity bits are correct
      - False if there is more than one corrupt bit
      - Coordinates of the corrupt bits if any
  """
  [p, q, r, s] = matrix

  a = p[1] == parities[0]
  b = p[2] == parities[1]
  c = q[0] == parities[2]
  d = r[0] == parities[3]

  # narrowing down the column of the error
  if not a and not b:
    col = 3
  elif not a and b:
    col = 1
  elif a and not b:
    col = 2
  else:
    col = 0
  
  # narrowing down the row of the error
  if not c and not d:
    row = 3
  elif not c and d:
    row = 1
  elif c and not d:
    row = 2
  else:
    row = 0

  if not row and not col:
    if p[0] == get_overall_parity(p[1:] + q + r + s):
      return True    # there is no error
    else:
      return False   # there are more than one error 

  # there is an error, and we are returning its coordinates
  else:
    return [row, col]


def create_matrix_with_parity(list):
  """    
    takes in an array of length 11 and returns a 16-bit 4x4 matrix with parity bits
  """
  matrix = construct_16bit_matrix(list)
  parities = get_parities_for_matrix(matrix)
  set_parity_bits(matrix, parities)

  return matrix

def display_matrix(matrix):
  for x in matrix:
    for y in x:
      print(y, end=" ")
    print()

# NOT PART OF THE MODULE 

if __name__ == "__main__":
  print("Information should be in binary and no longer than 176 bits. Leave blank for a random message\n")

  while True:
    try:
      data = input("Enter the binary information: ")

      if not data:
        data = [str(randint(0, 1)) for _ in range(33)]

      if len(data) > 176: 
        raise Exception("Message too long. Keep it to a maximum of 176 bits")

      for x in data:
        if x not in ["0", "1"]:
          raise Exception("Your message must consist of only 0s and 1s")
      break

    except Exception as e:
      print(e, "\n")


  # turning the array of strings into an array of its corresponding int values
  SENT = [int(x) for x in data]

  bit11_array = get_11bit_chunks(SENT)

  bit_matrix = [create_matrix_with_parity(x) for x in bit11_array]

  print(f"\n{'-'*40}\n")

  RECIEVED = bit_matrix

  # creating random error at a certain location
  RECIEVED[1][2][3] = 0 if RECIEVED[1][2][3] == 1 else 1
  RECIEVED[2][3][3] = 0 if RECIEVED[2][3][3] == 1 else 1

  errors = []

  for x in range(len(RECIEVED)):
    a = check_parity_bits(RECIEVED[x], get_parities_for_matrix(RECIEVED[x]))

    if a == True: continue
    
    if a == False:
      errors.append([x + 1, -1])
      continue

    if errors != -1:
      errors.append([x + 1, a[0] + 1, a[1] + 1])
  
  if not errors:
    print("Message is error free, yay!")

  else:
    print(f"{len(errors)} error{'s' if len(errors) != 1 else ''} found\n")
    for x in errors:
      if x[1] == -1:
        print(f"There is more than one corrupt bit in Byte #{x}")
      print(f"Byte #{x[0]}: bit at row {x[1]} and column {x[2]} is corrupt")