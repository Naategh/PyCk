#!/usr/bin/python
#PHPMailer Version Checker

import urllib.request, urllib.error, urllib.parse
import re

def checker(target):
   page = urllib.request.urlopen(target).read().decode('utf-8')
   if bool(re.search(r'5\.2\.(?:0|1)[0-8]', page)):
      print("\n" + target + ' appears to have PHPMailer installed!')
      print('Installed version is ', page)
      print('Check https://www.exploit-db.com/exploits/40969/ or https://www.exploit-db.com/exploits/40974/ for a possible exploit.')
   else:
      print("Target does not appear to be vulnerable ):")
      
def main():
   print("PHPMailer Checker")
   
   while True:
      target = input("Enter target URL: ")
      if 'http://' in target[:7] or 'https://' in target[:8]:
         break
   if bool(re.search(r'/VERSION$', target)):
      checker(target)
   else: 
      checker(target + "/VERSION")
        
if __name__ == "__main__":
   main()
