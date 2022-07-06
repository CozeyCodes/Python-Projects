from datetime import date

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @classmethod
    def agecalc(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)

    def show(self):
        print(f"{self.name} is {self.age} years old.")


x = Student("Kesha",27)
x.show()

name = Student.agecalc("Pratik", 1969)
name.show()