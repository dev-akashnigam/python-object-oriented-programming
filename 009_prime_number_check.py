import math

class PrimeNumberCheck:
    def __init__(self, num):
        self.number = num

    def is_prime(self):
        if self.number<=1:
            return False
        elif self.number==2:
            return True
        elif self.number%2==0:
            return False
        else:
            sqrt_number = math.isqrt(self.number)
            is_prime = True
            for i in range(3, sqrt_number+1, 2):
                if self.number%i==0:
                    is_prime = False
                    break
            return is_prime
    
    def display_result(self):
        if self.is_prime():
            print(f"Number {self.number} is PRIME.")
        else:
            print(f"Number {self.number} is NOT PRIME.")

print("Please enter a number: ")
num = int(input())

obj = PrimeNumberCheck(num)
obj.display_result()
