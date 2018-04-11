# -*- coding: utf-8 -*-

# 切片-slicing

booklist = ['pythoncookbook', 'dive into python', 'thinking in java', 'alive', 'three kingdoms\' romance']

print 'booklist[::]:', booklist[::]
print 'booklist[0:len(booklist):]:', booklist[0:len(booklist):]
print 'booklist[0:len(booklist):2]', booklist[0:len(booklist):2]
print 'booklist[-1:-2:-1]', booklist[-1:-2:-1]
print 'booklist[::-1]', booklist[::-1]
print 'booklist[::-1]', booklist[0:len(booklist):-1]