#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.course as course
import model.shift as shift
import model.classes as classes
import model.member as member
import json
import demjson
import time
import include.func as func
import model.bases as bases
globals = {'time': time}
render = web.template.render('templates/')


class CourseWList(bases.bases):
    def GET(self, csid=None, ccid=None,  page=None):
        results_list = course.Course().coursewlist(csid, ccid,  page)

        return render.coursewlist(results_list, globals=globals)

    def POST(self):
        return

class CourseIList(bases.bases):
    def GET(self, csid=None,  page=None):
        results_list = course.Course().courseilist(csid,  page)
        return render.courseilist(results_list, globals=globals)
    def POST(self):
        return
class CourseWAdd(bases.bases):
    def GET(self):
        shift_list = shift.Shift().shift_get_list(1, 2)
        #classes_list = classes.Classes().classes_get_status_list()
        lists=[]
        for shifts in shift_list:
            lists.append(shifts)
        classes_list = classes.Classes().classes_get_list(lists[0].csid)
        teacher_list = member.members().member_get_teacher_list(4)
        return render.coursewadd(lists, classes_list, teacher_list)
    def POST(self):
        i = web.input()
        coursetime_check=func.check_date(i.coursetime)
        if i.coursename=="":
            flag=2
        if not coursetime_check:
            flag=2
        else:
            flag=3
        if flag == 2:
            msg="校验失败"
        else:
            i.coursetime = time.mktime(time.strptime(i.coursetime, '%Y-%m-%d'))
            i.setdefault("createtime", time.time())
            flag = course.Course().course_save_add(i)
            if flag == 1:
                msg = "添加成功"
            elif flag == -1:
                msg = "该老师在这个日期时间段内存在课程"
            else:
                msg = "添加失败"
        msgdict = {'success': flag, 'msg': msg}
        msgjson = json.dumps(msgdict, sort_keys=True)
        return msgjson
class CourseIAdd(bases.bases):
    def GET(self):
        shift_list = shift.Shift().shift_get_list(2, 2)
        teacher_list = member.members().member_get_teacher_list(4)
        return render.courseiadd(shift_list, teacher_list)
    def POST(self):
        i = web.input()
        coursetime_check=func.check_date(i.coursetime)
        if i.coursename=="":
            flag=2
        if not coursetime_check:
            flag=2
        else:
            flag=3
        if i.coursename=='' or i.csid=='':
            flag=2
        if flag == 2:
            msg="校验失败"
        else:
            i.coursetime = time.mktime(time.strptime(i.coursetime, '%Y-%m-%d'))
            i.setdefault("createtime", time.time())
            flag = course.Course().course_save_add(i)
            if flag == 1:
                msg = "添加成功"
            elif flag == -1:
                msg = "该老师在这个日期时间段内存在课程"
            else:
                msg = "添加失败"
        msgdict = {'success': flag, 'msg': msg}
        msgjson = json.dumps(msgdict, sort_keys=True)
        return msgjson
class CourseWEdit(bases.bases):
    def GET(self, id=None):
        shift_list = shift.Shift().shift_get_list(1,2)
        classes_list = classes.Classes().classes_get_status_list()
        teacher_list = member.members().member_get_teacher_list(4)
        results = course.Course().course_get_list(id)
        list = []
        for v in results:
            list.append(v)
        return render.coursewedit(list, shift_list, classes_list, teacher_list, globals)
    def POST(self):
        i = web.input()
        i.setdefault("edittime", time.time())
        i.coursetime = time.mktime(time.strptime(i.coursetime, '%Y-%m-%d'))
        flag = course.Course().course_set_item(i)
        if flag == 1:
            msg = "修改成功"
        elif flag == -1:
            msg = "该老师在这个日期时间段内存在课程"
        else:
            msg = "添加失败"
        msgdict = {'success': flag, 'msg': msg}
        msgjson = json.dumps(msgdict, sort_keys=True)
        return msgjson
class CourseIEdit(bases.bases):
    def GET(self, id=None):
        shift_list = shift.Shift().shift_get_list(2,2)
        teacher_list = member.members().member_get_teacher_list(4)
        results = course.Course().course_get_list(id)
        list = []
        for v in results:
            list.append(v)
        return render.courseiedit(list, shift_list, teacher_list, globals)
    def POST(self):
        i = web.input()
        i.setdefault("edittime", time.time())
        i.coursetime = time.mktime(time.strptime(i.coursetime, '%Y-%m-%d'))
        flag = course.Course().course_set_item(i)
        if flag == 1:
            msg = "修改成功"
        elif flag == -1:
            msg = "该老师在这个日期时间段内存在课程"
        else:
            msg = "添加失败"
        msgdict = {'success': flag, 'msg': msg}
        msgjson = json.dumps(msgdict, sort_keys=True)
        return msgjson


class CourseDel(bases.bases):
    def GET(self):
        return

    def POST(self):
        i = web.input()
        result = course.Course().course_del(i.idstr)
        if result >= 1:
            flag = 1
            msg = "删除成功"
        else:
            flag = 1
            msg = "删除失败"
        msgdict = {'success': flag, 'msg': msg}
        msgjson = json.dumps(msgdict, sort_keys=True)
        return msgjson


class CourseAllWList(bases.bases):
    def GET(self):
        classes_list = []
        shift_list = shift.Shift().shift_all_list(1)
        lists=[]
        for shifts in shift_list:
            shifts.setdefault('classes', classes.Classes().classes_get_csid_list(shifts.csid))
            lists.append(shifts)
        #classes_all_list = classes.Classes().classes_get_list()
        #for m in classes_all_list:
            #classes_list.append(m)
        return render.courseallwlist(lists)
class CourseAllIList(bases.bases):
    def GET(self):
        classes_list = []
        shift_list = shift.Shift().shift_all_list(2)
        classes_all_list = classes.Classes().classes_all_list()
        for m in classes_all_list:
            classes_list.append(m)
        return render.courseallilist(shift_list)

class CourseTeacherList(bases.bases):
    def GET(self, tid=None,  page=None):
        results_list = course.Course().courseteacherlist(tid,  page)
        return render.courseteacherlist(results_list, globals=globals)
    def POST(self):
        return
class GetClasses(bases.bases):
    def GET(self):
        return
    def POST(self):
        i = web.input()
        classes_list = classes.Classes().classes_get_csid_list(i.csid)
        return demjson.encode(classes_list)