#-*- encoding: utf-8 -*-
import pylons

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__all__ = ['sendmail', 'sendmail_text', 'sendmail_html']



def sendmail(to,subject,**mime):
    if pylons.config.get("email_on","false") != "true":
        return
    email_from = pylons.config['email_from']
    msg = MIMEMultipart('alternative')
    msg.set_charset("utf-8")
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = to

    for t,c in mime.items():
        part = MIMEText(c, _subtype=t,_charset='utf-8')
        msg.attach(part)
    email_server_port=pylons.config.get("email_server_port","25")
    email_server = smtplib.SMTP(pylons.config['email_server'],int(email_server_port))
    if(pylons.config['email_server'] == "smtp.gmail.com"):
        email_server.starttls()
    email_server.login(pylons.config['email_username'],pylons.config['email_password'])
    email_server.sendmail(email_from, to, msg.as_string())
    email_server.quit()

def sendmail_text(to,subject,text):
    # part = MIMEText(text, 'plain')
    sendmail(to,subject,plain=text)

def sendmail_html(to,subject,html_doc):
    # part = MIMEText(html_doc, 'html')
    sendmail(to,subject,html=html_doc)

