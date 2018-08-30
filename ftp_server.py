# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 19:32:05 2018

@author: bharg
"""

import socket
socket.setdefaulttimeout(200)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.5', 21))
server.listen(1)
conn,addr = server.accept()
stri = conn.recv(1024)
print stri
conn.send("Got your string")
