import math
import numpy as np

# Refractive index for SiO2 (https://refractiveindex.info/?shelf=main&book=SiO2&page=Malitson)
# wavelength in micrometers
def refractive_index(wavelength):
    n2_1 = 0.6961663*wavelength**2 / (wavelength**2 - 0.0684043**2) + 0.4079426*wavelength**2 / (wavelength**2 - 0.1162414**2) + 0.8974794*wavelength**2 / (wavelength**2 - 9.896161**2) 
    n = math.sqrt(n2_1 + 1)
    return n


# Generate table of refractive index for wavelengths from given range
def generate_refractive_index_table(wavelength_range, filename):
    with open(filename, 'w') as f:
        for wavelength in wavelength_range:
            f.write(f'{wavelength} {refractive_index(wavelength)}\n')


# Using numpy to generate float range of wavelengths
wavelenght_range = np.arange(0.2, 6.7, 0.01)
generate_refractive_index_table(wavelenght_range, './labs1/refractive_index.txt')