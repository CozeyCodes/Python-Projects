# import required modules
import time
import random as r

# assign something to the name variable
name = input("NAME ->>> ").upper()

# all of the random characters that we'll use
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# you can also use these special symbols
# char = "XEOGFDS#$&$€£∾π∅§Ė₩ÄĐËĦŇŒŶŴμβδΣ"

# finding the length of our name variable
length = len(name)

# making an empty string variable
c = ""

# for loop that iterates upto the length of name
for i in range(len(name)):

    # printing the index i element of our name
    x = name[i]

    # concatenating every values of x
    c += x

    # using list comprehensions to make random characters
    ran = [r.choice(char) for i in range(length)]

    # concatenating elements of list
    values = "".join(ran)

    # printing the final value of name at last
    if i == length-1:
        print(c)

    # printing the random charcters excluding the characters of our name
    print(c+values[i:-1], end="\r")

    # delaying the loop
    time.sleep(1/4)
