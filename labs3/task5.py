import math

def frange(start, stop, step):
    l = []
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l


# Helper lambda for Sellmeier sum coefficient
sellmeier_coeff = lambda wavelength, b_i, c_i: b_i*wavelength**2 / (wavelength**2 - c_i**2) 


# Helper lambda for Sellmeier expression
sellmeier = lambda wavelength, b, c: sum([sellmeier_coeff(wavelength, b_i, c_i) for b_i, c_i in zip(b, c)]) + 1

# Refractive index for SiO2 (https://refractiveindex.info/?shelf=main&book=SiO2&page=Malitson)
# wavelength in micrometers
refractive_index_lambda = lambda wavelength: math.sqrt(sellmeier(wavelength, [0.6961663, 0.4079426, 0.8974794], [0.0684043, 0.1162414, 9.896161]))


# Generate float range of wavelengths
for wavelength in frange(0.2, 6.7, 0.01):
    print(refractive_index_lambda(wavelength))