#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 日志打印标准程序


class MyLog:

    isDebug = 0

    def __init__(self):
        self.__STATUS_DEBUG = 0
        self.__STATUS_RELEASE = 1

    @staticmethod
    def set_status(status):
        MyLog.isDebug = status

    @staticmethod
    def logcat(str):
        if MyLog.isDebug:
            print(str)

    @property
    def status_debug(self):
        return self.__STATUS_DEBUG

    @property
    def status_release(self):
        return self.__STATUS_DEBUG
