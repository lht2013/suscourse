#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
MYSQL_SERVER = 'localhost'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'sus_cource'
db = web.database(dbn='mysql', db=MYSQL_DATABASE, user=MYSQL_USERNAME, pw=MYSQL_PASSWORD)
