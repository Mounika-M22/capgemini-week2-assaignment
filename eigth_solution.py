# Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.	
class Animal:
    def speak(self):
        print('this is parent class')
class Dog(Animal):
    def speak(self):
        super().speak()
        print('the dog is shouting')
class Cat(Animal):
    def speak(self):
        super().speak()
        print('the cat is shouting')
obj1=Cat()
obj1.speak()

obj2=Dog()
obj2.speak()