class EvenOrOdd:
    def __init__(self, num):
        self.number = num

    def isEven(self):
        return self.number%2==0
    
    def displayResult(self):
        if self.isEven():
            print(f"Number: {self.number} is even.")
        else:
            print(f"Number: {self.number} is odd.")

print("Please enter a number: ")
num = int(input())

obj = EvenOrOdd(num)
obj.displayResult()