import os
import json

DEFAULT_SSL_PORT = 465


class EmailSMTPServer:

    host = ''
    user = ''
    pwd = ''
    port = DEFAULT_SSL_PORT

    @staticmethod
    def init(host, user, pwd, port=DEFAULT_SSL_PORT):
        EmailSMTPServer.user = user
        EmailSMTPServer.host = host
        EmailSMTPServer.pwd = pwd
        EmailSMTPServer.port = port

    @staticmethod
    def init(file_path):
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            try:
                with open(file_path, 'r') as f:
                    data = json.loads(f.read())
                    EmailSMTPServer.user = data['user']
                    EmailSMTPServer.host = data['host']
                    EmailSMTPServer.pwd = data['pwd']
                    if 'port' in data:
                        EmailSMTPServer.port = data['port']
                    else:
                        EmailSMTPServer.port = DEFAULT_SSL_PORT
            except Exception as e:
                print("打开文件错误!" + str(e))
