import email_bomber as email
from multiprocessing import Pool
import argparse
import json

def getEmails(fileName):
    with open(fileName, "r") as emails:
        return emails.readlines()

def configParser(fileName):
    #Reads a json formated config
    with open(fileName, "r") as confFile:
        return json.loads(confFile.read())

def buildPoolList(fileName, s, p, sub, m, t):
    emails = getEmails(fileName)
    poolList = []
    for i in emails:
        tmpTup = (s, p, i, sub, m, t)
        poolList.append(tmpTup)
    return poolList

def main():
    parser= argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help="email file list")
    parser.add_argument("-c", "--config", type=str, help="config file")
    args = parser.parse_args()
    if not args.filename and not args.config:
        print("need args")
        exit()
    else:
        config = configParser(args.config)
        plargs = buildPoolList(args.filename, config["sender"], config["passwd"], config["subject"], config["message"], config["times"])
        pool = Pool(5)
        pool.starmap(email.sendMail, plargs)

if __name__ == "__main__":
    main()
