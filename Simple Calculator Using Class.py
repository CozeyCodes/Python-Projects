'''Create a Class Calculator Capable of finding
square, cube & square root of a number.'''

class Calculator:

    def __init__(self, num):
        self.num = num

    def sqr(self):
        print(f"The sqaure of {self.num} is {self.num **2}.")
        
    def sqr_root(self):
        print(f"The sqaure root of {self.num} is {self.num **0.5}.")
    
    def cube(self):
        print(f"The cube of {self.num} is {self.num **3}.")

    def cube_root(self):
        print(f"The cube root of {self.num} is {self.num **1/3}.")
    

num = int(input("Enter A Number: "))

x = Calculator(num)
x.sqr()
x.sqr_root()
x.cube()
x.cube_root()
