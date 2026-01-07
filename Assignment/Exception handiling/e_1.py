# Write a function can_drink that takes age as argument checks if user can drink. If user is 18+, return True else return False. Note: You need to raise TypeError if age is not integer value, ValueError if age is below 0, AssertionError if age is above 100.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"P({self.x}, {self.y})"

    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __le__(self, other):
        return self.dist_from_origin() <= other.dist_from_origin()

    def __ge__(self, other):
        return self.dist_from_origin() >= other.dist_from_origin()

    def __eq__(self, other):
        return self.dist_from_origin() == other.dist_from_origin()

    def __ne__(self, other):
        return self.dist_from_origin() != other.dist_from_origin()


p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)                  # P(3, 4)
print(p2)                  # P(1, 2)

print("Distance p1:", p1.dist_from_origin())
print("Distance p2:", p2.dist_from_origin())

print("Addition:", p1 + p2)
print("Subtraction:", p1 - p2)

print("p1 > p2:", p1 > p2)
print("p1 < p2:", p1 < p2)
print("p1 == p2:", p1 == p2)
