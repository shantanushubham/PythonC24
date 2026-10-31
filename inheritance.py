# You can use any name. Parent is not a reserved keyword.
from typing_extensions import override


class Parent:

    def __init__(self, name):
        self.name = name

    def test_function(self):
        # Code to do Step 1-5
        print("This is parent test function")


# class Child extends Parent
class Child(Parent):  # Inheritance is happening here.

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def my_function(self):
        print("This is my function")

    # This is a decorator that tells the compiler that the method is overriding the parent method. 
    # Has no impact on the code but it is a good practice to write it.
    @override
    def test_function(self):
        super().test_function()
        # Code to do Step 6 & 7
        print("This is child test function")

    def parent_test_function(self):
        # super = parent class
        super().test_function()


p1 = Parent("John")
p1.test_function()

c1 = Child("Taylor")
c1.test_function()
