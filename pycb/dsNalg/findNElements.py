# -*- coding: utf-8 -*-
from collections import deque


# 保留最后N个元素
# 使用双端队列-deque 并且设置最大长度

def search(lines, pattern, history):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open("E:\\new 2.txt") as f:
        for line, prevlines in search(f, 'py', 3):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
