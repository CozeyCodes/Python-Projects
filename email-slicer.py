

email = input("Email ->>> ")

pos = email.index("@")

username_list = email[:pos]

domain_list = email[pos+1:]

dot = domain_list.index(".")

print("Username ->>>", username_list)

print("Domain Name->>>", domain_list[:dot])

print("Domain Extension ->>>", domain_list[dot+1:])
