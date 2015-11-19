#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import model.member as member
import model.bases as bases
render = web.template.render('templates/')

class index(bases.bases):
    def GET(self):
        #self.logger.info("request word pv")
        return render.index(web)
    def POST(self):
        return
class main(bases.bases):
    def GET(self):
        return render.main()
    def POST(self):
        return
