#!/usr/local/bin/python3
#coding: utf-8

from socket import AF_INET, SOCK_STREAM, socket , gethostbyname, gethostbyaddr, setdefaulttimeout
import optparse

#host = IP 
def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print("%d /tcp port open"% tgtPort)
        connskt.close()

    except:
        print("%d /tcp port closed"% tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    
    except:
        print("cannot resolve %s"% tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\n /scan result of %s"% tgtName[0])

    except:
        print("\n /scan result of %s"% tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("scanning port %d"% tgtPort)
        conScan(tgtHost, (tgtPort))

if __name__ == '__main__':
    portScan("google.com", [80, 22])
