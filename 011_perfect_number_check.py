class PerfectNumberCheck:
    def __init__(self, num):
        self.number = num

    def is_perfect(self):
        num = self.number
        half_of_number = num // 2
        sum_of_divisors = 0

        for i in range(1, half_of_number+1, 1):
            if num%i==0:
                sum_of_divisors += i
        return sum_of_divisors==num
    
    def display_result(self):
        if self.is_perfect():
            print(f"Number: {self.number} is a PERFECT NUMBER.")
        else:
            print(f"Number: {self.number} is NOT PERFECT NUMBER.")

print("Please enter a number: ")
number = int(input())

obj = PerfectNumberCheck(number)
obj.display_result()