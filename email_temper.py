from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://tempail.com/en/'
html = urlopen(url)
bs = BeautifulSoup(html.read(),'html.parser')

for e in bs.find_all('input',{'id':'eposta_adres'}):
    if 'value' in e.attrs:
        print('Your temp email is:\t',e.attrs['value'])
    else:
        print('Couldn\'t get temp mail!')
