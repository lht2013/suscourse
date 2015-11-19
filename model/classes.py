#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import MySQLdb
import config.dbcon
import hashlib
import math
import include.pagesupport as pagesupport
class Classes:
    def classeslist(self,page):
        total_results=config.dbcon.db.query("select count(ccid) as total  from sus_course_class")
        totaldata=total_results[0].total
        classes_results=config.dbcon.db.query("select * from sus_course_class limit $start,$pagesize",vars={"start":pagesupport.PageSupport().startpage(page),"pagesize":pagesupport.PageSupport.pagesize})
        results_list=[]
        for classes in classes_results:
            shift_results=config.dbcon.db.query("select shiftname from sus_course_shift where csid=$csid",vars={'csid':classes.csid})
            classes.setdefault('shiftname', shift_results[0].shiftname)
            results_list.append(classes)
        pagehtml=pagesupport.PageSupport().getpagehtml(page,totaldata)
        results= {"results_list":results_list, "pagehtml":pagehtml}
        return results
    def classes_save_add(self,i):
        result=config.dbcon.db.query("insert into sus_course_class(csid,classesname,status,createtime,edittime) VALUES ($csid,$classesname,$status,$createtime,$edittime)",
                                vars={'csid':i.csid,'classesname':i.classesname,"status":i.status,'createtime':i.createtime,'edittime':i.createtime})
        return result
    def classes_get_list(self,id):
        results=config.dbcon.db.query("select * from sus_course_class where ccid=$id",vars={"id":id})
        return results
    def classes_set_item(self,i):
        results=config.dbcon.db.query("update sus_course_class set csid=$csid,classesname=$classesname,status=$status,edittime=$edittime "
                                      "where ccid=$id",vars={"csid":i.csid,"classesname":i.classesname,"status":i.status,"edittime":i.edittime,"id":i.ccid})
        return results
    def classes_get_status_list(self):
        results=config.dbcon.db.query("select * from sus_course_class where status=1")
        return results
    def classes_all_list(self):
        results=config.dbcon.db.query("select * from sus_course_class where status=1")
        return results
    def classes_get_list(self,ccid):
        results=config.dbcon.db.query("select * from sus_course_class where ccid=$ccid and status=1",vars={"ccid":ccid})
        return results
    def classes_get_csid_list(self,csid):
        results=config.dbcon.db.query("select * from sus_course_class where csid=$csid and status=1",vars={"csid":csid})
        return results
    def classes_del(self,cidstr):
        result=config.dbcon.db.query("delete from sus_course_class where ccid in ("+cidstr+")")
        return result
    def classes_get_csid_list(self,csid):
        results=config.dbcon.db.query("select * from sus_course_class where csid=$csid and status=1",vars={"csid":csid})
        return results