class RightAngledTrianglePattern:
    def __init__(self, rc):
        self.row_count = rc

    def print_right_angled_triangle(self):
        for row in range(1, self.row_count+1, 1):
            for col in range(1, row+1, 1):
                print("*", end=" ")
            print()

print("Please enter the number of rows required in the right angled triangle: ")
row_count = int(input())

obj = RightAngledTrianglePattern(row_count)
obj.print_right_angled_triangle()

    