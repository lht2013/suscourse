#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import MySQLdb
import config.dbcon
import hashlib
import math
import include.pagesupport as pagesupport
class Role:
    def role_list(self,page):
        total_results=config.dbcon.db.query("select count(rid) as total from sus_role")
        totaldata=total_results[0].total
        member_results=config.dbcon.db.query("select * from sus_role limit $start,$pagesize",vars={"start":pagesupport.PageSupport().startpage(page),"pagesize":pagesupport.PageSupport.pagesize})
        pagehtml=pagesupport.PageSupport().getpagehtml(page,totaldata)
        results= {"results_list":member_results, "pagehtml":pagehtml}
        return results
    def role_add(self,i):
        get_member=self.role_get(i.rolename)
        if get_member[0].total==0:
            result=config.dbcon.db.query("insert into sus_role(rolename,createtime,edittime) VALUES ($rolename,$createtime,$edittime)",
                                vars={'rolename':i.rolename,'createtime':i.createtime,'edittime':i.createtime})
        else:
            result=-1
        return result
    def role_get(self,rolename):
        result=config.dbcon.db.query("select COUNT(*) AS total  from sus_role where rolename=$rolename",vars={'rolename':rolename})
        return result

        return result
    def role_get_edit(self,id):
        results=config.dbcon.db.query("select * from sus_role where rid=$rid",vars={"rid":id})
        return results
    def role_set_edit(self,i):
        total_results=config.dbcon.db.query("select count(rid) as total from sus_role where rolename=$rolename",vars={"rolename":i.rolename})
        totaldata=total_results[0].total
        if totaldata==0:
            results=config.dbcon.db.query("update sus_role set rolename=$rolename  "
                                      "where rid=$rid",vars={"rolename":i.rolename,"rid":i.rid})
        else:
            results=-1
        return results