# Public = Accessible everywhere


class Car:

    def __init__(self, brand):
        self.brand = brand

    # Public
    def start_engine(self):
        return self.brand + " engine started"


my_car = Car("Toyota")
# print(my_car.start_engine())

# Protected = Intended for internal use only which means it is accessible within the class and its child classes.
# Note: Python does not prevent external code from accessing a protected variable; 
# the underscore is a convention to warn developers not to access it directly.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary


class Manager(Employee):

    def get_salary(self):
        return self._salary

manager = Manager("Jane", 20000)
# print(manager.get_salary())

emp = Employee("John", 10000)
# print(emp._salary)

# Private = Intended for internal use only which means it is accessible within the class only.

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance


class SBIAccount(BankAccount):

    def get_balance_sbi(self):
        return self.__balance + 1000


account = BankAccount("John", 90000)
print(account.get_balance())
# print(account.__balance)
print(account._BankAccount__balance) # This is a hack. Don't do this in production.

# sbi_account = SBIAccount("Shantanu", 900000)
# print(sbi_account.get_balance_sbi())