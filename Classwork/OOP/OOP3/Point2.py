class Point:
    """
    represents points in 2d space.

    attributes: x,y
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __sub__(self, other):
        result = Point()
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result

    def __eq__(self, other):
        """
        return True if x of both are same
        """
        return self.x == other.x

    def __contains__(self, number):
        return number == self.x or number == self.y


victoria = Point(3, 4)
print(victoria)

myat = Point(5 , 5)

print(victoria + myat)
print(myat - victoria)

carmen = Point(3,4)
print(carmen == victoria) #true
print(carmen == myat) #false

print(3 in victoria)
print(4 in victoria)
print(5 in victoria)