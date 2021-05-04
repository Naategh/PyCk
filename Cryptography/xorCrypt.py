#!/usr/bin/env python3.6

"""
xorCrypt [python3]

This tool is written in python3 and it serves the feature of implementing the XOR cryptographic algorithms. The arguments that the tool takes in are described below.
--key   File containting the key
--text  File containing the text
Using these arguments, the user inputs information to this tool, and then it processes the task.

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
import argparse
import logging

def xorcrypt(cipher_text, key):
    """ The function for implementing the XOR cryptographic algorithm. The function takes two arguments as input, they are : cipher_text and key. The ciper_text is the plain user entered text that is needed to be encrypted, and the key is the password that is used to encrypt the text. """

    endRes = ""
    if len(cipher_text) != len(key):
        logging.error("cipher and key must be the same length")
    else:
        for i in range(0, len(cipher_text)):
            # Converts a character from cipher_text and key to its decimal value
            # Then xors the two
            intResult = ord(cipher_text[i]) ^ ord(key[i])

            # Convert intResult to its character representation
            endRes += chr(intResult)
    return endRes

def main():
    # DRIVER CODE

    # Parsing the user entered arguments while calling the script (.py file)
    parser = argparse.ArgumentParser(description = 'xorCrypt')
    parser.add_argument("--key", type = argparse.FileType('r'), help = 'File containing the key')
    parser.add_argument("--text", type = argparse.FileType('r'), help = 'File containing the text')
    args = parser.parse_args()

    # Checking the user entered arguments
    if not args.key or not args.text:
        # If the user has not entered the required arguments, then we display the error on the console screen

        logging.error('arguments required to run')

    else:
        # If the user entered proper arguments, then we continue to complete the task

        # Calling xorcrypt using the input from the two files, and then printing the result on the console screen
        result = xorcrypt(str(args.text.read()), str(args.key.read()))
        print(result)
        input('\nPress enter key to continue...')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script

        exit()
    except Exception as e:
        # If we encounter an error during the process, then we display the error message on the console screen and exit

        input('\n[ Error : {} ]\nPress enter key to continue...'.format(e))
        exit()