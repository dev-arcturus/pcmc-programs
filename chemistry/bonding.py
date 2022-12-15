
order_1 = ("σ1s", "σ*1s", "σ2s", "σ*2s", ("π2px", "π2py"),
     "σ2pz", ("π*2px", "π*2py"), "σ*2pz")

order_2 = ("σ1s", "σ*1s", "σ2s", "σ*2s",
     "σ2pz",("π2px", "π2py"), ("π*2px", "π*2py"), "σ*2pz")
     


def get_molecular_config(n: int):
  config, a = [], n
  for orbital in (order_1 if n <= 14 else order_2):
    if a == 0: break
    if type(orbital) is tuple:  # maximum multiplicity rule
      orbs = len(orbital)
      hunds_order, b, i = [0 for _ in range(orbs)], orbs * 2, 0
      while b:
        print(b, hunds_order, i)
        hunds_order[i] += 1
        b -= 1; i += 1
        if i == len(orbital): i = 0
      for i, orb in enumerate(orbital):
        config.append(f"{orb}{hunds_order[i]}")
    else:
      if a == 1:
        config.append(f"{orbital}")
        break
      config.append(f"{orbital}2")
    a -= 2
  return config


# get_molecular_config(14)

print(get_molecular_config(16))
