# Create a class called Point that has two attributes x-coordinate and y-coordinate. It should have method called dist_from_origin that should give how far point is from origin.
#Hint:d=√(x2+y2)Hint: d = √(x² + y²)Hint:d=√(x2+y2).
#Operator + should add as (x1 + x2, y1 + y2), - should implement (x1 − x2, y1 − y2).
#Print should display P(x, y).
# Also, overwrite relational operators that shows if point is smaller or greater based on distance from origin
# (i.e. overwrite <, >, <=, >=, == and !=).Initialize two point objects to demo above methods.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    