#!/usr/bin/env python3.6
#xorCrypt.py
#impliments xor encryption/decryption
import argparse
import logging

def xorcrypt(cipher_text, key):
    #Xor encryption implimentation
    endRes = ""
    if len(cipher_text) != len(key):
        logging.error("cipher and key must be the same length")
    else:
        for i in range(0, len(cipher_text)):
            #Converts a character from cipher_text and key to its decimal value
            #Then xors the two
            intResult = ord(cipher_text[i]) ^ ord(key[i])
            #Convert intResult to its character representation
            endRes += chr(intResult)
    return endRes

def main():
    #Argparse setup
    parser = argparse.ArgumentParser(description="xorCrypt")
    parser.add_argument("--key", type=argparse.FileType("r"), help="File containing the key")
    parser.add_argument("--text", type=argparse.FileType("r"), help="File containing the text")
    args = parser.parse_args()
    if not args.key or not args.text:
        logging.error("arguments required to run")

    else:
        #call xorcrypt using the input from the two files
        res = xorcrypt(str(args.text.read()), str(args.key.read()))
        print(res)

if __name__ == "__main__":
    main()
