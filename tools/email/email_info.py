import re
import os
from tools.email.my_email_exception import MyEmailException
from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.text import MIMEText

MESSAGE_TYPE_PLAIN = "plain"
MESSAGE_TYPE_HTML = "html"


class Email:
    def __init__(self, address, nick_name=""):
        self.address = address
        self.nick_name = nick_name

    address = ""
    nick_name = ""

    def get_formataddr(self):
        return formataddr((Header(self.nick_name, 'utf-8').encode(), self.address))


class Receivers:
    emails = []

    def get_formataddr(self):
        to_address = ""
        for item in self.emails:
            if len(to_address) > 0:
                to_address += ","
            to_address += item.get_formataddr()
        return to_address

    def get_address_list(self):
        address_list = []
        for item in self.emails:
            address_list.append(item.get_formataddr())
        return address_list


class EmailFile:
    file_path = ""

    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            raise MyEmailException(MyEmailException.Error.EXCEPTION_FILE_NOT_FOUNT, '文件地址:%s' % self.file_path)

    def get_attr(self):
        att = MIMEText(open(self.file_path, 'rb').read(), 'base64', 'utf-8')
        att['Content-Type'] = 'applivation/octet-stream'
        att['Content-Disposition'] = 'attachment; filename="%s"' % self.file_path.split("/")[-1]
        return att


class EmailInfo:
    # 发送邮箱信息 Email对象
    sender = None
    # 接收邮箱信息 Email数组
    receivers = None
    # 邮箱标题
    title = ""
    # 邮箱内容
    message = ""
    # 内容类型
    message_type = MESSAGE_TYPE_PLAIN
    # 附件地址
    files = []

    def __init__(self, sender: Email, receivers: Receivers, title, message
                 , files=[], message_type=MESSAGE_TYPE_PLAIN):
        self.sender = sender
        self.receivers = receivers
        self.title = title
        self.message = Header(message, 'utf-8')
        self.message_type = message_type
        email_files = []
        for item in files:
            email_files.append(EmailFile(item))
        self.files = email_files

    # 检查数据合法性
    def check_info(self) -> bool:
        # 空值检查
        if len(self.title) == 0:
            raise MyEmailException(MyEmailException.Error.EXCEPTION_TITLE_EMPTY)
        if len(self.message) == 0:
            raise MyEmailException(MyEmailException.Error.EXCEPTION_MESSAGE_EMPTY)
        self.check_sender()
        self.check_receivers()
        return True

    # 发送邮箱内容检查
    def check_sender(self):
        if self.sender is None:
            raise MyEmailException(MyEmailException.Error.EXCEPTION_SENDER_EMPTY)

        if 'address' not in self.sender:
            raise MyEmailException(MyEmailException.Error.EXCEPTION_SENDER_ADDRESS_MISS)
        else:
            address = self.sender.address
            emailRex = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
            if not re.match(emailRex, address):
                raise MyEmailException(MyEmailException.Error.EXCEPTION_SENDER_ADDRESS_ERROR)

    # 接收邮箱内容检查
    def check_receivers(self):
        if self.receivers is None:
            raise MyEmailException(MyEmailException.Error.EXCEPTION_RECEIVERS_EMPTY)

        for item in self.receivers.emails:

            if len(item.address) == 0:
                raise MyEmailException(MyEmailException.Error.EXCEPTION_SENDER_ADDRESS_MISS)
            else:
                address = item.address
                emailRex = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
                if not re.match(emailRex, address):
                    raise MyEmailException(MyEmailException.Error.EXCEPTION_RECEIVERS_ADDRESS_ERROR)
