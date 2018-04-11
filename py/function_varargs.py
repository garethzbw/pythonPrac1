# -*- coding: utf-8 -*-

# 可变参数

def function_varargs(a = 10, *var_tuple):
    print 'a = {}'.format(a)
    for i in var_tuple:
        print 'i =', i

if __name__ == '__main__':
    function_varargs([1, 2, 3, 4])