#!/usr/local/bin/python3
#coding: utf-8

import os
import optparse
from winreg import *

def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows_NT\CurrentVerision\ProfileList" + "\\" + sid)
        (value, type) = QueryValueEX(key, "ProfileImaagePath")
        user = value.split ("\\") [-1]
        return user
    except:
        return sid

def returnDir():
    dirs=["C:\\Recycler\\","C:\\Recycled\\","C:\\$Recycle.Bin\\"]
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print("\n files for user: " + str(user))
        for file in files:
            print("\n found files: " + str(file))

def main():
    recycledDir = returnDir()
    findRecycled(recycledDir)


if __name__ == '__main__':
    main()