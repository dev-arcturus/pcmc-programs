# implementing sets without using in-built set type

def display(set): 
  """ correctly formatted list and display as a set """
  print("{", ", ".join([str(x) for x in set]), "}")

def create(list):
  set_ = []
  for x in list: 
    if x not in set_: set_.append(x)
  return set_

def union(set1, set2):
  return create(set1 + set2)

def intersection(set1, set2):
  set_ = []
  for x in set1:
    if x in set2: set_.append(x)
  return set_

def is_element(element, set):
  return element in set

def is_subset(subset, set):
  for x in subset:
    if not x in set: return False
  return True

def is_disjoint(set1, set2):
  for x in set1:
    if x in set2: return False
  return True

def is_equal(set1, set2):
  for x in set1:
    if not x in set2: return False
  return True

def get_compliment(set, universal):
  set_ = []
  for x in universal:
    if x not in set: set_.append(x)
  return set_

setA = create([1, 2, 3, 4, 5])
setB = create([3, 4, 5, 6, 7])

# display(create([1, 2, 8, 8, 8, 9, 10]))

display(intersection(setA, setB))