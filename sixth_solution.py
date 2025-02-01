#  Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show_vehicledetails(self):
        print(f'the name of vehicle is {self.name},price of vehicle is {self.price}')
class Car(Vehicle):
    def __init__(self, name, price,seats):
        super().__init__(name, price)
        self.seats=seats
    def show_seats(self):
        
        print(f'no of seats in {self.name} are {self.seats}')

class Bike(Vehicle):
    def __init__(self, name, price,model):
        super().__init__(name, price)
        self.model=model
    def show_model(self):
        
        print(f'the model of  {self.name} is {self.model}')
class Electriccar(Car):
    def __init__(self, name, price, seats,charge):
        super().__init__(name, price, seats)
        self.charge=charge
    def show_charge(self):
        print(f'the charge of {self.name} is {self.charge}')

obj=Electriccar('toyota',5009080,6,600)
obj.show_vehicledetails()
obj.show_seats()
obj.show_charge()

obj2=Bike('royal',5000,'adventure')
obj2.show_vehicledetails()
obj2.show_model()