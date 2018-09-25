from requests import get
import sys, time

print('\33[31m Warning: Enter your target address such http://example.com/')
url = input('\033[92m Enter your target url: ')

def main():
    start = 'Start Scaning...\n'
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)
    file = open('admin_panels.txt','r')
    for link in file.read().splitlines():
        curl = url + link
        res = get(curl)
        if res.status_code == 200:
            print('\033[92m *' * 15)
            print('Admin panel found ==> {}'.format(curl))
            print('*' * 15)
        else:
            print('\033[95m Not found ==> {}'.format(curl))


if __name__ == '__main__':
    main()
