# -*- coding: utf-8 -*-
# 使用关键字而非位置来确定函数的参数

def function_keyword(a, b = 10, c = 20):
    print 'a is {}, b is {}, c is {}'.format(a, b, c)

def function_keyword2(a = 10):
    print 'a is', a

if __name__ == '__main__':
    function_keyword(10)
    function_keyword(1, 20)
    function_keyword(1, 20, 30)
    function_keyword(30, b=1)

    function_keyword2()