'''create a class Programmer for storing information
of few programmers working at a certain company.'''

class Programmer:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def getinfo(self):
        print(f"The name of the programmer is {self.name} who works for {self.brand}.")

print("---------------------------------------")
num = int(input("How Many Data To Store?: "))
print("---------------------------------------")

for i in range(num):
    name = input("Enter The Name: ")
    name = name.title()

    brand = input("Enter The Brand: ")
    brand = brand.title()

    print("---------------------------------------")

    x = Programmer(name, brand)
    x.getinfo()

    print("---------------------------------------")
