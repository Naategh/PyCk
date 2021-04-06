#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import requests, os, nmap, ipwhois, socket
import dns.resolver
from pprint import pprint
from time import sleep

os.system("clear")

print('''

   _____ _ _         _______        _
  / ____(_) |       |__   __|      | |
 | (___  _| |_ ___     | | ___  ___| |_ ___ _ __
  \___ \| | __/ _ \    | |/ _ \/ __| __/ _ \ '__|
  ____) | | ||  __/    | |  __/\__ \ ||  __/ |
 |_____/|_|\__\___|    |_|\___||___/\__\___|_|
					v1.1


''')

print('\033[91m1- \033[0mWhois')
print('\033[91m2- \033[0mSite Checker')
print('\033[91m3- \033[0mPort Scan')
print('\033[91m4- \033[0mNmap Scaner')
print('\033[91m5- \033[0mServer Information (Headers)')
print('\033[91m6- \033[0mNameservers of domain')
print('\033[91m7- \033[0mCMS detector')
print('\033[91m8- \033[0mExit')


def main():
    num = input('\033[36mEnter your choise: \033[0m')

    if num == '1':
        ip = input('\033[36mEnter target ip: \033[0m')
        resault = ipwhois.IPWhois(ip).lookup_whois()
        pprint(resault)
        main()

    elif num == '2':
        addr = input('\033[36mEnter target address: \033[0m')
        try:
            response = urlopen(addr).getcode()
            if response == 200:
                print('Ok, Site is up...')

        except URLError as err:
            print('Couldn\'t find a server!!!')
            print('Reason: ', err.reason)

        except HTTPError as err:
            print('Couldn\'t check target address')
            print('Error code: ', err.code)
        main()

    elif num == '3':
        site_ip = input('\033[36mEnter site ip: \033[0m')

        try:
            for port in range(20, 500):  # you can change this range
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn = sock.connect_ex((site_ip, port))
                if conn == 0:
                    print('Port \033[91m{}\033[0m:\t Open'.format(port))
                    sock.close()

        except KeyboardInterrupt:
            print('Cancel Scaning...')
            main()
        main()

    elif num == '4':
        target_ip = input('\033[36mEnter target ip: \033[0m')
        res = nmap.PortScanner().scan(target_ip, "20-160")  # range ip
        print(res)
        main()

    elif num == '5':
        server = input("\033[36mEnter target address: \033[0m")
        headers = requests.get(server).headers
        print("Some information...")
        sleep(2)

        for key, value in headers.items():  # headers is a dict so we can use items() function to get it as Key, Value
            print(key + "\t\t\t \033[91m ==> \033[0m " + value)
        main()

    elif num == '6':
        dom = input("\033[36mEnter target address (like example.com): \033[0m")
        ans = dns.resolver.query(dom, 'NS')
        for server in ans:
            print(server)
        main()

    elif num == '7':
        site = input("\033[36mEnter target address: \033[0m")

        # Wordpress Scan
        print("")
        print("Scan for Wordpress...")
        sleep(2)
        wpLcheck = requests.get(site + "/wp-login.php")
        if wpLcheck.status_code == 200 and "user_login" in wpLcheck.text and "404" not in wpLcheck.text:
            print("Wordpress detected: admin login => " + site + "/wp-admin.php")
        else:
            pass

        wpAcheck = requests.get(site + "/wp-admin")
        if wpAcheck.status_code == 200 and "user_login" in wpAcheck.text and "404" not in wpAcheck.text:
            print("Wordpress detected: admin page => " + site + "/wp-admin")
        else:
            pass

        # Joomla Scan
        print("")
        print("Scan for Joomla...")
        sleep(2)
        jmAcheck = requests.get(site + "/administrator")
        if jmAcheck.status_code == 200 and "mod-login-username" in jmAcheck.text and "404" not in jmAcheck.text:
            print("Joomla detected: administrator page => " + site + "/administrator")
        else:
            pass

        jmScheck = requests.get(site)
        if jmScheck.status_code == 200 and "joomla" in jmScheck.text and "404" not in jmScheck:
            print("Joomla detected: 'joomla' on index")
        else:
            pass

        # Drupal Scan
        print("")
        print("Scan for Drupal...")
        sleep(2)
        drRcheck = requests.get(site + "/readme.txt")
        if drRcheck.status_code == 200 and 'drupal' in drRcheck.text and '404' not in drRcheck.text:
            print("Drupal detected: Drupal Readme.txt => " + site + '/readme.txt')
        else:
            pass

        drCcheck = requests.get(site + '/core/COPYRIGHT.txt')
        if drCcheck.status_code == 200 and 'Drupal' in drCcheck.text and '404' not in drCcheck.text:
            print("Drupal detected: Drupal COPYRIGHT.txt => " + site + '/core/COPYRIGHT.txt')
        else:
            pass

        # Magento Scan
        print("")
        print("Scan for Magento...")
        sleep(2)
        mgRcheck = requests.get(site + '/RELEASE_NOTES.txt')
        if mgRcheck.status_code == 200 and 'magento' in mgRcheck.text:
            print("Magento detected: Magento Release_Notes.txt: " + site + '/RELEASE_NOTES.txt')
        else:
            pass

        mgCcheck = requests.get(site + '/js/mage/cookies.js')
        if mgCcheck.status_code == 200 and "404" not in mgCcheck.text:
            print("Magento detected: Magento cookies.js: " + site + '/js/mage/cookies.js')
        else:
            pass
        main()


    elif num == '8':
        exit()
    else:
        print("\033[91mWrong choise!!!\033[0m")
        main()


if __name__ == '__main__':
    main()
