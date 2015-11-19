#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,ftplib,socket
CONST_HOST = "202.85.213.22"
CONST_USERNAME = "lhtwwwroot"
CONST_PWD = "!@#$%^&*()123456789"
CONST_BUFFER_SIZE = 8192
def connect():
    try:
        ftp = ftplib.FTP(CONST_HOST)
        ftp.login(CONST_USERNAME,CONST_PWD)
        print ftp.getwelcome()
        return ftp
    except socket.error,socket.gaierror:
        print("FTP is unavailable,please check the host,username and password!")
        return False
        sys.exit(0)
    except ftplib.error_perm,e:
        print(e)
        return False
        sys.exit(0)
    except ftplib.error_reply,e:
        print(e)
        return False
        sys.exit(0)
    except ftplib.error_temp,e:
        print(e)
        return False
        sys.exit(0)
    except ftplib.error_proto,e:
        print(e)
        return False
        sys.exit(0)
def disconnect(ftp):
    ftp.quit()
def upload(ftp, filepath):
    f = open(filepath, "rb")
    file_name = os.path.split(filepath)[-1]
    try:
        ftp.cwd("/course/data")
        ftp.storbinary('STOR %s'%file_name, f, CONST_BUFFER_SIZE)
        #print ftp.size(file_name)
    except ftplib.error_perm:
        return False
    return True