# Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.

from abc import ABC,abstractmethod
class Idatabase:
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass

class Sqldatabase(Idatabase):
    def insert(self):
        print('inserted in sqldatabase')
    def update(self):
        print('updated in sqldatabase')
    def delete(self):
        print('deleted in sqldatabase')
class Nosqldatabase(Idatabase):
    def insert(self):
        print('inserted in sqldatabase')
    def update(self):
        print('updated in sqldatabase')
    def delete(self):
        print('deleted in sqldatabase')
obj=Sqldatabase()
obj.insert()
obj.delete()
obj.update()

obj2=Nosqldatabase()
obj2.insert()
obj2.delete()
obj2.update()
