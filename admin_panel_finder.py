#!/usr/bin/env python
from requests import get
import sys, time

print("\033[91mWarning: Enter your target address such http://example.com/\033[0m")
url = input("Enter your target url: ")

def main():
    start = "Start Scaning...\n"
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)
    file = open("admin_panels.txt","r")
    for link in file.read().splitlines():
        curl = url + link
        res = get(curl)
        if res.status_code == 200:
            print("*" * 15)
            print("Admin panel found ==> {}".format(curl))
            print("*" * 15)
        else:
            print("\033[91m Not found ==> {} \033[0m".format(curl))

if __name__ == "__main__":
    main()
