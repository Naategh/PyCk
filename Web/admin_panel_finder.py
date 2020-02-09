#!/usr/bin/env python
import requests
import sys
from time import sleep


def main():
    print("\033[91mWarning: Enter your target address such http://example.com\033[0m")
    url = input("Enter your target url: ")  # Get target url from user

    start = "Start Scaning...\n"
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.1)
    file = open("admin_panels.txt", "r")  # Open files containing possible admin directories
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print("*" * 15)
                print("Admin panel found ==> {}".format(curl))
                print("*" * 15)
            else:
                print("\033[91m Not found ==> {} \033[0m".format(curl))
    except KeyboardInterrupt:
        print("\033[91m Shutdown Request! \033[0m")
    except:
        print("\033[91m Unknown Error! \033[0m")
    file.close()


if __name__ == "__main__":
    main()
