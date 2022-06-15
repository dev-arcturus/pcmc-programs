BOHRS = 52.9 * 10 ** (-12)
SPEED_OF_LIGHT = 3 * 10 ** 8
PLANKS = 6.626 * 10 ** (-34)
RYDBERGS = 2.18 * 10 ** (-18)

def get_wavelength(frequency):
    return SPEED_OF_LIGHT / frequency

def get_frequency(wavelength):
    return SPEED_OF_LIGHT / wavelength

def get_radius(shells):
    return shells * (BOHRS ** 2)

def get_energy(shells):
    return -1 * RYDBERGS / (shells ** 2)

def get_frequency_of_bohrs_orbit(change_in_energy):
    return change_in_energy / PLANKS

def get_angular_momentum(mass, velocity, radius):
    return mass * velocity * radius