"""
Zaimplementuj klasę Complex, która będzie reprezentowała liczby zespolone.
Implementację klasy umieść w osobnym pliku. Klasa powinna wykorzystywać pola
prywatne do przechowywania części rzeczywistej oraz urojonej liczby zespolonej,
a także udostępniać metody, do odczytywania i nadawania ich wartości. Ponadto, klasa
powinna implementować metody do obliczania modułu i argumentu liczby zespolonej.
Zademonstruj działanie klasy w programie.
"""
"""
__add__(self, other),
• __radd__(self, other),
• __iadd__(self, other),
• __sub__(self, other),
• __rsub__(self, other),
• __isub__(self, other),
• __mul__(self, other),
• __rmul__(self, other),
• __imul__(self, other),
• __truediv__(self, other),
• __rtruediv__(self, other),
• __itruediv__(self, other),
• __neg__(self),
• __abs__(self).
"""

import math


class Complex():
    def __init__(self, x=0, y=0):
        self.__real = x
        self.__imaginary = y

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

    def __str__(self) -> str:
        return str((self.__real, self.__imaginary))

    def __add__(self, other):
        if type(other) == Complex:
            x = other.get_real() + self.__real
            y = other.get_imaginary() + self.__imaginary
            return Complex(x, y)
        else:
            raise NotImplementedError

    def __radd__(self, other):
        if type(other) == Complex:
            return self.__add__(other)
        else:
            raise NotImplementedError

    def __iadd__(self, other):
        if type(other) == Complex:
            self.__real += other.get_real()
            self.__imaginary += other.get_imaginary()
            return self
        else:
            raise NotImplementedError
        
    def __neg__(self):
        return Complex(-self.__real, -self.__imaginary)

    def __sub__(self, other):
        if type(other) == Complex:
            return self.__add__(-other)
        else:
            raise NotImplementedError

    def __rsub__(self, other):
        if type(other) == Complex:
            return other.__sub__(self)
        else:
            raise NotImplementedError

    def __isub__(self, other):
        if type(other) == Complex:
            self.__iadd__(other.__neg__())
            return self
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if type(other) == Complex:
            x = other.get_real() * self.__real - other.get_imaginary() * self.__imaginary
            y = other.get_real() * self.__imaginary + other.get_imaginary() * self.__real
            return Complex(x, y)
        else:
            raise NotImplementedError

    def __rmul__(self, other):
        if type(other) == Complex:
            return self.__mul__(other)
        else:
            raise NotImplementedError

    def __imul__(self, other):
        if type(other) == Complex:
            self = self.__mul__(other)
            return self
        else:
            raise NotImplementedError

    def __truediv__(self, other):
        if type(other) == Complex:
            x = (other.get_real() * self.__real - other.get_imaginary() * self.__imaginary) / (other.module() ** 2)
            y = (other.get_real() * self.__imaginary + other.get_imaginary() * self.__real) / (other.module() ** 2)
            return Complex(x, y)
        else:
            raise NotImplementedError

    def __rtruediv__(self, other):
        if type(other) == Complex:
            return other.__truediv__(self)
        else:
            raise NotImplementedError

    def __itruediv__(self, other):
        if type(other) == Complex:
            self = self.__truediv__(other)
            return self
        else:
            raise NotImplementedError

    def __abs__(self):
        return self.module()
