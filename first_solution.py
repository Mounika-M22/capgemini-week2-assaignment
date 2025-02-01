#  Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
        
    def show(self):
        print(f'the details are:\nname:{self.name}\nid is {self.id}\ndepartment is {self.department}\n')


n=int(input("enter num of employees:"))
def my_function(obj):
    obj.show()

employee_list=[]
for i in range(n):
    print(f'enter details of {i+1} employee')
    emp=Employee(name=input('enter name:'),id=int(input('enter id:')),department=input('enter department:'))
    employee_list.append(emp)
for i in employee_list:
    i.show()
    

    
