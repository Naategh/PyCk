from socket import gethostbyaddr
import os
ip = '192.168.1.'

for i in range(1,256):
    try:
        up = gethostbyaddr(ip+str(i))
        os_ = os.system('nmap -vv -A {} | grep Running'.format(ip+str(i)))
        print(ip+str(i)+'  '+up[0])
        print('==> ',os_)

    except:
        pass
