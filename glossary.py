# make it more visually more attractive by using pretty tables

path = r"C:\Quixotic\Python\Intermediate\PROJECTS\ASSESTS\Glossary.txt"

try:
    num = int(input("How Many Meanings? ->>> "))

    for i in range(num):

        with open(path, "a") as f:
            key = input("Word ->>> ").title()
            meaning = input("Meaning ->>> ").title()
            f.write(f"{key} : {meaning}\n")

except Exception:
    print("Invalid Input!")
