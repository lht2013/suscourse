#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import config.dbcon
class PageSupport:
    pagesize=20
    def getpagehtml(self,page,totaldata):
        cur_url=str(web.ctx.path)#获取当前url
        cur_arr=cur_url.split('/')
        del cur_arr[len(cur_arr)-1]
        cur_url="/".join(cur_arr)+"/"
        totalpage=int((totaldata+self.pagesize-1)/self.pagesize)#总页数
        start_url=cur_url+"1"
        end_url=cur_url+str(totalpage)
        pagevalue=5#阀值
        page=int(page)
        if page<=1:
            pageheadhtml='<div class="page mt10"><div class="pagination"><ul><li class="first-child"><a href="'+start_url+'">首页</a></li><li class="disabled"><span>上一页</span></li>'
        else:
            pageheadhtml='<div class="page mt10"><div class="pagination"><ul><li class="first-child"><a href="'+start_url+'">首页</a></li><li><a href="'+str(page-1)+'">上一页</span></li>'
        if (page+1)<=totalpage:
            pagefoothtml='<li><a href="'+str(page+1)+'">下一页</a><li class="last-child"><a href="'+end_url+'">末页</a></li></ul></div></div>'
        else:
            pagefoothtml='<li class="disabled"><span>下一页</span><li class="last-child"><a href="'+end_url+'">末页</a></li></ul></div></div>'
        pagehtml=''
        if page<pagevalue:
            if totalpage==1:
                 pagehtml=pagehtml+'<li class="active"><span>1</span></li>'
            else:

                for num in range(1,totalpage+1):
                    if num==page:
                        pagehtml=pagehtml+'<li class="active"><span>'+str(num)+'</span></li>'
                    else:
                        pagehtml=pagehtml+'<li><a href="'+cur_url+str(num)+'">'+str(num)+'</a></li>'
        if page>=pagevalue:
            if page+3<=totalpage:
                for num in range(page-2,page+3):
                    if num==page:
                        pagehtml=pagehtml+'<li class="active"><span>'+str(num)+'</span></li>'
                    else:
                        pagehtml=pagehtml+'<li><a href="'+cur_url+str(num)+'">'+str(num)+'</a></li>'
            else:
                for num in range(page-2,totalpage+1):
                    if num==page:
                        pagehtml=pagehtml+'<li class="active"><span>'+str(num)+'</span></li>'
                    else:
                        pagehtml=pagehtml+'<li><a href="'+cur_url+str(num)+'">'+str(num)+'</a></li>'
        pagehtml=pageheadhtml+pagehtml+pagefoothtml
        return pagehtml
    def startpage(self,page):
        start=start=int(page)*int(self.pagesize)-int(self.pagesize)
        return start