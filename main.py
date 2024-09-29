# o understand the __init__ constructor and the class method initFromBirthYear.
from datetime import date

class Student:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
# self refers to the instance of the class.
# name is a required parameter.
# age is an optional parameter with a default value of 0.
    def describe(self):
        print(f"My name is {self.name} and my age is {self.age}")
# The __init__ constructor initializes the instance variables name and age.
# The initFromBirthYear class method provides an alternative way to create a Student instance by calculating the age from the birth year.
# The describe method prints the student's name and age.
    @classmethod
    def initFromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

student1 = Student("Islam", 20)
student2 = Student.initFromBirthYear("Ahmed", 1993)

student1.describe()
student2.describe()
