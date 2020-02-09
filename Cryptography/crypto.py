from Crypto.Cipher import XOR
import base64, argparse

def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext))


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Simple crypto script")
    parser.add_argument("-d", "--decrypt", action="store_true")
    parser.add_argument("-e", "--encrypt", action="store_true")
    parser.add_argument("-k", "--key", required=True, help="Key for encryption/decryption")
    parser.add_argument("-t", "--text", required=True, help="Text you want encrypt/decrypt")
    args = parser.parse_args()

    if args.decrypt:
        print(decrypt(args.key, args.text))
    elif args.encrypt:
        print(encrypt(args.key, args.text))
