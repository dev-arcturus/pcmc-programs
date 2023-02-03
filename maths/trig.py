from math import pi, sqrt

def rad(degree: float):
  return degree * pi / 180

def deg(rad: float):
  return rad * 180 / pi

def format_degree(degree: float):
  deg = int(degree)
  rmd = (degree - deg) * 60
  min = int(rmd)
  rmd = (rmd - min) * 60
  sec = int(rmd)
  
  if sec:
    return f"{deg}° {min}\' {sec}\""
  elif min:
    return f"{deg}° {min}'"
  else:
    return f"{deg}°"

def generate_table(base: float, perp: float):
  hyp = sqrt(base ** 2 + perp ** 2)

  print("sin:  ", format_degree(deg(perp / hyp)))
  print("cos:  ", format_degree(deg(base / hyp)))
  print("tan:  ", format_degree(deg(perp / base)))
  print("csc:  ", format_degree(deg(hyp / perp)))
  print("sec:  ", format_degree(deg(hyp / base)))
  print("cot:  ", format_degree(deg(base/ perp)))

generate_table(1, 1)