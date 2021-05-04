"""
crypto.py [python3]

This tool is written in python3 and it serves the feature of encryption and decryption of text (strings) using a key (password). How to use this tool, just type the following commands on terminal and press enter key : 'python3 crypto.py <arguments>'.
The arguments that the script uses are listed below :
 -d, --decrypt    For decryption process
 -e, --encrypt    For encryption process
 -k, --key        For specifying the key of the encryption/decryption
 -t, --text       For specifying the text for the encryption/decryption

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
try:
    from Crypto.Cipher import XOR
    import base64, argparse
except Exception as e:
    # If there are any errors encountered during the importing of the required modules, then we display the error on the console screen

    input('\n[ Error : {} ]\nPress enter key to continue...'.format(e))
    exit()

def encrypt(key, plaintext):
    """ The function to encrypt the plain text into a cipher text using an user specified key. The function takes two arguments : key, plaintext """

    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
    """ The function to decrypt the cipher text into a plain text using an user specified key. The function takes two arguments : key, plaintext. Note : For decryption of a cipher text to its original version, the function would require the original key that was used to encrypt the string/text. """

    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ciphertext))


if __name__ == '__main__':
    try:
      # First, we will parse all the arguments entered by the user while calling this script
      parser = argparse.ArgumentParser('Simple crypto script')
      parser.add_argument('-d', '--decrypt', action = 'store_true')
      parser.add_argument('-e', '--encrypt', action = 'store_true')
      parser.add_argument('-k', '--key', required = True, help = 'Key for encryption/decryption')
      parser.add_argument('-t', '--text', required = True, help = 'Text you want encrypt/decrypt')
      args = parser.parse_args()

      if args.decrypt:
          # If the user choosed encryption, then we continue to execute the task

          print(decrypt(args.key, args.text))
      elif args.encrypt:
          # If the user choosed decryption, then we continue to execute the task

          print(encrypt(args.key, args.text))
      else:
        # If the user's choice is neither encryption nor decryption, then we display the error on the console screen

        input('\n[ Error : Please specify either encryption (-e, --encrypt) or decryption (-d, --decryption) ]\nPress enter key to continue...')
        exit()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script

        exit()
    except Exception as e:
        # If there are any errors encountered during the process, then we display the error on the console screen

      input('\n[ Error : {} ]\nPress enter key to continue...'.format(e))
      exit()