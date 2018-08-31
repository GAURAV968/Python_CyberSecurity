#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:03:30 2018

@author: sat_system
"""
import speedtest
import os
import time
import syslog


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    # write to csv
    try:
     if os.stat('/home/sat_system/speedtest/speedtest.csv').st_size == 0:
         with open('/home/sat_system/speedtest/speedtest.csv', 'a+') as f:
           f.write('Date,Time,Download (Mbit/s),Upload (Mbit/s),Ping (ms)\n')
    except:
      pass
    with open('/home/sat_system/speedtest/speedtest.csv', 'a+') as f:
     #f.write('download,upload,ping\n')
      d, u, p = test()
      d=d/(1024*1024)
      u=u/(1024*1024)
      message = '{},{},{},{},{}\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'),d, u, p)
      f.write('{},{},{},{},{}\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'),d, u, p))
      syslog.syslog(message)
    # pretty write to txt file
    #with open('file.txt', 'w') as f:
     #   for i in range(3):
      #      print('Making test #{}'.format(i+1))
       #     d, u, p = test()
        #    f.write('Test #{}\n'.format(i+1))
         #   f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
          #  f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
           # f.write('Ping: {}\n'.format(p))
    # simply print in needed format if you want to use pipe-style: python script.py > file
    #for i in range(3):
    d, u, p = test()
       # print('Test #{}\n'.format(i+1))
    print('Download: {:.2f} Mb/s\n'.format(d /(1024*1024)))
    print('Upload: {:.2f} Mb/s\n'.format(u /(1024*1024)))
    print('Ping: {}\n'.format(p))
   

if __name__ == '__main__':
    main()

