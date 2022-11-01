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


order = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2), ("3d", 10), ("4p", 6), ("5s", 2),
         ("4d", 10), ("5p", 6), ("6s", 2), ("4f", 14), ("5d", 10), ("6p", 6), ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)]


def get_electron_config(Z: int):
    config, a = [], Z
    for orbital in order:
        if a <= orbital[1]:
            config.append(f"{orbital[0]}{a}")
            break
        config.append(f"{orbital[0]}{orbital[1]}")
        a -= orbital[1]
    return config


print(", ".join(get_electron_config(52)))
