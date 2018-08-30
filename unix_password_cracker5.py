# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:29:29 2018

@author: bharg
"""

import crypt
def testpass(cryPass):
 salt = cryPass[0:2]
 dictfile = open('dictionary.txt', 'r')
 for word in dictfile.readlines():
    word = word.strip("\n")
    cryptword = crypt.crypt(word,salt)
    if (cryptword == cryPass):
        print " The password is being cracked and it is %s" %(cryptword)
        return
    
 print " The password is not found"
 return


def main():
    passfile = open('passwords.txt', 'r')
    for line in passfile.readlines():
        if ':' in line:
            user = line.split(":")[0]
            cryPass = line.split(":")[1].strip(" ")
            print " Now the Password to be cracked is for : %s" %(user)
            testpass(cryPass)

if __name__ =='__main__':
    main()