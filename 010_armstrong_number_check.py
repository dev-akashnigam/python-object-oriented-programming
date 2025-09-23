class ArmstrongNumberCheck:
    def __init__(self, num):
        self.number = num

    def find_digits_in_number(self):
        num = self.number
        total_digits_in_number = 0
        while num!=0:
            num = num // 10
            total_digits_in_number += 1
        return total_digits_in_number
    
    def isArmstrong(self):
        num = self.number
        total_digits_in_number = self.find_digits_in_number()
        sum = 0
        while num!=0:
            last_digit_of_number = num % 10
            sum = sum + (last_digit_of_number ** total_digits_in_number)

            num = num // 10
        return sum==self.number
    
    def display_result(self):
        if self.isArmstrong():
            print(f"Number {self.number} is ARMSTRONG NUMBER.")
        else:
            print(f"Number {self.number} is NOT ARMSTRONG NUMBER.")

print("Please enter a number: ")
number = int(input())

obj = ArmstrongNumberCheck(number)
obj.display_result()
