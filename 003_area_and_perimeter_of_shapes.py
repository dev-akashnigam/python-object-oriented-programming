import math

class AreaAndPerimeterOfShapes:
    def __init__(self, r, l, w, s1, s2, s3):
        self.radius_of_circle = r
        self.length_of_rectangle = l
        self.width_of_rectangle = w
        self.side1_of_triangle = s1
        self.side2_of_triangle = s2
        self.side3_of_triangle = s3

    def calc_area_of_circle(self):
        return math.pi * (self.radius_of_circle ** 2)

    def calc_perimeter_of_circle(self):
        return 2 * math.pi * self.radius_of_circle

    def calc_area_of_rectangle(self):
        return self.length_of_rectangle * self.width_of_rectangle

    def calc_perimeter_of_rectangle(self):
        return 2 * (self.length_of_rectangle + self.width_of_rectangle)

    def calc_perimeter_of_triangle(self):
        return self.side1_of_triangle + self.side2_of_triangle + self.side3_of_triangle

    def calc_area_of_triangle(self):
        semi_perimeter_of_triangle = (self.side1_of_triangle + self.side2_of_triangle + self.side3_of_triangle) / 2
        return math.sqrt(semi_perimeter_of_triangle * abs(semi_perimeter_of_triangle - self.side1_of_triangle) * abs(semi_perimeter_of_triangle - self.side2_of_triangle) * abs(semi_perimeter_of_triangle - self.side3_of_triangle))
    
    def displayResult(self):
        print(f"Area and Perimeter of Circle of radius: {self.radius_of_circle:.2f} = {self.calc_area_of_circle():.2f}, {self.calc_perimeter_of_circle():.2f}")
        print(f"Area and Perimeter of Rectangle of length: {self.length_of_rectangle:.2f} and width: {self.width_of_rectangle:.2f} = {self.calc_area_of_rectangle():.2f}, {self.calc_perimeter_of_rectangle():.2f}")
        print(f"Area and Perimeter of Triangle with side having lengths: {self.side1_of_triangle:.2f}, {self.side2_of_triangle:.2f} and {self.side3_of_triangle:.2f} = {self.calc_area_of_triangle():.2f}, {self.calc_perimeter_of_triangle():.2f}")
    
print("Please enter the radius of circle: ")
radius_of_circle = float(input())

print("Please enter the length of rectangle: ")
length_of_rectangle = float(input())

print("Please enter the width of rectangle: ")
width_of_rectangle = float(input())

print("Please enter the length of first side of triangle: ")
first_side_of_triangle = float(input())

print("Please enter the length of second side of triangle: ")
second_side_of_triangle = float(input())

print("Please enter the length of third side of triangle: ")
third_side_of_triangle = float(input())

obj = AreaAndPerimeterOfShapes(radius_of_circle, length_of_rectangle, width_of_rectangle, first_side_of_triangle, second_side_of_triangle, third_side_of_triangle)
obj.displayResult()