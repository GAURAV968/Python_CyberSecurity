# -*- coding: utf-8 -*-
"""
Created on Thu Aug 09 12:33:09 2018

@author: tiruvs
"""

import socket
import os
import struct
import binascii
def eth_hdr(data):
    ip_bool=False
    eth_hdr=struct.unpack("!6s6sH",data[:14])
    dmac=binascii.hexlify(eth_hdr[0])
    smac=binascii.hexlify(eth_hdr[1])
    proto= (eth_hdr[2])
    print "=====================Ethernet Header================================"
    print " Destination mac:\t %s:%s:%s:%s:%s:%s" %(dmac[0:2],dmac[2:4],dmac[4:6],dmac[6:8],dmac[8:10],dmac[10:12])
    print " Source mac: \t %s:%s:%s:%s:%s:%s" %(smac[0:2],smac[2:4],smac[4:6],smac[6:8],smac[8:10],smac[10:12])
    print " Protocol: \t \t %s"%hex(proto)
    if hex(proto)=="0x8000" : #ipv4
        ip_bool= True
    data=data[14:]
    return data,ip_bool
def ip_hdr(data):
    ip_hdr= struct.unpack("!6H4s4s",data[:20])
    ver = ip_hdr[0]>>12 #shift 12 bits the data is binary not decimal
    ihl= (ip_hdr[0]>>8) &0x0f # shif 8 bits and have to remove version so hence logical 
    tos= ip_hdr[0]&0x00ff 
    total_length = ip_hdr[1]
    ip_id=ip_hdr[2]
    flags = ip_hdr[3]>>13 # we require only the first 3 bits
    frag_offset = ip_hdr[3]&0x1fff
    ip_ttl = ip_hdr[4]>>8
    ip_proto= ip_hdr[4]&0x00ff
    ch_sum=ip_hdr[5]
    src_addr=socket.ntoa(ip_hdr[6])
    dest_addr=socket.ntoa(ip_hdr[7])
    no_frag = flags >>1
    more_frag = flags &0x1
    print "===========================IP Header=============================="
    print " Version \t %hu" %ver
    print " IHL \t %hu" %ihl
    print " TOS \t %hu" %tos
    print " Total Length \t %hu" %total_length
    print " ID \t %hu" %ip_id
    print " No Frag \t %hu" %no_frag
    print " More Frag \t %hu" %more_frag
    print " Fragment offset \t %hu" %frag_offset
    print " TTL \t %hu" %ip_ttl
    print " Next Proto \t %hu" %ip_proto
    print " CheckSum \t %hu" %ch_sum
    print " Source IP \t %s" %src_addr
    print " Destination IP \t %s" %dest_addr
    
    
    if ip_proto == 6: #TCP
        next_proto="TCP"
    elif ip_proto == 7: #UDP
        next_proto="UDP"
    else:
        next_proto = "OTHER"
    data=data[20:]
    return data,next_proto

def udp_header(data):
    udpheader = struct.unpack("!4H",data[:8])
    src_port = udpheader[0]
    dst_port = udpheader[1]
    length = udpheader[2]
    checksum = udpheader[3]
    print "=====================UDP Header============================="
    print "Source Port \t %hu"%src_port
    print "Destination Port \t %hu"%dst_port
    print "Length \t %hu"%length
    print "CheckSum \t %hu "%checksum
    data =data[8:]
    return data

def tcp_header(data):
    tcpheader =struct.unpack("!2H2I4H",data[:20])
    src_port =tcpheader[0]
    dest_port = tcpheader[1]
    seq_num = tcpheader[2]
    ack_number = tcpheader[3]
    data_offset = tcpheader[4]>>12
    reserved = (tcpheader[4]>>6) &0x03ff
    flags = tcpheader[4]&0x003f
    urg = flags&0x0020
    ack = flags&0x0010
    psh = flags&0x0008
    rst = flags&0x0004
    syn = flags&0x0002
    fin = flags&0x0001
    window = tcpheader[5]
    checksum = tcpheader[6]
    urg_ptr= tcpheader[7]
    print "======================TCP Header==================================="
    print " Source Port \t %hu"%src_port
    print " Destination Port \t %hu"%dest_port
    print " Sequence Number \t %hu"%seq_num
    print " Acknowledgement Number \t %hu"%ack_number
    print " Flags: "
    print "Urgent Flag %d"%urg
    print "Reserved Flag %d"%reserved
    print "Acknowledgement Flag %d"%ack
    print "PUSH Flag %d"%psh
    print "Reset Flag %d"%rst
    print "SYN Flag %d" %syn
    print "FIN Flag %d" %fin
    print "Window \t %hu"%window
    print " Checksum \t %hu"%checksum
    data=data[20:]
    return data
            
def main():
    eth=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
    data=eth.recv(2048)
    os.system("clear")
    data,ip_bool= eth_hdr(data)
    if ip_bool:
        data,next_proto = ip_hdr(data)
    else :
        return
    if next_proto == "TCP":
        data = tcp_header(data)
    elif next_proto == "UDP":
        data = udp_header(data)
    else:
        return


while (True):
    main()