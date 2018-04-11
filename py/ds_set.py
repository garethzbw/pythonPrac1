# coding = utf-8

set_x = {'a', 'b', 'c', 'z'}

set_y = {'b', 'c', 'd'}

print 'set_y.issuperset(set_x)', set_y.issuperset(set_x)
print 'set_y.issubset(set_x)', set_y.issubset(set_x)

set_y.add('a')

print set_y
print 'set_y.issuperset(set_x)', set_y.issuperset(set_x)

set_y_cpy = set_y.copy()

print 'set_y_cpy:', set_y_cpy

set_y.add('e')

print 'set_y:', set_y
print 'set_y_cpy:', set_y_cpy

print 'set_y.__xor__(set_x):', set_y^set_x

