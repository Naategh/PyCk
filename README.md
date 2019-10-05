# PyCk v1.1


This is a simple project that implements some useful scripts.
This project can be used for learning scripting with Python and 
creating simple pentesting tools, too.

And I should also point out that
The reason for using different and large libraries in this project
It is for educational use.

## Installation

- git clone https://github.com/Naategh/PyCk.git
- cd PyCk
- pip3 install -r requirements.txt

## Requirements
- Python 3.5


## Description

| File                  | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| `admin_panel_finder.py` | Brute force urls to find admin panels                                 |
| `admin_panels.txt`      | List of dir/urls to brute; for use with admin_panel_finder.py         |
| `email_bomber.py`       | Send 1000 emails quickly for spam to another email                    |
| `email_temper.py`       | Query tempail.com and print email address                             |
| `lfi_tester.py`         | Local file inclusion tester                                           |
| `Site_Tester.py`        | Variety of utilities: whois, website availability, nmap, CMS detector |
| `sysInfo.py`           | Host system information                                               |
| `text_to_hash.py`       | Hash text using a variety of hashing algorithims                      |
| `XssTester.py`          | Test Cross Site Scripting Vulnerability                               |
| `XssPayloads.txt`       | List of XSS payloads for use with XssTester.py                        |
| `postexfil.py`          | Http server that saves POSTED content out to file useful for exfil    |
| `sniff.py`              | Scapy based sniffer                                                   |
| `wifi_scan.py`          | Iw based wireless scanner, only works on linux                        |
| `xorCrypt.py`           | xor encryption/decryption script                                      |
| `bulk_bomber.py`        | An email_bomber extension that has multiprocessing                    |
| `getFuncs.py`           | A r2pipe script that uses radare to get a function list: INSTALL R2   |


## Roadmap
This is an educational project to learn to make simple and useful tools for pentest in python.
If you have any idea share with us to improve it, Please.
Checkout the Writting.md file to learn about how to use this repo for 
teaching yourself how to write your own security related python scripts.

## License
This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details

## Contact
- Email: manamtabeshekan@gmail.com
- Telegram: @Naategh
