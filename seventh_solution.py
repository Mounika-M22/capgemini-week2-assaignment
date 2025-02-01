#  Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.

class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'the name of person is {self.name}')

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary
    def show_dep(self):
        print(f'{self.name} is having {self.salary} salary')
        
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
        print(f'{self.name} is from {self.department} department and a manager')
    def approve(self):
        print(f'the manager can approve leave')
obj=Manager('khushi',50000,'hr')
obj.show()
obj.show_dep()
obj.approve()
