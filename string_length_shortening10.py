# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:02:45 2018

@author: bharg
"""

def main():
    ostr=raw_input("Enter the original string")
    letter=raw_input("Enter the letter that you want remove")
    location =0
    length= len(ostr)
    while(location<length):
        if ostr[location] == letter:
            ostr= ostr[:location]+ostr[location+1:]
            length-=1
        location+=1
    print " The string after removal of the letter is %s" %(ostr)


if __name__=="__main__":
    main()
    