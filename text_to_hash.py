import hashlib
import argparse

def main(text,hashType):
    encoder = text.encode('utf_8')

    if hashType.lower() == 'md5':
        myhash = hashlib.md5(encoder).hexdigest()

    elif hashType.lower() == 'sha1':
        myhash = hashlib.sha1(encoder).hexdigest()

    elif hashType.lower() == 'sha224':
        myhash = hashlib.sha224(encoder).hexdigest()

    elif hashType.lower() == 'sha256':
        myhash = hashlib.sha256(encoder).hexdigest()

    elif hashType.lower() == 'sha384':
        myhash = hashlib.sha384(encoder).hexdigest()

    elif hashType.lower() == 'sha512':
        myhash = hashlib.sha512(encoder).hexdigest()

    else:
        print('Script not support this hash type')

    print(myhash)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert text to hash')
    parser.add_argument('-t','--text',dest='text',required=True)
    parser.add_argument('-T','--Type',dest='type',required=True)
    args = parser.parse_args()

    txt = args.text
    hType = args.type
    main(txt,hType)






# text = 'behnam'
# ha = text.encode('utf_8')
# hasham = hashlib.md5(ha).hexdigest()
