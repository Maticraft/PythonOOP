import math

def frange(start, stop, step):
    l = []
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l


# Helper lambda for Sellmeier expression
sellmeier_expr = lambda wavelength, b, c: b*wavelength**2 / (wavelength**2 - c**2) 


# Refractive index for SiO2 (https://refractiveindex.info/?shelf=main&book=SiO2&page=Malitson)
# wavelength in micrometers
refractive_index_lambda = lambda wavelength: math.sqrt(sellmeier_expr(wavelength, 0.6961663, 0.0684043)\
    + sellmeier_expr(wavelength, 0.4079426, 0.1162414) + sellmeier_expr(wavelength, 0.8974794, 9.896161) + 1)


# Generate float range of wavelengths
wavelength_range = frange(0.2, 6.7, 0.01)
gen = (refractive_index_lambda(wavelength) for wavelength in wavelength_range)
for ref_ind in gen:
    print(ref_ind)