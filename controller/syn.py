#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import json
import demjson
import model.classes as classes
import model.shift as shift
import model.course as course
import model.bases as bases
# import include.ftp as ftp
import os
# import types
import include.up as up
render = web.template.render('templates/')
class SynMenu(bases.bases):
    def GET(self):
        return render.synmenu()
    def POST(self):
        shift_list = shift.Shift().shift_all_list(None)
        lists=[]
        for shifts in shift_list:
            classes_list=classes.Classes().classes_get_csid_list(shifts.csid)
            classesdict = {}
            classeslist=[]
            for classessub in classes_list:
                classesdict.setdefault('ccid',classessub.ccid)
                classesdict.setdefault('classesname',classessub.classesname)
                classeslist.append(classesdict)
                classesdict={}
            shifts.setdefault('classes',classeslist)
            shiftsdict = {}
            shiftsdict.setdefault('shiftyear',shifts.shiftyear)
            shiftsdict.setdefault('shiftname',shifts.shiftname)
            shiftsdict.setdefault('csid',shifts.csid)
            shiftsdict.setdefault('shifttype',shifts.shifttype)
            shiftsdict.setdefault('classes',shifts.classes)
            lists.append(shiftsdict)
        path='./static/json/menu.json'
        f=open(path,'w')
        f.write(demjson.encode(lists))
        f.close()
        fileexist=os.path.exists(path)
        flag=False
        if fileexist==True:
            msg=up.upload(path)
        else:
             msg='文件不存在，创建失败'
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class SynShift(bases.bases):
    def GET(self):
        return
    def POST(self):
        shift_list = shift.Shift().shift_all_list(1)
        lists=[]
        for shifts in shift_list:
            shiftsdict = {}
            shiftsdict.setdefault('shiftyear',shifts.shiftyear)
            shiftsdict.setdefault('shiftname',shifts.shiftname)
            shiftsdict.setdefault('csid',shifts.csid)
            shiftsdict.setdefault('shifttype',shifts.shifttype)
            shiftsdict.setdefault('classtime',shifts.classtime)
            shiftsdict.setdefault('classplace',shifts.classplace)
            shiftsdict.setdefault('teachermobile',shifts.teachermobile)
            shiftsdict.setdefault('teacher',shifts.username)
            shiftsdict.setdefault('busroute',shifts.busroute)
            shiftsdict.setdefault('createtime',shifts.createtime)
            lists.append(shiftsdict)
        path='./static/json/shift.json'
        f=open(path,'w')
        f.write(demjson.encode(lists))
        f.close()
        fileexist=os.path.exists(path)
        flag=False
        if fileexist==True:
            msg=up.upload(path)
        else:
             msg='文件不存在，创建失败'
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson


class SynWcourse(bases.bases):
    def GET(self):
        return
    def POST(self):
        lists=course.Course().coursenopage(1)
        path='./static/json/wcourse.json'
        f=open(path,'w')
        f.write(demjson.encode(lists))
        f.close()
        fileexist=os.path.exists(path)
        flag=False
        if fileexist==True:
            msg=up.upload(path)
        else:
             msg='文件不存在，创建失败'
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class SynIcourse(bases.bases):
    def GET(self):
        return
    def POST(self):
        lists=course.Course().coursenopage(2)
        path='./static/json/icourse.json'
        f=open(path,'w')
        f.write(demjson.encode(lists))
        f.close()
        fileexist=os.path.exists(path)
        flag=False
        if fileexist==True:
            msg=up.upload(path)
        else:
             msg='文件不存在，创建失败'
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class SynShiftYear(bases.bases):
    def GET(self):
        return
    def POST(self):
        lists=shift.Shift().shiftyear_all_list()
        path='./static/json/shiftyear.json'
        f=open(path,'w')
        f.write(demjson.encode(lists))
        f.close()
        fileexist=os.path.exists(path)
        flag=False
        if fileexist==True:
            msg=up.upload(path)
        else:
             msg='文件不存在，创建失败'
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class SynPublic(bases.bases):
    def GET(self):
        return render.synpublic()
    def POST(self):
        return