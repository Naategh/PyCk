import ftplib

def main(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print(ftp.getwelcome())
        ftp.set_pasv(1)
        print(ftp.dir())        
        print('\n[*] ' + str(hostname) +' FTP Anonymous Login Succeeded.')
        return ftp
    except Exception as e:
        print(str(e))
        print('\n[-] ' + str(hostname) +' FTP Anonymous Login Failed.')
        return False

if __name__ == '__main__':
    target = input("Enter target ip: ")
    main(target)
