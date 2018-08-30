# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:49:12 2018

@author: bharg
"""

import ftplib

def ret_list(ftp):
    try:
        dirlist=ftp.nlst()
    except:
        print " No contents found on the target"
    contents=[]
    for filename in dirlist:
        fn=filename.lower()
        if ".php" in fn or ".htm" in fn or ".asp"in fn:
            print " Found a file with name %s"%(fn)
            contents.append(fn)
    return contents
def connect(hostname,username,password):
    ftp=ftplib.FTP(hostname)
    ftp.login(username,password)
    contents=ret_list(ftp)
    for content in contents:
        print content

connect("192.168.134.124","intern","S3cure!!")