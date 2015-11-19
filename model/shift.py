#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import MySQLdb
import config.dbcon
import hashlib
import math
import include.pagesupport as pagesupport
class Shift:
    def shiftlist(self,type,page):
        total_results=config.dbcon.db.query("select count(csid) as total  from sus_course_shift where shifttype=$shifttype",vars={'shifttype':type})
        totaldata=total_results[0].total

        member_results=config.dbcon.db.query("select * from sus_course_shift where shifttype=$shifttype limit $start,$pagesize",vars={'shifttype':type,"start":pagesupport.PageSupport().startpage(page),"pagesize":pagesupport.PageSupport.pagesize})
        results_list=[]
        #for members in member_results:
            #member_role_results=config.dbcon.db.query("select rolename from sus_role where rid=$rid",vars={'rid':members.rid})
            #members.setdefault('rolename', member_role_results[0].rolename)
            #results_list.append(members)
        pagehtml=pagesupport.PageSupport().getpagehtml(page,totaldata)
        results= {"results_list":member_results, "pagehtml":pagehtml}
        return results
    def shift_save_add(self,i):
        result=config.dbcon.db.query("insert into sus_course_shift(shiftyear,shiftname,shifttype,classtime,classplace,busroute,tid,teachermobile,status,createtime,edittime) "
                                     "VALUES ($shiftyear,$shiftname,$shifttype,$classtime,$classplace,$busroute,$tid,$teachermobile,$status,$createtime,$edittime)",
                                vars={'shiftyear':i.shiftyear,'shiftname':i.shiftname,'shifttype':i.shifttype,'classtime':i.classtime,
                                      'classplace':i.classplace,'busroute':i.busroute,'tid':i.tid,'teachermobile':i.teachermobile,'status':
                                    i.status,'createtime':i.createtime,'edittime':i.createtime})
        return result
    def shift_get_list(self,id):
        results=config.dbcon.db.query("select * from sus_course_shift where csid=$id",vars={"id":id})
        return results
    def shift_set_item(self,i):
        results=config.dbcon.db.query("update sus_course_shift set shiftyear=$shiftyear,shiftname=$shiftname,classtime=$classtime,classplace=$classplace,"
                                      "busroute=$busroute,tid=$tid,teachermobile=$teachermobile,status=$status,edittime=$edittime "
                                      "where csid=$id",vars={"shiftyear":i.shiftyear,"shiftname":i.shiftname,"classtime":i.classtime,"classplace":i.classplace,
                                                             "busroute":i.busroute,"tid":i.tid,"teachermobile":i.teachermobile,"status":i.status,"edittime":i.edittime,"id":i.csid})
        return results
    def shift_get_list(self,shifttype,status):
        results=config.dbcon.db.query("select * from sus_course_shift where shifttype=$shifttype and status=$status",vars={"shifttype":shifttype,"status":status})
        return results
    def shift_all_list(self,type):
        if type==None:
            results=config.dbcon.db.query("select a.*,b.username as username from sus_course_shift as a LEFT JOIN sus_user as b on a.tid=b.uid order by a.shifttype,a.shiftyear desc")
        else:
            results=config.dbcon.db.query("select a.*,b.username as username from sus_course_shift as a LEFT JOIN sus_user as b on a.tid=b.uid where a.shifttype=$shifttype",vars={"shifttype":type})
        return results
    def shift_get_item(self,id):
        results=config.dbcon.db.query("select * from sus_course_shift where csid=$csid",vars={"csid":id})
        return results
    def shift_del(self,cidstr):
        result=config.dbcon.db.query("delete from sus_course_shift where csid in ("+cidstr+")")
        return result
    def shiftyear_list(self,page):
        total_results=config.dbcon.db.query("select count(syid) as total from sus_shift_year")
        totaldata=total_results[0].total
        member_results=config.dbcon.db.query("select * from sus_shift_year limit $start,$pagesize",vars={"start":pagesupport.PageSupport().startpage(page),"pagesize":pagesupport.PageSupport.pagesize})
        pagehtml=pagesupport.PageSupport().getpagehtml(page,totaldata)
        results= {"results_list":member_results, "pagehtml":pagehtml}
        return results
    def shiftyear_add(self,i):
        get_total=self.shiftyear_get(i.shiftyear)
        get_flag_total=0
        if i.flag=="1":
            get_flag_total=self.shiftyear_flag_get(i.flag)[0].total
        if get_total[0].total==0 and get_flag_total==0:
            result=config.dbcon.db.query("insert into sus_shift_year(shiftyear,flag,createtime,edittime) VALUES ($shiftyear,$flag,$createtime,$edittime)",
                                vars={'shiftyear':i.shiftyear,'flag':i.flag,'createtime':i.createtime,'edittime':i.createtime})
        else:
            result=-1
        return result
    def shiftyear_get(self,shiftyear):
        result=config.dbcon.db.query("select COUNT(*) AS total  from sus_shift_year where shiftyear=$shiftyear",vars={'shiftyear':shiftyear})
        return result
    def shiftyear_flag_get(self,flag):
        result=config.dbcon.db.query("select COUNT(*) AS total  from sus_shift_year where flag=$flag",vars={'flag':flag})
        print flag
        return result
    def shiftyear_get_edit(self,id):
        results=config.dbcon.db.query("select * from sus_shift_year where syid=$syid",vars={"syid":id})
        return results
    def shiftyear_set_edit(self,i):
        total_results=config.dbcon.db.query("select count(syid) as total from sus_shift_year where flag=$flag and flag=1",vars={"flag":i.flag})
        totaldata=total_results[0].total
        if totaldata==0:
            results=config.dbcon.db.query("update sus_shift_year set flag=$flag where syid=$syid",vars={"flag":i.flag,"syid":i.syid})
        else:
            results=-1
        return results
    def shiftyear_all_list(self):
        results=config.dbcon.db.query("select syid,shiftyear,flag from sus_shift_year order by shiftyear desc")
        return results