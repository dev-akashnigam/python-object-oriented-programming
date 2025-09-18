class SumDifferenceProductQuotientOf2Nos:

    def __init__(self, x, y):
        self.first_num = x
        self.second_num = y

    def get_sum(self):
        return self.first_num + self.second_num

    def get_difference(self):
        return self.first_num - self.second_num
    
    def get_product(self):
        return self.first_num * self.second_num
    
    def get_quotient(self):
        return self.first_num / self.second_num

print("Please enter first number: ")
num_x = int(input())

print("Please enter second number: ")
num_y = int(input())

obj = SumDifferenceProductQuotientOf2Nos(num_x, num_y)

print(f"Sum = {obj.get_sum()}")
print(f"Difference = {obj.get_difference()}")
print(f"Product = {obj.get_product()}")
print(f"Quotient = {obj.get_quotient()}")