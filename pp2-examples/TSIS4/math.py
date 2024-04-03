#Task 1
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 15
radian = degree_to_radian(degree)
print("Output radian:", radian)

#Task 2
def area_of_trapezoid(height, base1, base2):
    return (height * (base1 + base2)) / 2

height = 5
base1 = 5
base2 = 6
area = area_of_trapezoid(height, base1, base2)
print("Expected Output:", area)

#Task 3
import math

def area_of_polygon(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

n = 4
side_length = 25
area = area_of_polygon(n, side_length)
print("The area of the polygon is:", area)

#Task 4
def area_of_parallelogram(base, height):
    return base * height

base = 5
height = 6
area = area_of_parallelogram(base, height)
print("Expected Output:", area)