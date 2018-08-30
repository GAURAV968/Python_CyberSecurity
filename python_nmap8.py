# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:14:24 2018

@author: bharg
"""

import optparse
import nmap
import socket
def nmapScan(thost,tport):
    tip = socket.gethostbyname(thost)
    nscan=nmap.PortScanner()
    nscan.scan(tip,tport)
    state = nscan[tip]['tcp'][int(tport)]['state']
    print " Target host %s and Target port %d and State is %s" %(tip,int(tport),state)

#def portScan(thost, tport):
  #  tip=socket.gethostbyname(thost)
   # nmapScan(tip,tport)
def main():
    parser=optparse.OptionParser("Usage -H <HostName> -P <PortNumber>")
    parser.add_option("-H", dest='thost', type='string', help='Enter the Target address you wanna scan')
    parser.add_option("-P",dest ='tport', type = 'string', help='Enter the Target ports that you want to scan')
    (options, args)=parser.parse_args()
    if ((options.thost==None) | (options.tport==None)):
        print parser.usage
        exit(0)
    else:
        thost=options.thost
        tport=(options.tport.split(","))
        for port in tport:
            nmapScan(thost,port)

if __name__ == "__main__":
    main()
    