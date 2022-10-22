import math

def frange(start, stop, step):
    l = []
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l


# Refractive index for SiO2 (https://refractiveindex.info/?shelf=main&book=SiO2&page=Malitson)
# wavelength in micrometers
def refractive_index(wavelength):
    n2_1 = 0.6961663*wavelength**2 / (wavelength**2 - 0.0684043**2) + 0.4079426*wavelength**2\
         / (wavelength**2 - 0.1162414**2) + 0.8974794*wavelength**2 / (wavelength**2 - 9.896161**2) 
    n = math.sqrt(n2_1 + 1)
    return n


# Generate float range of wavelengths
wavelength_range = frange(0.2, 6.7, 0.01)
refractive_index_range = [refractive_index(wavelength) for wavelength in wavelength_range]

for ref_ind in refractive_index_range:
    print(ref_ind)