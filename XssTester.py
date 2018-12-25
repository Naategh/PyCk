#!/usr/bin/python3.5
import requests
import argparse
from subprocess import call
import sys

call('clear')
print('\033[1;31mWarning: ','\033[0mYour url should such as: http://example.com/search?q=')
url = input('Enter your url: ')
print('\n  Start Scaning be wait...')

def core():
    vulnerable = []
    f = open('XssPayloads.txt','r')
    for payload in f.read().splitlines():
        link = url+payload
        r = requests.get(link)
        if payload.lower() in r.text.lower():
            print('\033[1;31m [-] This site vulnerable to: ' + '\033[0;32m' + payload + '\033[0m')

            if payload not in vulnerable:
                vulnerable.append(payload)
        else:
            pass

    print('[-] Availabe payloads:')
    print('-- \n'.join(vulnerable))

core()
