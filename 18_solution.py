# Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
from abc import ABC,abstractmethod
class Ical:
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def sub():
        pass
    @abstractmethod
    def multiply():
        pass
    @abstractmethod
    def divide():
        pass
class Calculator(Ical):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        
        print(f'the sum is {self.a+self.b}')
    def sub(self):
        print(f'the subtraction is {self.a-self.b}')
    def multiply(self):
        print(f'the multiplication is {self.a*self.b}')
    def divide(self):
        print(f'the division is {self.a/self.b}')
    
obj=Calculator(4,3)
obj.add()
obj.sub()
obj.multiply()
obj.divide()