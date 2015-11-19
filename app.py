#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import config.url
import datetime
from include import log
web.config.debug = False
if __name__ == "__main__":
    app = web.application(config.url.urls, globals())
    web.config.session_parameters['cookie_name'] = '222'
    #web.config.session_parameters['cookie_domain'] = "/"

    nowtime = datetime.datetime.now()
    #nowtimesecond=nowtime.hour * 3600 + nowtime.minute * 60 + nowtime.second
    web.config.session_parameters['timeout'] = nowtime.second+38400 #24 * 60 * 60, # 24 hours   in seconds
    #web.config.session_parameters['ignore_expiry'] = False
    #web.config.session_parameters['ignore_change_ip'] = True
    #web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
    #web.config.session_parameters['expired_message'] = 'Session expired'
    #print web.config.session_parameters['timeout']
    #if web.config.get('_session') is None:
        #session = web.session.Session(app, web.session.DiskStore('sessions'), {'logind': 0})
        #web.config._session = session
    #else:
        #session = web.config._session
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'logind': 0})
    def session_hook():
        web.ctx.session = session
    app.add_processor(web.loadhook(session_hook))
    #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    #app.run(log.Log)
    app.run()