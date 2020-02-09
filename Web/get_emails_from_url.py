#!/usr/bin/env python
import urllib.request, urllib.error, urllib.parse
import re, sys

url = input("Enter an URL: ")
res = urllib.request.Request(url)
content = urllib.request.urlopen(res).read().decode('utf-8')

pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+[-a-zA-Z0-9._]+")
emails = re.findall(pattern, content)
print(emails)



