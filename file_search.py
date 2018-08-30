# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:52:49 2018

@author: bharg
"""
import re
import os
filename = raw_input("Enter the file name that you want to search for")
root,dirs,files= os.walk(os.getcwd())
pattern=re.compile(str(filename))
for i in files:
    if(re.search(pattern,i)):
        print " The file exists"
        print i