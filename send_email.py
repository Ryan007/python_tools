# -*- coding: UTF-8 -*-
import smtplib
import requests
import urllib,urllib2
from operator import itemgetter
from email.mime.text import MIMEText


mailto_list=["goodboyryan@126.com"] 
mail_host='smtp.exmail.qq.com'  #设置服务器
mail_user="noreply@dazizhu.cn"    #用户名
mail_pass="Noreply"   #口令 
mail_postfix="dazizhu.cn"  #发件箱的后缀


message = """ 
Subject: Hello Ryan 
%s
""" 


try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(mail_user+'@'+mail_postfix, mailto_list, message)         
	print "Successfully sent email"
except Exception,e:
	print str(e)    
	print "Error: unable to send email"
