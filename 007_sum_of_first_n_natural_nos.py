class SumOfFirstNNaturalNos:
    def __init__(self, num):
        self.number = num

    def calc_sum(self):
        sum = 0
        for i in range(1, self.number+1, 1):
            sum += i
        return sum
    
    def print_result(self):
        print(f"Sum of first {self.number} natural numbers = {self.calc_sum()}")

print("Please enter the natural number till where sum is required: ")
nat_num = int(input())
obj = SumOfFirstNNaturalNos(nat_num)
obj.print_result()
