#  Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'device name is {self.name}')        




class Mobiledevice(Electronics):
    def __init__(self, name,model):
        super().__init__(name)
        self.model=model
    def show(self):
        Electronics.show(self)
        print(f'the model name is {self.model}')


class Smartphone(Mobiledevice):
    def __init__(self, name, model,storage):
        super().__init__(name, model)
        self.storage=storage
    def show(self):
        Mobiledevice.show(self)
        print(f'the storage of {self.name} is {self.storage}')
obj=Smartphone('oppo','reno 2z','35gb')
obj.show()
