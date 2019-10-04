import email_bomber as email
from multiprocessing import Pool

def getEmails():
    with open("email_list.txt", "r") as emails:
        return emails.readlines()

def buildPoolList(s, p, sub, m, t):
    emails = getEmails()
    poolList = []
    for i in emails:
        tmpTup = (s, p, i, sub, m, t)
        poolList.append(tmpTup)
    return poolList

def main():
    sender = "SENDEREMAILHERE"
    passwd = "PASSWDHERE"
    subject = "SUBJECT"
    message = "MESSAGE"
    times = 1
    plargs = buildPoolList(sender, passwd, subject, message, times)
    pool = Pool(5)
    pool.starmap(email.sendMail, plargs)

if __name__ == "__main__":
    main()
