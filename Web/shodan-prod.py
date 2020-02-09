#!/usr/bin/env python
# Search for sdifferent products in shodan

import shodan

def main():

    API_KEY = input("Enter your shodan api key: ")
    # If you don't want enter your shodan key every time you can define API_KEY as a string like API_KEY = "YOUR_SHODAN_KEY"
    api = shodan.Shodan(API_KEY)
    try:
        prod = input("Enter product name: ")
        res = api.search(prod)

        print("Results found {}".format(res['total']))
        for r in res['matches']:
            print("IP: {}".format(res['ip_str']))
            print(res['data'])
            print("")

    except shodan.APIError as e:
        print("Error: {}".format(e))

    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)

if __name__ == '__main__':
    main()

