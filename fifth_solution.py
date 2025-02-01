# Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if self.stock>=quantity:
            print(f'the requested quantity {quantity} is available')
        else:
            print(f'the quantity is not available')
obj=Product('rice',500,6000)
obj.check_availability(500)
        