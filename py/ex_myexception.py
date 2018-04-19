# -*- coding: utf-8 -*-
# 自定义异常


class MyException(Exception):

    def __init__(self, name):
        Exception.__init__(self)
        self.name = name

try:
    name = input('type sth')
    if name == 'ex':
        raise MyException('intputed ex')
except MyException as ex:
    print 'exception name is {}'.format(ex.name)
except Exception as ex:
    print ex
else:
    print 'no exception'

