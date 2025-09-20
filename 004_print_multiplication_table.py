class MultiplicationTable:
    def __init__(self, n):
        self.number = n

    def printTable(self):
        for i in range(1, 11, 1):
            print(f"{self.number} X {i} = {self.number*i}")

print("Please enter a number: ")
num = int(input())

obj = MultiplicationTable(num)
obj.printTable()