#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib

from email.mime.text import MIMEText

from tools.email.email_info import EmailInfo
from tools.email.email_smtp_server import EmailSMTPServer
from tools.my_log import MyLog


def send_email(email_info: EmailInfo):
    ret = False

    message = MIMEText(email_info.title, email_info.message_type, 'utf-8')

    message['From'] = email_info.sender.get_formataddr()
    message['To'] = email_info.receivers.get_formataddr()
    message['Subject'] = email_info.message

    try:
        server = smtplib.SMTP_SSL(EmailSMTPServer.host, EmailSMTPServer.port)
        server.login(EmailSMTPServer.user, EmailSMTPServer.pwd)
        server.sendmail(EmailSMTPServer.user, email_info.receivers.get_address_list(), message.as_string())
        server.quit()
        MyLog.logcat('发送成功')
        ret = True
    except smtplib.SMTPException as e:
        MyLog.logcat('Error,无法发送邮件! \n ' + str(e))

    return ret