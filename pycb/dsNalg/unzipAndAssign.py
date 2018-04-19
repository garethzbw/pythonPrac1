# -*- coding: utf-8 -*-

# 解压序列复制给多个变量

p = (4, 5)
x, y = p
print(x, y)

data = ['bla', 1, 23, (2, 'd'), [32, 'eqw']]
name, quant, age, detail1, detail2 = data
print(name, quant, age, detail1, detail2)

# name, quant, age, detail1 = data  # 数目不符,异常

name, _, _, _, detail2 = data  # 抛弃掉不用的
print(name, detail2)


# 解压任何可迭代对象
# 使用带*号的变量表示一个列表来解压不定数量的元素

record = ['name', 23, 'painter', 'coder', 'singer']

name, age, *jobs = record
print("name: {}, age:{}, jobs:{}".format(name, age, jobs))


# 用*号来解压字符串
s = "gbale_23_188_80_PFA_RWF"
name, age, *body, league, pos = s.split('_')
print(name, age, body, league, pos)

