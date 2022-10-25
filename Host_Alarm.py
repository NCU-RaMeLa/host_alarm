# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:58:48 2021

@author: zih
"""

import configparser
import winsound
import socket
from time import sleep
from datetime import datetime

def isOpen(ip,port,timeout):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       s.settimeout(timeout)
       s.connect((ip, int(port)))
       s.shutdown(2)
       return True
   except:
       return False

c = 0
tt = 0

while True:
    print(datetime.now())
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    hostname = config['common']['hostname']
    port = int(config['common']['port'])
    count = int(config['common']['count'])
    interval = int(config['common']['interval'])
    timeout = int(config['common']['timeout'])
    frequency = int(config['alarm']['frequency'])
    duration = int(config['alarm']['duration'])

    if isOpen(hostname,port,timeout):
        c = 0
        print(c,hostname+":"+str(port)+" is alive")
    else:
        c += 1
        print(hostname+":"+str(port)+" faile. count:",c)
    if c >= count:
        while tt <= interval:
            winsound.Beep(frequency, duration)
            tt+=duration
        tt = 0
    else:
        sleep(interval)