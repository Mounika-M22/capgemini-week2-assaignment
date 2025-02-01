# Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        return 'moves on road'
class Airplane:
    def move(self):
        return 'moves in air'
class Flyingcar(Car,Airplane):
    def move(self):
        
        print('Flyingcar'+" " +Car.move(self)+" " +'and'+" " +Airplane.move(self))
        
        print()
        
obj=Flyingcar()
obj.move()