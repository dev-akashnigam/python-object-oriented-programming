class ReverseNumber:
    def __init__(self, num):
        self.number = num

    def get_reversed_number(self):
        original_number = self.number
        reversed_number = 0

        while original_number!=0:
            last_digit = original_number % 10
            reversed_number = reversed_number * 10 + last_digit

            original_number = original_number // 10
        return reversed_number
    
    def display_result(self):
        print(f"Reverse of number {self.number} = {self.get_reversed_number()}")

print("Please enter a number: ")
num = int(input())

obj = ReverseNumber(num)
obj.display_result()