# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:36:05 2018

@author: bharg
"""
#tcp_Full_connect_scan
from threading import *
import optparse
import socket
screenLock = Semaphore(value=1)

def connScan(tip,port):
    try:
        #parameters are socket.AF_INET and socket.SOCK_STREAM
        conskt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #The connect method has 
        conskt.connect((tip,port))
        conskt.send("Violent Python\r\n")
        ans=conskt.recv(1024)
        screenLock.acquire()
        print "The target %s has port:%d open in it " %(tip,port)
        print " The response from the target for this particular port is %s" %(ans)
        
    except:
        screenLock.acquire()
        print " The target host %s has this port: %d closed" %(tip,port)
        return
    finally:
        screenLock.release()
        conskt.close()
        

        

def portScan(thost,tport):
    try:
        tip=socket.gethostbyname(thost)
    except:
        print " Cannot resolve the host name %s" %(thost)
        return
    #try:
     #   tname = socket.gethostbyaddr(tip)
      #  print " The name of the host translated from the IP %s" %tname
    #except:
      # print " Cannot resolve the IP address %s" %(tip)
       #return    
    socket.setdefaulttimeout(2)
    print tport
    for port in tport:
     print "Scanning the target %s for the port %s" %(tip, port)
     t= Thread(target=connScan, args= (tip, int(port)))
     t.start()
        


def main():
 parser=optparse.OptionParser("Usage: -H <HostName> -P <PortNumbers>")
 parser.add_option("-H", dest='thost', type='string', help ='Specify the target host')
 parser.add_option("-P", dest='tport', type='string', help= 'Specify the target port')
 (options,args)=parser.parse_args()

 if (options.thost==None)|(options.tport==None):
     print parser.usage
     exit(0)
 else:
      thost=options.thost
      tport=(options.tport.split(","))
      portScan(thost,tport)

if __name__ == "__main__":
 main()
 
 
