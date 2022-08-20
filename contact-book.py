# format more using pretty table
# make the search term name as valid
# making it more advanced by storing data into a file

names = []

mails = []

max = 2

for i in range(max):
    ask_name = input("ENTER PERSON'S NAME ->>> ").title()
    ask_mail = input("ENTER HIS/HER EMAIL ->>> ").lower()
    names.append(ask_name)
    mails.append(ask_mail)

print(" | NAMES |\t\t|MAILING ADDRESS|\n")

for i in range(max):
    print(f"{names[i]}\t\t{mails[i]}")


search = input("\nSEARCH CONTACTS OF ->>> ").title()
x = search.split()


if search in names:
    index = names.index(search)
    print(f"\nName  ->>> {search}\nEmail ->>> {mails[index]}")
else:
    print("CONTACT NOT FOUND!")
