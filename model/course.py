#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import MySQLdb
import config.dbcon
import hashlib
import math
import time,datetime
import include.func as func
import include.pagesupport as pagesupport



class Course:
    def coursewlist(self, csid, ccid, page):
        if ccid == None and page == None:
            page = csid
            total_results = config.dbcon.db.query(
                "select count(a.csid) as total from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=1")
            totaldata = total_results[0].total
            lists = config.dbcon.db.query(
                "select a.* from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=1 limit $start,$pagesize",
                vars={"start": pagesupport.PageSupport().startpage(page), "pagesize": pagesupport.PageSupport.pagesize})
            results_list = []
            for i in lists:
                subone_results_list = config.dbcon.db.query("select username from sus_user  where uid=$uid",
                                                            vars={'uid': i.tid})
                i.setdefault('tusername', subone_results_list[0].username)
                subtwo_results_list = config.dbcon.db.query("select shiftname from sus_course_shift where csid=$csid",
                                                            vars={'csid': i.csid})
                # if subtwo_results_list>0:
                i.setdefault('shiftname', subtwo_results_list[0].shiftname)
                subthree_results_list = config.dbcon.db.query(
                    "select classesname from sus_course_class where ccid=$ccid", vars={'ccid': i.ccid})
                classname = subthree_results_list[0].classesname
                i.setdefault('classesname', classname)
                results_list.append(i)
        else:
            total_results = config.dbcon.db.query(
                "select count(a.csid) as total  from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=1 and a.csid=$csid and a.ccid=$ccid",
                vars={'csid': csid, 'ccid': ccid})
            totaldata = total_results[0].total
            lists = config.dbcon.db.query(
                "select a.* from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid WHERE b.shifttype=1 and a.csid=$csid and a.ccid=$ccid limit $start,$pagesize",
                vars={'csid': csid, 'ccid': ccid, "start": pagesupport.PageSupport().startpage(page),
                      "pagesize": pagesupport.PageSupport.pagesize})
            results_list = []
            for i in lists:
                subone_results_list = config.dbcon.db.query("select username from sus_user where uid=$uid",
                                                            vars={'uid': i.tid})
                i.setdefault('tusername', subone_results_list[0].username)
                subtwo_results_list = config.dbcon.db.query("select shiftname from sus_course_shift where csid=$csid",
                                                            vars={'csid': i.csid})
                i.setdefault('shiftname', subtwo_results_list[0].shiftname)
                subthree_results_list = config.dbcon.db.query(
                    "select classesname from sus_course_class where ccid=$ccid", vars={'ccid': i.ccid})
                i.setdefault('classesname', subthree_results_list[0].classesname)
                results_list.append(i)
        pagehtml = pagesupport.PageSupport().getpagehtml(page, totaldata)
        results = {"results_list": results_list, "pagehtml": pagehtml}
        return results

    def courseilist(self, csid, page):
        if page == None:
            page = csid
            total_results = config.dbcon.db.query(
                "select count(a.csid) as total from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=2")
            totaldata = total_results[0].total
            lists = config.dbcon.db.query(
                "select a.* from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=2 limit $start,$pagesize",
                vars={"start": pagesupport.PageSupport().startpage(page), "pagesize": pagesupport.PageSupport.pagesize})
            results_list = []
            for i in lists:
                subone_results_list = config.dbcon.db.query("select username from sus_user  where uid=$uid",
                                                            vars={'uid': i.tid})
                i.setdefault('tusername', subone_results_list[0].username)
                subtwo_results_list = config.dbcon.db.query("select shiftname from sus_course_shift where csid=$csid",
                                                            vars={'csid': i.csid})
                # if subtwo_results_list>0:
                i.setdefault('shiftname', subtwo_results_list[0].shiftname)
                results_list.append(i)
        else:
            total_results = config.dbcon.db.query(
                "select count(a.csid) as total  from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=2 and a.csid=$csid",
                vars={'csid': csid})
            totaldata = total_results[0].total
            lists = config.dbcon.db.query(
                "select a.* from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid WHERE b.shifttype=2 and a.csid=$csid  limit $start,$pagesize",
                vars={'csid': csid, "start": pagesupport.PageSupport().startpage(page),
                      "pagesize": pagesupport.PageSupport.pagesize})
            results_list = []
            for i in lists:
                subone_results_list = config.dbcon.db.query("select username from sus_user where uid=$uid",
                                                            vars={'uid': i.tid})
                i.setdefault('tusername', subone_results_list[0].username)
                subtwo_results_list = config.dbcon.db.query("select shiftname from sus_course_shift where csid=$csid",
                                                            vars={'csid': i.csid})
                i.setdefault('shiftname', subtwo_results_list[0].shiftname)
                results_list.append(i)
        pagehtml = pagesupport.PageSupport().getpagehtml(page, totaldata)
        results = {"results_list": results_list, "pagehtml": pagehtml}
        return results

    #未用
    def courselist(self,tid,page):

        if page==None:
            page=tid
            total_results = config.dbcon.db.query(
                "select count(cid) as total  from sus_course")
            totaldata = total_results[0].total
            lists = config.dbcon.db.query(
                "select * from sus_course limit $start,$pagesize",
                vars={"start": pagesupport.PageSupport().startpage(page),
                      "pagesize": pagesupport.PageSupport.pagesize})
            results_list = []
            for i in lists:
                results_list.append(i)


        else:
            total_results = config.dbcon.db.query(
                "select count(cid) as total  from sus_course where tid=$tid",
                vars={'tid': tid})
            totaldata = total_results[0].total
            print totaldata
            lists = config.dbcon.db.query(
                "select * from sus_course  where tid=$tid limit $start,$pagesize",
                vars={'tid': tid, "start": pagesupport.PageSupport().startpage(page),
                      "pagesize": pagesupport.PageSupport.pagesize})
            results_list = []
            for i in lists:
                results_list.append(i)
        pagehtml = pagesupport.PageSupport().getpagehtml(page, totaldata)
        results = {"results_list": results_list, "pagehtml": pagehtml}
        return results


    #老师课程列表
    def courseteacherlist(self,tid,page):
        if page==None:
            page=tid
            totalrst = config.dbcon.db.query(
                "SELECT count(cid) as total  FROM sus_course")
            total = totalrst[0].total
            totaldata=0
            results_list = []
            if total>0:
                total_results = config.dbcon.db.query(
                    "SELECT count(cid) as total  FROM sus_course group by coursetime")
                totaldata = total_results[0].total
                lists = config.dbcon.db.query(
                    "SELECT *  FROM sus_course  group by coursetime limit $start,$pagesize",
                    vars={"start": pagesupport.PageSupport().startpage(page),
                          "pagesize": pagesupport.PageSupport.pagesize})

                for i in lists:
                    #i.setdefault('sublist',config.dbcon.db.query("select * from sus_course where coursetime=$coursetime",vars={"coursetime":i.coursetime}))
                    sub_list=config.dbcon.db.query("select * from sus_course where coursetime=$coursetime",vars={"coursetime":i.coursetime})
                    i.setdefault('week',func.get_week_day(datetime.date.fromtimestamp(i.coursetime)))
                    sub_temp_list=[]
                    for j in sub_list:
                        sub_temp_list.append(j)
                    sub_temp_list_len= len(sub_temp_list)
                    tmp_dict={'intervaltime':''}
                    if sub_temp_list_len==1:
                        sub_temp_list.append( web.storage(tmp_dict))
                        sub_temp_list.append( web.storage(tmp_dict))
                    if sub_temp_list_len==2:
                        sub_temp_list.append( web.storage(tmp_dict))
                    i.setdefault('sublist',sub_temp_list)
                    results_list.append(i)

        else:

            totalrst = config.dbcon.db.query(
                "SELECT count(cid) as total  FROM sus_course")
            total = totalrst[0].total
            totaldata=0
            results_list = []
            if total>0:
                total_results = config.dbcon.db.query(
                    "SELECT count(cid) as total  FROM sus_course where tid=$tid group by coursetime",vars={"tid":tid})
                totaldata = total_results[0].total

                lists = config.dbcon.db.query(
                    "SELECT *  FROM sus_course  where tid=$tid  group by coursetime limit $start,$pagesize",
                    vars={"tid":tid,"start": pagesupport.PageSupport().startpage(page),
                          "pagesize": pagesupport.PageSupport.pagesize})

                for i in lists:
                    sub_list=config.dbcon.db.query("select * from sus_course where coursetime=$coursetime",vars={"coursetime":i.coursetime})
                    i.setdefault('week',func.get_week_day(datetime.date.fromtimestamp(i.coursetime)))
                    sub_temp_list=[]
                    for j in sub_list:
                        sub_temp_list.append(j)
                    sub_temp_list_len= len(sub_temp_list)
                    tmp_dict={'intervaltime':''}
                    if sub_temp_list_len==1:
                        sub_temp_list.append( web.storage(tmp_dict))
                        sub_temp_list.append( web.storage(tmp_dict))
                    if sub_temp_list_len==2:
                        sub_temp_list.append( web.storage(tmp_dict))
                    i.setdefault('sublist',sub_temp_list)
                    results_list.append(i)
        pagehtml = pagesupport.PageSupport().getpagehtml(page, totaldata)
        results = {"results_list": results_list, "pagehtml": pagehtml}
        return results


    def course_save_add(self, i):
        result_tid = config.dbcon.db.query(
            "select count(cid) as cidtotal from sus_course where tid=$tid and coursetime=$coursetime and intervaltime=$intervaltime",
            vars={"tid": i.tid, "coursetime": i.coursetime, "intervaltime": i.intervaltime})

        if result_tid[0].cidtotal == 0:
            if i.shifttype == "1":
                result = config.dbcon.db.query(
                    "insert into sus_course(coursename,tid,csid,ccid,coursetime,intervaltime,status,createtime,edittime) VALUES ($coursename,$tid,$csid,$ccid,$coursetime,$intervaltime,$status,$createtime,$edittime)",
                    vars={'coursename': i.coursename, 'tid': i.tid, 'csid': i.csid, 'ccid': i.ccid,
                          'coursetime': i.coursetime, 'intervaltime': i.intervaltime, "status": i.status,
                          'createtime': i.createtime, 'edittime': i.createtime})
            elif i.shifttype == "2":
                result = config.dbcon.db.query(
                    "insert into sus_course(coursename,tid,csid,ccid,coursetime,intervaltime,status,createtime,edittime) VALUES ($coursename,$tid,$csid,0,$coursetime,$intervaltime,$status,$createtime,$edittime)",
                    vars={'coursename': i.coursename, 'tid': i.tid, 'csid': i.csid, 'coursetime': i.coursetime,
                          'intervaltime': i.intervaltime, "status": i.status, 'createtime': i.createtime,
                          'edittime': i.createtime})
        else:
            result = -1
        return result


    def course_get_list(self, id):
        results = config.dbcon.db.query("select * from sus_course where cid=$id", vars={"id": id})
        return results


    def course_set_item(self, i):
        if i.shifttype == "1":
            result_tid = config.dbcon.db.query(
                "select count(cid) as cidtotal from sus_course where tid=$tid and coursetime=$coursetime and intervaltime=$intervaltime and cid<>$id",
                vars={"tid": i.tid, "coursetime": i.coursetime, "intervaltime": i.intervaltime, "id": i.cid})
            cidtotal=result_tid[0].cidtotal
            if cidtotal == 0:
                result = config.dbcon.db.query(
                    "update sus_course set coursename=$coursename,tid=$tid,csid=$csid,ccid=$ccid,coursetime=$coursetime,intervaltime=$intervaltime,status=$status,edittime=$edittime "
                    "where cid=$id", vars={"coursename": i.coursename, "tid": i.tid, "csid": i.csid, "ccid": i.ccid,
                                           "coursetime": i.coursetime, "intervaltime": i.intervaltime, "status": i.status,
                                           "edittime": i.edittime, "id": i.cid})
            else:
                result = -1
        elif i.shifttype == "2":
            result_tid = config.dbcon.db.query(
                "select count(cid) as cidtotal from sus_course where tid=$tid and coursetime=$coursetime and intervaltime=$intervaltime and cid<>$id",
                vars={"tid": i.tid, "coursetime": i.coursetime, "intervaltime": i.intervaltime, "id": i.cid})
            if result_tid[0].cidtotal == 0:
                result = config.dbcon.db.query(
                    "update sus_course set coursename=$coursename,tid=$tid,csid=$csid,coursetime=$coursetime,intervaltime=$intervaltime,status=$status,edittime=$edittime "
                    "where cid=$id",
                    vars={"coursename": i.coursename, "tid": i.tid, "csid": i.csid, "coursetime": i.coursetime,
                          "intervaltime": i.intervaltime, "status": i.status, "edittime": i.edittime, "id": i.cid})
            else:
                result = -1
        return result
    def course_del(self, idstr):
        result = config.dbcon.db.query("delete from sus_course where cid in (" + idstr + ")")
        return result
    def coursenopage(self,shifttype):
        #result = config.dbcon.db.query("select a.* from sus_course as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=$shifttype",vars={"shifttype": shifttype})
        lists = config.dbcon.db.query(
            "SELECT FROM_UNIXTIME(a.coursetime, '%Y-%m-%d') as coursetimeformat,a.coursetime,a.ccid,a.csid  FROM sus_course  as a LEFT JOIN  sus_course_shift as b on a.csid=b.csid where b.shifttype=$shifttype group by coursetime,ccid",vars={"shifttype": shifttype})
        results_list = []
        print lists
        for i in lists:
            sub_list=config.dbcon.db.query("select * from sus_course where coursetime=$coursetime and ccid=$ccid",vars={"coursetime":i.coursetime,"ccid":i.ccid})
            i.setdefault('week',func.get_week_day(datetime.date.fromtimestamp(i.coursetime)))
            sub_temp_list=[]
            for j in sub_list:
                del j['ccid'];
                del j['csid'];
                del j['createtime'];
                del j['edittime'];
                del j['coursetime'];
                del j['tid'];
                sub_temp_list.append(j)
            del i['coursetime'];
            i.setdefault('sublist',sub_temp_list)
            results_list.append(i)
        return results_list