from collections import namedtuple
import re

# from misc.utils import get_hcf


def safe_int_convert(string: str):
    if not string.isdigit(): return None
    else: return int(string)


Element = namedtuple(
    'Element', 'chemical_name atomic_number atomic_mass group')

ELEMENTS = {
    'H': Element('Hydrogen', 1, 1, 'Non Metals'),
    'He': Element('Helium', 2, 4, 'Noble Gases'),
    'Li': Element('Lithium', 3, 7, 'Alkali Metals'),
    'Be': Element('Berylium', 4, 9, 'Alkaline Earth Metals'),
    'B': Element('Boron', 5, 11, 'Non Metals'),
    'C': Element('Carbon', 6, 12, 'Non Metals'),
    'N': Element('Nitrogen', 7, 14, 'Non Metals'),
    'O': Element('Oxygen', 8, 16, 'Non Metals'),
    'F': Element('Florine', 9, 19, 'Halogens'),
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
    'Cr': Element("Chromium", 24, 52, "")
}


def get_elements_from_compound(compound): return re.findall(
    r'[A-Z][a-z]*[1-9]*', compound)


def isolate_element(element): return re.search(r'[A-Z][a-z]*', element).group()


def lookup(key): return ELEMENTS[isolate_element(key)]


def get_coefficient(element):
    try: return safe_int_convert(re.findall(r'[2-9]+', element)[0])
    except(IndexError): return 1

def get_molar_mass(compound):
    elements, molar_mass = get_elements_from_compound(compound), 0
    try: moles = int(re.match(r'[0-9]+', compound).group())
    except: moles = 1
    for element in elements:
        molar_mass += lookup(element).atomic_mass * get_coefficient(element)
    return molar_mass * moles

def find_limiting_reagent(equation, given_masses_of_reactants):
    [[r1, r2], product], GMR = equation, given_masses_of_reactants
    MM = [get_molar_mass(x) for x in [r1, r2, product]]
    r2needed = GMR[0] * MM[1] / MM[0]
    return lookup(r2 if r2needed > GMR[1] else r1).chemical_name

def get_molarity(compound, volume): return get_molar_mass(compound) / volume

def get_molality(compound, molarity, density_in_kgm3):
    mass_of_solution = density_in_kgm3 / 1000
    mass_of_solute = get_molar_mass(compound) / 1000 * molarity
    mass_of_solvent = mass_of_solution - mass_of_solute
    return round(molarity / mass_of_solvent)


# def balance_equation(reactants, products):
#   R, P, tR, tP = reactants, products, {}, {}

#   for [wing, tally] in [[R, tR], [P, tP]]:
#     for compound in wing:
#       for [element, i] in [[isolate_element(y), get_coefficient(y)] for y in get_elements_from_compound(compound)]:
#         if element in tally.keys(): tally[element] += i
#         else: tally[element] = i

#   for x in tR:
#     a, b = tP[x], tR[x]
#     if a != b:
#       pass

#   print(tR, tP, sep='\n')
