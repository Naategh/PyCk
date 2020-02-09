#!/usr/bin/python3.5
import requests
from subprocess import call

def main():
    call("clear")
    print("\033[1;31mWarning: ", "\033[0mYour target url should be like http://example.com/search?q=")
    url = input("Enter your target url: ")
    print("\n  Start Scanning be wait...")

    vulnerable = []
    f = open("XssPayloads.txt", "r")
    for payload in f.read().splitlines():
        link = url + payload
        r = requests.get(link)
        if payload.lower() in r.text.lower():
            print("\033[1;31m [-] This site is vulnerable to: \033[0m" + payload)

            if payload not in vulnerable:
                vulnerable.append(payload)
            else:
                pass
        else:
            pass
    f.close()

    print("[-] Available payloads:")
    print("\n".join(vulnerable))


if __name__ == "__main__":
    main()
