# Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def details(self):
        return self.name,self.roll
obj=Student('mouni',62)
print(obj.details())