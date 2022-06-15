class Vector():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    self.x += other.x
    self.y += other.y
    return self

  def __sub__(self, other):
    self.x -= other.x
    self.y -= other.y
    return self
  
  def __mul__(self, other):
    self.x *= other.x
    self.y *= other.y
    return self
  
  def __truediv__(self, other):
    self.x /= other.x
    self.y /= other.y
    return self
  
  def __repr__(self):
    return f"({self.x}, {self.y})"


A = Vector(1, 2)
B = Vector(3, 4)
print(A * B)