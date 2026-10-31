# OOP - Object Oriented Programming

# Class
# Object

# BluePrint or an Idea of how to make a coffee - Class
# TypeOfCoffee - Americano/Latte/Cappuccino/Mocha
# Size - Small/Medium/Large
# Temperature - Hot/Cold
# Sugar - Yes/No
# TypeOfMilk - Regular/Skim/Soy/Almond/None


# Actual Coffee made by the above blueprint or idea - Object

# AdityaCoffee
# - Cappuccino - Small - Hot - Yes - Regular

# AnkushCoffee
# - Americano - Small - Hot - No - None

"""

class Coffee:

    Things that needed to make a coffee:
    1. TypeOfCoffee
    2. Size
    3. Temperature
    4. Sugar
    5. TypeOfMilk

    We need to have a mechanism to make coffee once the above info is provided,
    i.e. making an object of the class Coffee

"""


class Coffee:

    # self = this

    # When self is used inside a constructor, self = the object that is going to be created.

    # Constructor = it has to be a function called __init__.
    def __init__(
        self, type_of_coffee: str, size, is_hot, has_sugar, type_of_milk="Regular"
    ):
        self.type_of_coffee = type_of_coffee
        self.size = size
        self.is_hot = is_hot
        self.has_sugar = has_sugar
        if type_of_coffee == "Americano":
            self.type_of_milk = None
        else:
            self.type_of_milk = type_of_milk

    # When we create a function inside a class, it is called a method. And the first argument of the method is always self.

    # When self is used outside a constructor, self = the object that is used to access the member of the class.
    def test_function(self):
        print("This is a test function")
        print(self.type_of_coffee)



coffee_for_aditya = Coffee("Cappuccino", "Small", True, True, "Soy")
coffee_for_ankush = Coffee("Americano", "Small", True, False)
coffee_for_shantanu = Coffee(
    type_of_milk="Oat",
    type_of_coffee="Mocha",
    has_sugar=False,
    size="Large",
    is_hot=True,
)

# print(coffee_for_aditya.type_of_coffee)
# print(coffee_for_ankush.type_of_milk)
# print(coffee_for_shantanu.type_of_milk)

coffee_for_shantanu.test_function()
coffee_for_aditya.test_function()
coffee_for_ankush.test_function()

# RAM
# []["Regular"][][][][][True][][][]["Cappuccino"][][][][][][][True][][][][][]["Small"][][][][][][][][][][][][[xx,x1,x2,x3,x4,x5]]
#       xx               x1              x3                     x4               x5                            coffee_for_aditya
