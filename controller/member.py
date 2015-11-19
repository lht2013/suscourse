#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.member as member
import model.bases as bases
import json
import time
globals = {'time': time}
render = web.template.render('templates/')
class login():
    def GET(self):
        #db = web.database(dbn='mysql', db='sus_erp', user='root',pw='123456')
        #results = db.query("SELECT COUNT(*) AS total_users FROM sus_user")
        #return results[0].total_users
        #x=  time.localtime(1317091800)
        #print globals["time"].strftime('%Y-%m-%d %H:%M:%S',globals["time"].localtime(1317091800))
        #print globals.time.strftime('%Y-%m-%d %H:%M:%S')
        #print globals["time"].strftime('%Y-%m-%d %H:%M:%S')
        return render.login()
    def POST(self):
        i = web.input()
        results=member.members().login(i.username,i.userpwd)
        flag=len(results)
        if flag==1:
            list_tmp=[]
            for i in results:
                list_tmp.append(i)
            msg='登录成功'
            web.ctx.session.logind=1
            web.ctx.session.username=list_tmp[0].username
            web.ctx.session.uid=list_tmp[0].uid
            web.ctx.session.rid=list_tmp[0].rid
            web.ctx.session.rolename=list_tmp[0].rolename
        else:
            msg='登录失败'
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        #web.header('Content-Type', 'application/json')
        return msgjson
class loginOut(bases.bases):
     def GET(self):
         return
     def POST(self):
         web.ctx.session.logind=None
         web.ctx.session.username=None
         msgdict = {'success':1,'msg':web.ctx.session.logind}
         msgjson = json.dumps(msgdict,sort_keys=True)
         return msgjson
class memberlist(bases.bases):
    def GET(self,page=None):
        results_list=member.members().memberlist(page)
        #print ', '.join(['%s:%s' % item for item in flag.__dict__.items()])
        #msgjson = json.dumps(msgdict,sort_keys=True)
        #print msgjson
        return render.memberlist(results_list,globals=globals)
    def POST(self):
        return
class MemberAdd(bases.bases):
    def GET(self):
        role_list=member.members().role_list()
        return render.memberadd(role_list)
    def POST(self):
        i = web.input()
        username=i.username
        userpwd=i.userpwd
        role=i.role
        email=i.email
        qq=i.qq
        realname=i.realname
        status=i.status
        i.setdefault("createtime",time.time())
        flag=member.members().member_add(i)
        if flag==1:
            msg="添加成功"
        else:
            msg="添加失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class MemberDel(bases.bases):
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
class MemberEdit(bases.bases):
    def GET(self,id=None):
        role_list=member.members().role_list()
        results=member.members().member_get_edit(id)
        list=[]
        for v in results:
            list.append(v)
        return render.memberedit(list,role_list)
    def POST(self):

        i = web.input()
        i.setdefault("edittime",time.time())
        flag=member.members().member_set_edit(i)
        if flag==1:
            msg="修改成功"
        else:
            msg="修改失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson
class MemberPWD(bases.bases):
    def GET(self):
        return render.memberpwd(web)
    def POST(self):
        i = web.input()
        flag=member.members().member_set_pwd(i)
        if flag==1:
            msg="修改成功"
        else:
            msg="修改失败"
        msgdict = {'success':flag,'msg':msg}
        msgjson = json.dumps(msgdict,sort_keys=True)
        return msgjson