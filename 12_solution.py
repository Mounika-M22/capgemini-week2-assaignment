# Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
class Payment:
    def __init__(self,money):
        self.money=money
    def process_payment(self):
        return f'the payment of {self.money} is done'
class Creditcard(Payment):
    def __init__(self, money):
        super().__init__(money)
    def process_payment(self):
        print(super().process_payment()+'through creditcard')
        
class Paypal(Payment):
    def __init__(self, money):
        super().__init__(money)
    def process_payment(self):
        print(super().process_payment()+'through paypal')

class Bitcoin(Payment):
    def __init__(self, money):
        super().__init__(money)
    def process_payment(self):
        print(super().process_payment()+'through bitcoin')
obj=Bitcoin(2500)
obj.process_payment()


        
