# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:16:21 2018

@author: bharg
"""

import optparse
from pexpect import pxssh

class Client:
    def __init__(self,host,user,password):
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect()
    def connect(self):
        try:
            s=pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception,e:
                print str(e)
                print "Error connecting"
    def send_command(self,cmd):
       self.session.sendline(cmd)
       self.session.prompt()
       return self.session.before()


def botnet_command(cmd):
    for client in botnets:
        output=client.send_command(cmd)
        print "The output is %s" %output
botnets=[]
def add_client(host,user,password):
    client=Client(host,user,password)
    botnets.append(client)

add_client("192.168.134.26","root","netwitness")
add_client("192.168.134.46","firstwatch","netwitness")

botnet_command("ping 8.8.8.8")
botnet_command("")