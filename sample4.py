# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 12:32:55 2018

@author: bharg
"""

from sys import argv
import os
from os.path import exists
script_name, filename = argv
#if the file exist in the path
if not os.path.isfile(filename):
    print 'The file doesnot exist'
    exit(0)
print " The file exists = %s" %exists(filename)
#checking if the file has read access
print 'The file have read access = %s' %(os.access(filename, os.R_OK))
print 'Reading from the file'
f = open(filename, 'r')
content = f.read()
print content
#pinging google
os.system('ping 8.8.8.8')