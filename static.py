class Demo:

    # It is supposed to behave like a static variable
    a = 5

    def __init__(self, b):
        self.b = b

    def test_function(self):
        print("This is a test function")

    @staticmethod # This is only an extra & doesn't change the output of the code but it is a good practice to write it
    def my_function(): # static method
        print("This is my function")


print(Demo.a)
d1 = Demo(10)
print(d1.a)
d1.a = 50 # This will create a new non-static a and assign 50 to it
print(d1.a)
d1.z = -100
print(Demo.a)

Demo.a = 100
print(d1.a)

d2 = Demo(20)
print(d2.z)
print(d2.my_function())