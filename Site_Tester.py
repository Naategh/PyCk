from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import ipwhois, socket
import nmap
from pprint import pprint


print('''

   _____ _ _         _______        _
  / ____(_) |       |__   __|      | |
 | (___  _| |_ ___     | | ___  ___| |_ ___ _ __
  \___ \| | __/ _ \    | |/ _ \/ __| __/ _ \ '__|
  ____) | | ||  __/    | |  __/\__ \ ||  __/ |
 |_____/|_|\__\___|    |_|\___||___/\__\___|_|
					v0.8


''')


print('1- Whois')
print('2- Site Checker')
print('3- Port Scan')
print('4- Nmap Port Scaner')
print('5- Exit')
num = input('Enter your choise: ')


def main():
    if num == '1':
        ip = input('Enter target ip: ')
        resault = ipwhois.IPWhois(ip).lookup_whois()
        pprint(resault)
        

    elif num == '2':
        addr = input('Enter target address: ')
        try:
            response = urlopen(addr).getcode()
            if response == '200':
                print('Ok,site is up...')
			

        except URLError as err:
            print('Couldn\'t find a server!!!')
            print('Reason: ',err.reason)

        except HTTPError as err:
            print('Couldn\'t check target address')
            print('Error code: ',err.code)

    elif num == '3':
        site_ip = input('Enter site ip: ')
        sock = socket.socket(family=AF_INET,type=SOCK_STREAM)
        for i in range(0,1000):
            try:
                conn = sock.connect_ex((site_ip,port))
                if conn == 0:
                    print('Port {}:\t Open')
                    conn.close()

            except KeyboardInterrupt:
                print('Cansel Scaning...')
                exit()

    elif num == '4':
        target_ip = input('Enter target ip: ')
        res = nmap.PortScanner().scan(target_ip)
        print(res)

    elif num == '5':
        exit()
    else:
        print('Wrong choise!!!')

if __name__ == '__main__':
    main()
