#import modules
from datetime import datetime as dt
import time

# windows host path
hosts = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# sites to block
websites = ["www.instagram.com", "instagram.com"]

# time when blocker will work
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("404 Access Denied!")
        with open(hosts, "r+") as f:
            content = f.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    f.write(redirect + "\t" + site + "\n")

    else:
        with open(hosts, 'r+') as f:
            content = f.readlines()
            for line in content:
                if not any(site in line for site in websites):
                    f.write(line)
                    f.truncate()
                print("Access Granted!")
        time.sleep(5)
