

list = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

try:
    name = input("Your Name ->>> ").upper()

    for i in name:
        x = list.index(i)
        print(x, end=" ")

except ValueError:
    print("INTEGER VALUE FORBIDDEN!")
