import math

def frange(start, stop, step):
    l = []
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l

# sellmeier equation
# coeffs - list of coefficients (b, c)
def sellmeier(coeffs):
    def refractive_index(wavelength):
        sellmeier_coeff = lambda wavelength, b_i, c_i: b_i*wavelength**2 / (wavelength**2 - c_i**2)
        sellmeier_sum = lambda wavelength, coeffs: sum([sellmeier_coeff(wavelength, b_i, c_i) for b_i, c_i in coeffs]) + 1
        return math.sqrt(sellmeier_sum(wavelength, coeffs))
    return refractive_index

sio2_ref_index = sellmeier(((0.6961663, 0.0684043), (0.4079426, 0.1162414), (0.8974794, 9.896161))) 


# Generate float range of wavelengths
for wavelength in frange(0.2, 6.7, 0.01):
    print(sio2_ref_index(wavelength))