#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import MySQLdb
import config.dbcon
import hashlib
import math
import include.pagesupport as pagesupport
class members:
    def login(self, username, password):
        pwdhash = hashlib.md5(password).hexdigest()
        results = config.dbcon.db.query("SELECT * FROM sus_user as a,sus_role as b where username='%s' and userpwd='%s' and a.rid=b.rid" %(username, pwdhash))
        return results
    def memberlist(self,page):
        member_total_results=config.dbcon.db.query("select count(uid) as total_users from sus_user")
        totaldata=member_total_results[0].total_users
        member_results=config.dbcon.db.query("select * from sus_user limit $start,$pagesize",vars={"start":pagesupport.PageSupport().startpage(page),"pagesize":pagesupport.PageSupport.pagesize})
        results_list=[]
        for members in member_results:
            member_role_results=config.dbcon.db.query("select rolename from sus_role where rid=$rid",vars={'rid':members.rid})
            members.setdefault('rolename', member_role_results[0].rolename)
            results_list.append(members)
        pagehtml=pagesupport.PageSupport().getpagehtml(page,totaldata)
        results= {"results_list":results_list, "pagehtml":pagehtml}
        return results
    def member_add(self,i):
        get_member=self.member_get(i.username)
        if get_member[0].total_users==0:
            pwdhash = hashlib.md5(i.userpwd).hexdigest()
            result=config.dbcon.db.query("insert into sus_user(rid,username,userpwd,realname,email,qq,status,createtime,edittime) VALUES ($rid,$username,$userpwd,$realname,$email,$qq,$status,$createtime,$edittime)",
                                vars={'rid':i.role,'username':i.username,'userpwd':pwdhash,'realname':i.realname,'email':i.email,'qq':i.qq,'status':i.status,'createtime':i.createtime,'edittime':i.createtime})
        else:
            result=-1
        return result
    def role_list(self):
        role_restults=config.dbcon.db.query("select * from sus_role")
        return role_restults
    def member_get(self,username):
        result=config.dbcon.db.query("select COUNT(*) AS total_users  from sus_user where username=$username",vars={'username':username})
        return result
    def member_del(self,uidstr):
        result=config.dbcon.db.query("delete from sus_user where uid in ("+uidstr+")")
        return result
    def member_get_edit(self,id):
        results=config.dbcon.db.query("select * from sus_user where uid=$uid",vars={"uid":id})
        return results
    def member_set_edit(self,i):
        if i.userpwd==None:
            results=config.dbcon.db.query("update sus_user set rid=$rid,email=$email,qq=$qq,realname=$realname,status=$status  "
                                      "where uid=$uid",vars={"rid":i.role,"email":i.email,"qq":i.qq,"realname":i.realname,"status":i.status,"uid":i.uid})
        else:
            pwdhash = hashlib.md5(i.userpwd).hexdigest()
            results=config.dbcon.db.query("update sus_user set userpwd=$userpwd,rid=$rid,email=$email,qq=$qq,realname=$realname,status=$status  "
                                      "where uid=$uid",vars={"userpwd":pwdhash,"rid":i.role,"email":i.email,"qq":i.qq,"realname":i.realname,"status":i.status,"uid":i.uid})
        return results
    def member_get_teacher_list(self,rid):
        results=config.dbcon.db.query("select * from sus_user where rid=$rid",vars={"rid":rid})
        return results
    def member_set_pwd(self,i):
        pwdhash = hashlib.md5(i.userpwd).hexdigest()
        results=config.dbcon.db.query("update sus_user SET userpwd=$userpwd WHERE uid=$uid and username=$username",vars={"userpwd":pwdhash,"uid":i.uid,"username":i.username})
        return results