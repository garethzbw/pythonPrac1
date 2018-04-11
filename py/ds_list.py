# -*- coding: utf-8 -*-

def list_print(a):
    print 'print the list as a str:'
    print a

def list_print_iter(a):
    print 'print the list iterately:'
    for i in a:
        print i

def list_len(a):
    print 'the length of the list is:', len(a)

def list_sort(a):
    a.sort()
    print 'list after sort:', a

def list_append(a, *b):
    print 'add some more thins to list:', b
    for i in b:
        a.append(i)

    print 'list after appending:', a

def list_peak(a):
    print 'the first one in the list is:', a[0]

def list_pop(a):
    del a[0]
    print 'the first one in the list is:', a[0]

if __name__ == '__main__':
    a = [3, 2, 11, 13, 27, 9, 'b', '[', 100, u'龍']

    list_print(a)
    list_print_iter(a)
    list_len(a)
    list_sort(a)
    list_print(a)
    list_append(a, 77, 83, 99, 'optic', '_(:з」∠)_')
    list_peak(a)
    list_print(a)
    list_pop(a)
    list_print(a)




