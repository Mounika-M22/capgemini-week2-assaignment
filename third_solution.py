#You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
class Book:
    def __init__(self,name,author,isbn):
        self.name=name
        self.author=author
        self.isbn=isbn
    def show(self):
        print(f'the details of book are:\nname of the book is {self.name}\nauthor of {self.name} is {self.author}\nisbn of {self.name} is {self.isbn}')
obj=Book('it ends with us','collen hover',2345)
obj.show()