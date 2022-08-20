

import time


def countdown(num):
    while num:
        min, sec = divmod(num, 60)
        x = f"{min:02d}:{sec:02d}"
        print(x, end="\r")
        time.sleep(1)
        num -= 1


countdown(100)
