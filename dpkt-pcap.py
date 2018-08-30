# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:37:37 2018

@author: bharg
"""

import socket
import dpkt

def printpcap(pcap):
    for (ts,buf) in pcap:
        try: 
            eth=dpkt.ethernet.Ethernet(buf)
            ip=eth.data
            src=socket.inet_ntoa(ip.src)
            dst=socket.inet_ntoa(ip.dst)
            print "Source IP: %s and Destination IP %s" %(src,dst)
        except:
            pass

def main():
    
    f = open("C:\\Users\\bharg\Desktop\\sample.pcap",'rb')  
    pcap = dpkt.pcap.Reader(f)
    printpcap(pcap)
    

if __name__=="__main__":
    main()