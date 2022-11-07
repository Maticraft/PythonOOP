"""
Zaimplementuj klasę Complex, która będzie reprezentowała liczby zespolone.
Implementację klasy umieść w osobnym pliku. Klasa powinna wykorzystywać pola
prywatne do przechowywania części rzeczywistej oraz urojonej liczby zespolonej,
a także udostępniać metody, do odczytywania i nadawania ich wartości. Ponadto, klasa
powinna implementować metody do obliczania modułu i argumentu liczby zespolonej.
Zademonstruj działanie klasy w programie.
"""

import math


class Complex():
    def __init__(self):
        self.__real = 0
        self.__imaginary = 0

    def set_real(self, real):
        self.__real = real

    def set_imaginary(self, imaginary):
        self.__imaginary = imaginary

    def get_real(self):
        return self.__real

    def get_imaginary(self):
        return self.__imaginary

    def module(self):
        return (self.__real ** 2 + self.__imaginary ** 2) ** 0.5
        
    def argument(self):
        return math.acos(self.__real / self.module())
