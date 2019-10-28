class MyEmailException:
    message = ""
    code = 0

    def __init__(self, code, message=""):
        self.code = code
        if code in self.Error.EXCEPTION_MESSAGE:
            self.message = self.Error.EXCEPTION_MESSAGE[code]
        else:
            self.message = message

    class Error:
        EXCEPTION_MESSAGE = {}

        # <editor-fold desc="发送信息错误">
        # 发送信息错误 10000 + 100
        EXCEPTION_SENDER_EMPTY = 10000 + 110
        EXCEPTION_MESSAGE[EXCEPTION_SENDER_EMPTY] = '发送信息为空'

        EXCEPTION_SENDER_ADDRESS_MISS = EXCEPTION_SENDER_EMPTY + 1
        EXCEPTION_MESSAGE[EXCEPTION_SENDER_ADDRESS_MISS] = '发送邮箱为空'

        EXCEPTION_SENDER_ADDRESS_ERROR = EXCEPTION_SENDER_EMPTY + 2
        EXCEPTION_MESSAGE[EXCEPTION_SENDER_ADDRESS_ERROR] = '发送邮箱格式不对'
        # </editor-fold>

        # <editor-fold desc="接收信息错误">
        # 接收信息错误 10000 + 120
        EXCEPTION_RECEIVERS_EMPTY = 10000 + 120
        EXCEPTION_MESSAGE[EXCEPTION_RECEIVERS_EMPTY] = '接收信息为空'

        EXCEPTION_RECEIVERS_ADDRESS_MISS = EXCEPTION_SENDER_EMPTY + 1
        EXCEPTION_MESSAGE[EXCEPTION_RECEIVERS_ADDRESS_MISS] = '接收邮箱为空'

        EXCEPTION_RECEIVERS_ADDRESS_ERROR = EXCEPTION_SENDER_EMPTY + 2
        EXCEPTION_MESSAGE[EXCEPTION_RECEIVERS_ADDRESS_ERROR] = '接收邮箱格式不对'
        # </editor-fold>

        # <editor-fold desc="其他错误">
        # 其他错误 10000 + 140
        EXCEPTION_OTHER = 10000 + 140
        EXCEPTION_TITLE_EMPTY = EXCEPTION_OTHER + 1
        EXCEPTION_MESSAGE[EXCEPTION_TITLE_EMPTY] = '邮箱标题为空'

        EXCEPTION_MESSAGE_EMPTY = EXCEPTION_OTHER + 2
        EXCEPTION_MESSAGE[EXCEPTION_MESSAGE_EMPTY] = '邮箱内容为空'
        # </editor-fold>
