#!/usr/bin/env python
# -*- coding: utf-8 -*-
import include.ftp as ftp
import os
import types
def upload(path):
    ftpc = ftp.connect()
    if type(ftpc) is types.InstanceType:
        fileupload = ftp.upload(ftpc, path)
        if fileupload == False:
            msg = '上传失败'
        else:
            msg = '上传成功'

    elif ftpc == False:
        msg = 'ftp连接失败'
    ftp.disconnect(ftpc)
    return msg
