# Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC,abstractmethod

class Ishape:
    @abstractmethod
    def calculate_area():
        pass
class Rectangle(Ishape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate_area(self):
        print(f'the area of rectangle is {self.a*self.b}')

class Circle(Ishape):
    def __init__(self,r):
        self.r=r
        
    def calculate_area(self):
        print(f'the area of circle is {(22/7)*(self.r**2)}')

def my_function(obj):
    obj.calculate_area()


obj1=Circle(5)
obj1.calculate_area()

obj2=Rectangle(3,4)
obj2.calculate_area()


        
    

