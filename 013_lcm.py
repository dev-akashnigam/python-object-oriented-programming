class LCM:
    def __init__(self, f_num, s_num):
        self.first_number = f_num
        self.second_number = s_num

    def find_lcm(self):
        if self.first_number > self.second_number:
            larger_number = self.first_number
            smaller_number = self.second_number
        else:
            larger_number = self.second_number
            smaller_number = self.first_number
        
        multiple = 1
        while True:
            if (larger_number*multiple)%smaller_number==0:
                lcm = larger_number*multiple
                break
            multiple+=1
        return lcm
    
    def display_result(self):
        print(f"LCM of {self.first_number} and {self.second_number} = {self.find_lcm()}")

print("Please enter the first number: ")
first_num = int(input())

print("Please enter the second number: ")
second_num = int(input())

obj = LCM(first_num, second_num)
obj.display_result()