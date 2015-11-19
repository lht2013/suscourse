#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.member as member
import time
import model.bases as bases
globals = {'time': time}
render = web.template.render('templates/')

class TeacherAllList(bases.bases):
    def GET(self):
        teacher_list=member.members().member_get_teacher_list(4)
        return render.teacheralllist(teacher_list)
