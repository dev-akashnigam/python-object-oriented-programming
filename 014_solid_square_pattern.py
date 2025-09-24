class SolidSquarePattern:
    def __init__(self, r_count):
        self.row_count = r_count

    def print_solid_square(self):
        col_count = self.row_count
        for row in range(1, self.row_count+1, 1):
            for col in range(1, col_count+1, 1):
                print("*", end=" ")
            print()

print("Please enter the number of rows required in the solid square pattern: ")
rows = int(input())

obj = SolidSquarePattern(rows)
obj.print_solid_square()