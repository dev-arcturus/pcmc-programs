from collections import namedtuple
import re

def safe_int_convert(str):
  try: return int(str)
  except(ValueError): return None  


Element = namedtuple('Element', 'symbol atomic_number atomic_mass group')

ELEMENTS = {
    'H': Element('Hydrogen', 1, 1, 'Non Metals'),
    'He': Element('Helium', 2, 4, 'Noble Gases'),
    'Li': Element('Lithium', 3, 7, 'Alkali Metals'),
    'Be': Element('Berylium', 4, 9, 'Alkaline Earth Metals'),
    'B': Element('Boron', 5, 11, 'Non Metals'),
    'C': Element('Carbon', 6, 12, 'Non Metals'),
    'N': Element('Nitrogen', 7, 14, 'Non Metals'),
    'O': Element('Oxygen', 8, 16, 'Non Metals'),
    'F': Element('F', 9, 19, 'Halogens'),
    'Ne': Element('Neon', 10, 20, 'Noble Gasses'),
    'Na': Element('Sodium', 11, 23, 'Alkali Metals'),
    'Mg': Element('Magnesium', 12, 24, 'Alkaline Earth Metal'),
    'Al': Element('Aluminium', 13, 27, 'Other Metals'),
    'Si': Element('Silicon', 14, 28, 'Non Metals'),
    'P': Element('Phosphorus', 15, 31, 'Non Metals'),
    'S': Element('Sulphur', 16, 32, 'Non Metals'),
    'Cl': Element('Chlorine', 17, 35.5, 'Halogens'),
    'Ar': Element('Argon', 18, 40, 'Noble Gasses'),
    'K': Element('Potassium', 19, 39, 'Alkali Metals'),
    'Ca': Element('Calcium', 20, 40, 'Alkaline Earth Metals'),
    'Mn': Element('Manganese', 25, 55, 'Transition Metals'),
    'Fe': Element('Iron', 26, 56, 'Transition Metals'),
    'Co': Element('Cobalt', 27, 59, 'Transition Metals'),
    'Ni': Element('Nickel', 28, 59, 'Transition Metals'),
    'Cu': Element('Copper', 29, 63.5, 'Transition Metals'),
    'Zn': Element('Zinc', 30, 65, 'Transition Metals'),
    'Ga': Element('Gallium', 31, 70, 'Other Metals'),
}

def get_elements_from_compound(compound):
  return re.findall(r'[A-Z][a-z]*[1-9]*', compound) 

def get_molar_mass(compound):
  elements = get_elements_from_compound(compound)
  molar_mass = 0
  for element in elements:
    coefficient = 1
    try: coefficient = safe_int_convert(re.findall(r'[2-9]+', element)[0])
    except(IndexError): pass
    lookup = re.findall(r'[A-Z][a-z]*', element)[0]
    molar_mass += ELEMENTS[lookup].atomic_mass * coefficient
  return molar_mass

def get_molarity(compound, volume): return get_molar_mass(compound) / volume

def get_molality(compound, molarity, density):
  mass_of_solution = density / 1000
  mass_of_solute = get_molar_mass(compound) / 1000 * molarity
  mass_of_solvent = mass_of_solution - mass_of_solute
  return round(molarity / mass_of_solvent)

print(get_molality("NaCl", 3, 1250))