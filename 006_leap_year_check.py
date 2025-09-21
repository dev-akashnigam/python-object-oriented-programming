class LeapYearCheck:
    def __init__(self, y):
        self.year = y

    def isLeapYear(self):
        if self.year%100 == 0:
            if self.year%400 == 0:
                return True
            else:
                return False
        else:
            if self.year%4 == 0:
                return True
            else:
                return False
            
    def displayResult(self):
        if self.isLeapYear():
            print(f"Year: {self.year} is a leap year")
        else:
            print(f"Year: {self.year} is NOT leap year")

print("Please enter the year: ")
year = int(input())

obj = LeapYearCheck(year)
obj.displayResult()
