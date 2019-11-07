"""
Exercise 5 (group work)
Write a definition for a class of anything you want. You have to use the following methods:

_init_ method that initializes some attributes. One of the attributes has to be an empty list.

_str_ method that returns a string that reasonably represent the thing.

A special method that overloads the one type of operators.

Some other methods that reasonably represent the thing's actions, inclduing one method that takes an object of any type and adds it to the attribute of type list.

Test your code by creating two objects and using all the methods.
"""

class Favorite_Foods:
    """Represents someone's favorite foods"""
    def __init__(self, name='', foods=[]):
        """initialize"""
        self.name = name
        self.foods = foods

    def __str__(self):
        """
        return a object in a human-readable format
        text represenation of this object
        """
        return f"{self.name}'s favorite foods are {', '.join(self.foods)}"

    def __eq__(self, other):
        """
        return True if self and other share the same favorite foods
        """
        return self.foods == other.foods

    def __add__(self, other):
        """returns self and other favorite foods"""
        total_foods = self.foods + other.foods
        return f"{self.name} and {other.name}'s favorite foods are {', '.join(total_foods)}"

Arteen = Favorite_Foods('Arteen', ['ice cream', 'pizza'])
print(Arteen)

Spencer = Favorite_Foods('Spencer', ['ice cream', 'pizza'])
print(Spencer)

Brian = Favorite_Foods('Brian', ['rice', 'pasta'])
print(Brian)

print(Arteen == Spencer) #True
print(Brian == Spencer) #False

print(Arteen + Brian)