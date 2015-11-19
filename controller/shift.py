#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.shift as shift
import model.member as member
import json
import time
import model.bases as bases
globals = {'time': time}
render = web.template.render('templates/')
class ShiftList(bases.bases):
    def GET(self,type=None,page=None):

        results_list=shift.Shift().shiftlist(type,page)
        return render.shiftlist(results_list,type,globals=globals)
    def POST(self):
        return
class ShiftAdd(bases.bases):
    def GET(self,type=None):

        teacher_results=member.members().member_get_teacher_list(5)
        shiftyearlist=shift.Shift().shiftyear_all_list()
        return render.shiftadd(teacher_results,type,shiftyearlist)

    def POST(self,type=None):
        i = web.input()
        i.setdefault("createtime",time.time())
        flag=shift.Shift().shift_save_add(i)
        if flag==1:
            msg="添加成功"
        else:
            msg="添加失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class ShiftEdit(bases.bases):
        def GET(self,id=None):
            teacher_results=member.members().member_get_teacher_list(5)
            results=shift.Shift().shift_get_item(id)
            list=[]
            for v in results:
                list.append(v)
            shiftyearlist=shift.Shift().shiftyear_all_list()
            return render.shiftedit(list,teacher_results,shiftyearlist)
        def POST(self):
            i = web.input()
            i.setdefault("edittime",time.time())
            flag=shift.Shift().shift_set_item(i)
            if flag==1:
                msg="修改成功"
            else:
                msg="修改失败"
            msgdict = {'success':flag,'msg':msg}
            msgjson = json.dumps(msgdict,sort_keys=True)
            return msgjson
class ShiftDel(bases.bases):
    def GET(self):
        return
    def POST(self):
        i = web.input()
        result=shift.Shift().shift_del(i.idstr)
        if result>=1:
            flag=1
            msg="删除成功"
        else:
            flag=1
            msg="删除失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class ShiftYearList(bases.bases):
    def GET(self,page=None):
        results_list=shift.Shift().shiftyear_list(page)
        return render.shiftyearlist(results_list,globals=globals)
    def POST(self):
        return
class ShiftYearAdd(bases.bases):
    def GET(self):
        return render.shiftyearadd()
    def POST(self):
        i = web.input()
        i.setdefault("createtime",time.time())
        flag=shift.Shift().shiftyear_add(i)
        if flag==1:
            msg="添加成功"
        else:
            msg="添加失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class ShiftYearEdit(bases.bases):
    def GET(self,id=None):
        results=shift.Shift().shiftyear_get_edit(id)
        list=[]
        for v in results:
            list.append(v)
        return render.shiftyearedit(list)
    def POST(self):
        i = web.input()
        i.setdefault("edittime",time.time())
        flag=shift.Shift().shiftyear_set_edit(i)
        if flag==1:
            msg="修改成功"
        elif flag==-1:
            msg="只能有一个默认年份"
        else:
            msg="修改失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson