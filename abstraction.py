from abc import ABC, abstractmethod

# Abstract class
# 1. It is a class. And thus, it behaves like normal class.
# 2. You cannot create an object of an abstract class.
# 3. It can have abstract methods as well as non-abstract methods.

# Abstract method
# 1. It is a method that is declared in an abstract class but has no function body.
# 2. It can only exist inside an abstract class.
# 3. It must be overridden in the child class.


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def test_function(self):
        print("Test function")


class PetrolEngine(Engine):

    def start(self):
        print("Petrol engine started")

    def stop(self):
        print("Petrol engine stopped")


class DieselEngine(Engine):

    def start(self):
        print("Diesel engine started")

    def stop(self):
        print("Diesel engine stopped")


class ElectricEngine(Engine):

    def start(self):
        print("Electric engine started")

    def stop(self):
        print("Electric engine stopped")


engine = ElectricEngine()
engine.test_function()

engine.start()
engine.stop()
