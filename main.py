import os
import sys
from tools.my_log import MyLog
from tools.email.email_smtp_server import *
from tools.email.email import send_email
from tools.email.email_info import *


def init_app():
    MyLog.set_status(MyLog.status_debug)
    EmailSMTPServer.init("server_info.json")


def start():
    os.system('cls')
    try:
        start_task()
    except Exception as e:
        print("Unexpected error:", e.with_traceback())


def start_task():

    sender = Email(EmailSMTPServer.user, '发送测试')

    receivers = Receivers()
    receivers.emails = [Email('xx@xx.com', '测试啦')]

    message = "这是测试内容"
    title = "这是测试标题"

    send_email(EmailInfo(sender, receivers, title, message, ['test1.txt', '2.txt']))


if __name__ == '__main__':
    init_app()
    start()
