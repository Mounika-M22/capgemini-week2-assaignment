# Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
from abc import ABC,abstractmethod
class Shape:
    
    @abstractmethod
    def area():
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        print(f'the area of square is {self.side*self.side}\n')

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        print(f'the area of square is {(1/2)*self.base*self.height}\n')
def my_function(obj):
    obj.area()
obj1=Square(5)
obj1.area()

obj2=Triangle(4,3)
obj2.area()


    