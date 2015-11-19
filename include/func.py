#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    return week_day_dict[day].decode('UTF-8')
def check_date(str):
    regs = re.compile(r'\d{4}-\d{2}-\d{2}$')
    match=re.match(regs,str)
    if match:
        flags=1
    else:
        flags=0
    return flags
