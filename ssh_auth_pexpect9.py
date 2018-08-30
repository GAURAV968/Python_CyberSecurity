# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 22:37:57 2018

@author: bharg
"""

import pexpect
def send_command(child, cmd):
    prompt =[ "#", "\$",">>>",">" ]
    child.sendline(cmd)
    child.expect(prompt)
    print child.before

def connect(user,host,password):
    prompt =[ "#", "\$",">>>",">" ]
    ssh_newkey= "Are you sure you want to continue connecting"
    #This spawns a connection with ssh , user and host values using pexpect.spawn method
    connstr= "ssh "+user+"@"+host
    #spawn function is available only for Unix systems. For windows find similar method.
    
    child = pexpect.spawn(connstr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret==0:
        print " Error in connecting"
        return
    if ret ==1:
        child.sendline("yes")
    ret= child.expect([pexpect.TIMEOUT, '[P|p]assword'])
    if ret==0:
        print "Error in connecting"
        return
    if ret==1:
        child.sendline(password)
    child.expect(prompt)
    return child

def main():
    host = 'localhost'
    user = 'bharg'
    password = '9566208036'
    child = connect(user,host,password)
    send_command(child, 'cd C:\users\bharg\Desktop')


if __name__ == "__main__":
    main(   )

    
        