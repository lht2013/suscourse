#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.role as role
import json
import time
import model.bases as bases
globals = {'time': time}
render = web.template.render('templates/')

class RoleList(bases.bases):
    def GET(self,page=None):
        results_list=role.Role().role_list(page)
        return render.rolelist(results_list,globals=globals)
    def POST(self):
        return
class RoleAdd(bases.bases):
    def GET(self):
        return render.roleadd()
    def POST(self):
        i = web.input()
        i.setdefault("createtime",time.time())
        flag=role.Role().role_add(i)
        if flag==1:
            msg="添加成功"
        else:
            msg="添加失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class RoleDel(bases.bases):
    def GET(self):
        return
    def POST(self):
        i = web.input()
        result=member.members().member_del(i.uidstr)
        if result>=1:
            flag=1
            msg="删除成功"
        else:
            flag=1
            msg="删除失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class RoleEdit(bases.bases):
    def GET(self,id=None):
        results=role.Role().role_get_edit(id)
        list=[]
        for v in results:
            list.append(v)
        return render.roleedit(list)
    def POST(self):
        i = web.input()
        i.setdefault("edittime",time.time())
        flag=role.Role().role_set_edit(i)
        print flag
        if flag==1:
            msg="修改成功"
        elif flag==-1:
            msg="用户名存在"
        else:
            msg="修改失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson