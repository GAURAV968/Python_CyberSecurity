# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:59:58 2018

@author: bharg
"""
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("8.8.8.8", 443))
    ans = s.recv(1024)
    print ans
except Exception, e:
    print "Error = %s" %str(e)