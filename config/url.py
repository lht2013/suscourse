#!/usr/bin/env python
# -*- coding: utf-8 -*-
pre_fix = 'controller.'
urls = (
    '/login', pre_fix + 'member.login',
    '/loginout', pre_fix + 'member.loginOut',

    '/index', pre_fix + 'index.index',
    '/main', pre_fix + 'index.main',
    '/member/memberlist/(\d+)', pre_fix + 'member.memberlist',
    '/member/memberadd', pre_fix + 'member.MemberAdd',
    '/member/memberdel', pre_fix + 'member.MemberDel',
    '/member/memberedit/(\d+)', pre_fix + 'member.MemberEdit',
    '/member/memberedit', pre_fix + 'member.MemberEdit',

    '/member/memberpwd', pre_fix + 'member.MemberPWD',

    '/role/rolelist/(\d+)', pre_fix + 'role.RoleList',
    '/role/roleadd', pre_fix + 'role.RoleAdd',
    '/role/roledel', pre_fix + 'role.RoleDel',
    '/role/roleedit/(\d+)', pre_fix + 'role.RoleEdit',
    '/role/roleedit', pre_fix + 'role.RoleEdit',


    '/shift/shiftyearlist/(\d+)', pre_fix + 'shift.ShiftYearList',
    '/shift/shiftyearadd', pre_fix + 'shift.ShiftYearAdd',
    '/shift/shiftyearedit/(\d+)', pre_fix + 'shift.ShiftYearEdit',
    '/shift/shiftyearedit', pre_fix + 'shift.ShiftYearEdit',

    '/shift/shiftlist/(\d+)/(\d+)', pre_fix + 'shift.ShiftList',
    '/shift/shiftadd/(\d+)', pre_fix + 'shift.ShiftAdd',
    '/shift/shiftedit/(\d+)', pre_fix + 'shift.ShiftEdit',
    '/shift/shiftedit', pre_fix + 'shift.ShiftEdit',
    '/shift/shiftdel', pre_fix + 'shift.ShiftDel',

    '/classes/classeslist/(\d+)', pre_fix + 'classes.ClassesList',
    '/classes/classesadd', pre_fix + 'classes.ClassesAdd',
    '/classes/classesedit/(\d+)', pre_fix + 'classes.ClassesEdit',
    '/classes/classesedit', pre_fix + 'classes.ClassesEdit',
    '/classes/classesdel', pre_fix + 'classes.ClassesDel',

    '/course/courseallwlist', pre_fix + 'course.CourseAllWList',
    '/course/coursewlist/(\d+)/(\d+)/(\d+)', pre_fix + 'course.CourseWList',
    '/course/coursewlist/(\d+)', pre_fix + 'course.CourseWList',
    '/course/coursewadd', pre_fix + 'course.CourseWAdd',
    '/course/coursewedit/(\d+)', pre_fix + 'course.CourseWEdit',
    '/course/coursewedit', pre_fix + 'course.CourseWEdit',
    '/course/coursewdel', pre_fix + 'course.CourseDel',

    '/course/getclasses', pre_fix + 'course.GetClasses',

    '/course/courseallilist', pre_fix + 'course.CourseAllIList',
    '/course/courseilist/(\d+)/(\d+)', pre_fix + 'course.CourseIList',
    '/course/courseilist/(\d+)', pre_fix + 'course.CourseIList',
    '/course/courseiadd', pre_fix + 'course.CourseIAdd',
    '/course/courseiedit/(\d+)', pre_fix + 'course.CourseIEdit',
    '/course/courseiedit', pre_fix + 'course.CourseIEdit',
    '/course/courseidel', pre_fix + 'course.CourseDel',



    '/teacher/teacheralllist', pre_fix + 'teacher.TeacherAllList',
    '/course/coursetacherlist/(\d+)/(\d+)', pre_fix + 'course.CourseTeacherList',
    '/course/coursetacherlist/(\d+)', pre_fix + 'course.CourseTeacherList',


    '/syn/synmenu', pre_fix + 'syn.SynMenu',
    '/syn/synshift', pre_fix + 'syn.SynShift',


    '/syn/synwcourse', pre_fix + 'syn.SynWcourse',
    '/syn/synicourse', pre_fix + 'syn.SynIcourse',
    '/syn/synshiftyear', pre_fix + 'syn.SynShiftYear',




    '/syn/synpublic', pre_fix + 'syn.SynPublic',




)
