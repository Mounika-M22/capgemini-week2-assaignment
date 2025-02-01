# Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
from abc import ABC,abstractmethod
class Ivehicle:
    @abstractmethod
    def start_engine():
        pass
    @abstractmethod
    def stop_engine():
        pass

class Car(Ivehicle):
    def start_engine(self):
        print(f'the car has started')
    def stop_engine(self):
        print(f'the car has stoped')

class Bike(Ivehicle):
    def start_engine(self):
        print(f'the bike has started')
    def stop_engine(self):
        print(f'the bike has stoped')

class Truck(Ivehicle):
    def start_engine(self):
        print(f'the truck has started')
    def stop_engine(self):
        print(f'the truck has stoped')

def my_function(obj):
    obj.start_engine()
    obj.stop_engine()

obj1=Car()
my_function(obj1)

obj2=Truck()
my_function(obj2)

obj3=Bike()
my_function(obj3)


