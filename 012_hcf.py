class HCF:
    def __init__(self, fNum, sNum):
        self.first_num = fNum
        self.second_num = sNum

    def find_HCF(self):
        if self.first_num > self.second_num:
            larger_num = self.first_num
            smaller_num = self.second_num
        else:
            larger_num = self.second_num
            smaller_num = self.first_num
        
        hcf = 1
        for i in range(smaller_num, 1, -1):
            if self.first_num%i==0 and self.second_num%i==0:
                hcf = i
                break
        return hcf
    
    def display_result(self):
        print(f"HCF of {self.first_num} and {self.second_num} = {self.find_HCF()}")

print("Please enter the first number: ")
first_num = int(input())

print("Please enter the second number: ")
second_num = int(input())

obj = HCF(first_num, second_num)
obj.display_result()
