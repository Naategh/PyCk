"""
Text to Hash [python3]

This tool is written in python3 and it serves the feature of hashifying the user entered text. To use the tool follow the below commands and arguments guide.
python3 text_to_hash.py <argument> <inputs>

Arguments
-t, --text  The plain text to be converted to hash form
-T, --Type  The type of the hashing algorithm

Author : Naategh (https://github.com/Naategh/)
Created on : -

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 4, 2021

Changes made in last modification :
1. Made the code clean and error free.
2. Added the function of quiting the script immediately when the user presses the CTRL+C.
3. Added the commented docs, making things easy for the readers of the code.

Authors contributed to this script (Add your name below if you have contributed) :
1. Naategh (github:https://github.com/Naategh/)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
import hashlib
import argparse


def main():
    # DRIVER CODE

    # Parsing the user entered arguments
    parser = argparse.ArgumentParser(description = 'Convert text to hash')
    parser.add_argument('-t', '--text', dest = 'text', required = True)
    parser.add_argument('-T', '--Type', dest = 'type', required = True)
    args = parser.parse_args()

    # Encoding the user specified text to utf-8 encoding
    encoder = args.text.encode('utf_8')
    myHash = ''

    if args.type.lower() == 'md5':
        # If the user specified md5 hashing algorithm

        myHash = hashlib.md5(encoder).hexdigest()
    elif args.type.lower() == 'sha1':
        # If the user specified sha1 hashing algorithm

        myHash = hashlib.sha1(encoder).hexdigest()
    elif args.type.lower() == 'sha224':
        # If the user specified sha224 hashing algorithm

        myHash = hashlib.sha224(encoder).hexdigest()
    elif args.type.lower() == 'sha256':
        # If the user specified sha256 hashing algorithm

        myHash = hashlib.sha256(encoder).hexdigest()
    elif args.type.lower() == 'sha384':
        # If the user specified sha384 hashing algorithm

        myHash = hashlib.sha384(encoder).hexdigest()
    elif args.type.lower() == 'sha512':
        # If the user specified sha512 hashing algorithm

        myHash = hashlib.sha512(encoder).hexdigest()
    else:
        # If the user specified hashing algorithm is not supported by the script

        raise TypeError('The specified hashing algorithm is not supported by this tool')

    # If there are no errors in the process, then we display the created hash on the console screen
    print('[$] Hash formed : {}'.format(myHash))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script

        exit()
    except Exception as e:
        # If there are any errors during the process, then we display the error message on the console screen

        input('\n[ Error : {} ]\nPress enter key to continue...')
        exit()