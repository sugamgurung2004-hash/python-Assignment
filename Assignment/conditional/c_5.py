# Take three side length of triangle and display if triangle is eQuilateral, isosceles or scalene

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))


if a == b == c:
        print("The triangle is Equilateral.")
elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
else:
        print("The triangle is Scalene.")

