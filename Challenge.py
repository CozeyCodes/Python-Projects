import random

def main():

    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("[ MENU ]                     [ PRESS ]")
    print("1. C to F Conversion.           [1]")
    print("2. Suqare Root of A Number.     [2]")
    print("3. 10 Lucky Numbers Between 2.  [3]")
    print("4. Multipli. Table of A Number. [4]")
    print("<<<<<<<<<<<<<EXIT>>>>>>>>>>>>>  [X]")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    ans = input("ENTER YOUR CHOICE! ->>> ").upper()

    list = ["1", "2", "3", "4","X"]

    if ans not in list:
        print("Please Choose A Valid Option!")
        quit()
    else: 
        pass

    print(F"OK, LET'S GO WITH! ->>> {ans}")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    if ans == "X":
        quit()

    elif ans == "1":
        print("   </> CELSIUS INTO FAHRENHEIT </>")
        celsius = int(input("DEGREE IN CENTRIGRADE: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C IS EQUAL TO {fahrenheit}°F.")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    elif ans =="2":
        print("   </> SQUARE ROOT OF A NUMBER </>  ")
        num = int(input("ENTER A NUMEBR ->>> "))
        sqr = num**0.5
        print(f"SQUARE ROOT OF {num} IS {sqr:.7f}.")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    elif ans =="3":
        print("    </> TOP 10 LUCKY NUMBERS </>  ")
        num1 = int(input("STARTING NUMBER ->>> "))
        num2 = int(input("ENDING NUMBER   ->>> "))
        for i in range (1,11):
            x = random.randint(num1,num2)
            print(f"{x}, ", end="")
        print("\n")    
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")    
            
    elif ans =="4":
        n = int(input("ENTER A NUMBER ->>> "))
        for i in range (1,11):
            print(f"{i}. {n} × {i} = {n*i}")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    else:
        choice = input("PLAY AGAIN? [Y/N] ->>> ").upper()
        if choice == "Y":
            main()
        else:
            print("Goodbye, We'll Miss You!")
            exit()

    choice = input("PLAY AGAIN? UwU [Y/N] ->>> ").upper()
    if choice == "Y":
            main()
    else:
            print("Goodbye, We'll Miss You! ToT")
            exit()

main()