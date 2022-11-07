"""
Zaimplementuj klasę Pet, która będzie przechowywała informacje o zwierzęciu
domowym (imię, rodzaj, wiek). Klasa powinna udostępniać metody do odczytywania
i nadawania wartości pól klasy. Zademonstruj działanie klasy w programie.
"""

class Pet():
    def __init__(self):
        self.__name = ""
        self.__type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__type = type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"Name: {self.__name} Type: {self.__type} Age: {self.__age}"

def main():
    pet = Pet()
    pet.set_name("Burek")
    pet.set_type("Dog")
    pet.set_age(5)
    print(pet)

if __name__ == '__main__':
    main()