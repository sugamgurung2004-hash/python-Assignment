#calculate area and perimeter of circle based on diameter

#diameter = float(input("Enter the diameter of the circle: "))
diameter=int(input("Enter the diameter: "))
radius =diameter / 2
pi = 3.14159

area = pi * radius ** 2
perimeter = 2 * pi * radius

print("Area of the circle:", area)
print("Perimeter (Circumference) of the circle:", perimeter)