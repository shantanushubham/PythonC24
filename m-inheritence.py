class ParentOne:

    def test_function(self):
        print("This is parent one test function")

    def parent_one_function(self):
        print("This is parent one function")


class ParentTwo:

    def test_function(self):
        print("This is parent two test function")

    def parent_two_function(self):
        print("This is parent two function")


class Child(ParentOne, ParentTwo):

    def child_function(self):
        super().test_function()
        ParentTwo.test_function(self)
        print("This is child function")


c1 = Child()
c1.child_function()
c1.test_function()
c1.parent_one_function()
c1.parent_two_function()



class Mammal:

    def mammal_function(self):
        print("This is mammal function")


class AqauticAnimal:

    def aquatic_animal_function(self):
        print("This is aquatic animal function")



class Whale(Mammal, AqauticAnimal):

    def whale_function(self):
        print("This is whale function")


