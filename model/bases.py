#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import datetime
class bases:
    def __init__(self):
        #self.logger = web.ctx.environ['wsgilog.logger'] # 使用日志 #
        nowtime = datetime.datetime.now()
        web.config.session_parameters['timeout'] = nowtime.second+38400
        if web.ctx.session.logind!=1:
            raise web.seeother('/login')
			#raise web.redirect('http://202.85.213.24/login')
