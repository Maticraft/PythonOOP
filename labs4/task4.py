"""Zaimplementuj klasę Course, która będzie przechowywać informacje, o kursach
prowadzonych przez uczelnię (nazwa, kod, punkty ECTS, wymiar godzinowy itp.).
Zaprojektuj i zaimplementuj interfejs klasy. Napisz program, w którym utworzysz listę
kursów, które realizujesz w tym semestrze."""

class Course():
    def __init__(self):
        self.__name = ""
        self.__code = ""
        self.__ects = 0
        self.__hours = 0

    def set_name(self, name):
        self.__name = name

    def set_code(self, code):
        self.__code = code

    def set_ects(self, ects):
        self.__ects = ects

    def set_hours(self, hours):
        self.__hours = hours

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_ects(self):
        return self.__ects

    def get_hours(self):
        return self.__hours

    def __str__(self):
        return f"Name: {self.__name} Code: {self.__code} ECTS: {self.__ects} Hours: {self.__hours}"

def main():
    course_names = ["Python", "C++", "Java", "C#", "JavaScript"]
    course_codes = ["PYT", "CPP", "JAV", "C#", "JS"]
    course_ects = [5, 3, 2, 4, 3]
    course_hours = [30, 20, 15, 25, 20]
    for i in range(len(course_names)):
        course = Course()
        course.set_name(course_names[i])
        course.set_code(course_codes[i])
        course.set_ects(course_ects[i])
        course.set_hours(course_hours[i])
        print(course)


if __name__ == '__main__':
    main()