import random

while 1:
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&"

    len = int(input("Enter the Length of your Password ->>> "))

    amt = int(input("How many Passwords do you want? ->>> "))

    for i in range(0,len):
        password = ""
        for i in range(0,amt):
            x = random.choice(chars)
            password +=x
        print("Your Passowrd is", password)