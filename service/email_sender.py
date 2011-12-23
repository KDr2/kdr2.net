#!/usr/bin/python
#-*- coding: utf-8 -*-
# author : KDr2
#

import utils

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__all__ = ['sendmail', 'sendmail_text', 'sendmail_html']



def sendmail(to,subject,**mime):
    email_from = utils.get_config('email_from')

    msg = MIMEMultipart('alternative')
    msg.set_charset("utf-8")
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = to

    for t,c in mime.items():
        part = MIMEText(c, _subtype=t,_charset='utf-8')
        msg.attach(part)
        
    email_server = smtplib.SMTP(utils.get_config('email_server'))
    if "gmail" in utils.get_config('email_server').lower():
        email_server.starttls()
    email_server.login(utils.get_config('email_username'),utils.get_config('email_password'))
    email_server.sendmail(email_from, to, msg.as_string())
    email_server.quit()

def sendmail_text(to,subject,text):
    # part = MIMEText(text, 'plain')
    sendmail(to,subject,plain=text)

def sendmail_html(to,subject,html_doc):
    # part = MIMEText(html_doc, 'html')
    sendmail(to,subject,html=html_doc)

