# find a good audio player

import datetime as dt
import os

alram_hour = int(input("ENTER HOURS   ->>> "))
alram_min = int(input("ENTER MINUTES ->>> "))
alram_ampm = input("ENTER AM/PM ->>> ").upper()

if alram_ampm == "PM":
    alram_hour += 12

while True:
    if alram_hour == dt.datetime.now().hour and alram_min == dt.datetime.now().minute:
        print("Playing...")
        os.startfile(
            'C:\\Quixotic\\Python\\Intermediate\\PROJECTS\\ASSESTS\\TiKToK.mp4')
        break
