"""
Zaimplementuj klasę Glass, która będzie przechowywała informacje o szkle (np. nazwa,
współczynniki zależności Sellmeiera). Dodatkowo, klasa Glass powinna udostępniać
metodę, która pozwala obliczać współczynnik załamania dla konkretnej długości fali.
"""

import math

class Glass():
    def __init__(self):
        self.__name = ""
        self.__sellmeier = []

    def set_name(self, name):
        self.__name = name

    def set_sellmeier(self, sellmeier):
        self.__sellmeier = sellmeier

    def get_name(self):
        return self.__name

    def get_sellmeier(self):
        return self.__sellmeier

    def refractive_index(self, wavelength):
        return math.sqrt(self.__sellmeier[0] + self.__sellmeier[1] * wavelength ** 2 / (wavelength ** 2 - self.__sellmeier[2]) + self.__sellmeier[3] * wavelength ** 2 / (wavelength ** 2 - self.__sellmeier[4]))

    def __str__(self):
        return f"Name: {self.__name} Sellmeier: {self.__sellmeier}"

def main():
    glass = Glass()
    glass.set_name("BK7")
    glass.set_sellmeier([1.03961212, 0.231792344, 1.01046945, 1.00092791, 6.00069867])
    print(glass)
    print(glass.refractive_index(0.5))

if __name__ == '__main__':
    main()