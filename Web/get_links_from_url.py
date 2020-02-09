#!/usr/bin/env python
import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag == "a"):
            for a in attrs:
                if(a[0] == "href"):
                    link = a[1]
                    print(link)
                    newParse = myParser()
                    newParse.feed(link)

url = input("Enter an URL: ")
req = urllib.request.Request(url)
handle = urllib.request.urlopen(req)
parser = myParser()
parser.feed(handle.read().decode('utf-8'))


