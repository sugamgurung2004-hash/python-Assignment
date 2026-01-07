# Write a function to calculate area and perimeter of a rectangle based on length and breath.


def calculation(length, breadth):
    area = length*breadth
    perimeter = 2*(length + breadth)
    return area, perimeter
    
ar, pm = calculation(2,4)