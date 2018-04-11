# -*- coding: utf-8 -*-

dict = {
    'jump' : 'naruto',
    'gintoki' : 'samurai',
    4 : 'arsenal'
}

print dict

print 'is dict contains \'jump\'?: ', dict.__contains__('jump')

print 'is dict has key \'jump\'?: ', dict.has_key('jump')

print 'jump has:', dict.get('jump')

print 'the size of the dict', dict.__sizeof__()

print 'dict\'s items:', dict.items()

print 'dict\'s keys:', dict.keys()

print 'dict\'s values:', dict.values()

print 'dict\'s iterator:', dict.iteritems()

dict.pop('gintoki')

print 'pop \'gintoki\', now the items are', dict
