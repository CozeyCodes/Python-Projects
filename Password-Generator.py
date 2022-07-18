import random

while 1:
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&"

    c = 0

    len = int(input("How Long? ->>> "))

    amt = int(input("How Many? ->>> "))

    for i in range(0,amt):
        password = ""
        c+=1
        for i in range(0,len):
            x = random.choice(chars)
            password +=x
        print(f"{c}. Password ->>> {password}.")