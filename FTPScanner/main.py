#!/usr/local/bin/python3
#coding: utf-8

import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous")

        print("\n " + str(hostname) + " FTP anonymous login succeded")
        ftp.quit()
        return True
    
    except Exception:
        print("\n " + str(hostname) + " FTP anonymous login failed")
        return False



if __name__ == '__main__':

    anonLogin("ip_goes_here")
