#  Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC,abstractmethod
class Userauthentication:
    @abstractmethod
    def login():
        pass
    @abstractmethod
    def logout():
        pass
class Google(Userauthentication):
    def login(self):
        print('login is done by google')
    def logout(self):
        print('logout is done by google')
    
class Facebook(Userauthentication):
    def login(self):
        print('login is done by facebook')
    def logout(self):
        print('logout is done by facebook')

# def my_function(obj):
#     obj.login()
#     obj.logout()

# obj1=Google()
# my_function(obj1)

# obj2=Facebook()
# my_function(obj2)
obj=Google()
obj.login()
obj.logout()
