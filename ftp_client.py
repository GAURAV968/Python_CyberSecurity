# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 19:32:15 2018

@author: bharg
"""

import socket
socket.setdefaulttimeout(200)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.5', 21))
client.send("Watha dei")
print client.recv(1024)
