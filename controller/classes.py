#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.classes as classes
import model.shift as shift
import json
import time
import model.bases as bases
globals = {'time': time}
render = web.template.render('templates/')
class ClassesList:
    def GET(self,page=None):
        results_list=classes.Classes().classeslist(page)
        return render.classeslist(results_list,globals=globals)
    def POST(self):
        return
class ClassesAdd:
    def GET(self):
        shift_list=shift.Shift().shift_all_list(1)
        return render.classesadd(shift_list)
    def POST(self):
        i = web.input()
        i.setdefault("createtime",time.time())
        flag=classes.Classes().classes_save_add(i)
        if flag==1:
            msg="添加成功"
        else:
            msg="添加失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class ClassesEdit:
        def GET(self,id=None):
            shift_list=shift.Shift().shift_all_list(1)
            results=classes.Classes().classes_get_list(id)
            print id
            list=[]
            for v in results:
                list.append(v)
            print list
            return render.classesedit(list,shift_list)
        def POST(self):
            i = web.input()
            i.setdefault("edittime",time.time())
            flag=classes.Classes().classes_set_item(i)
            if flag==1:
                msg="修改成功"
            else:
                msg="修改失败"
            msgdict = {'success':flag,'msg':msg}
            msgjson = json.dumps(msgdict,sort_keys=True)
            return msgjson
class ClassesDel(bases.bases):
    def GET(self):
        return
    def POST(self):
        i = web.input()
        result=classes.Classes().classes_del(i.idstr)
        if result>=1:
            flag=1
            msg="删除成功"
        else:
            flag=1
            msg="删除失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson