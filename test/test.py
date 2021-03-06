import unittest
from collections import deque
from queue import Queue

from src.common import *


class TestBasic(unittest.TestCase):
    def test_sb(self):
        # https://www.w3school.com.cn/python/python_howto_reverse_string.asp
        l = [1, 2, 3]
        print(l[::-1])  # reverse,向后退步的切片

    def test_zip(self):
        m = [[1, 2, 3], [4, 5, 6]]
        print(*m)  # unpack -> [1, 2, 3] [4, 5, 6]
        z = zip(*m)  # zip
        print(list(z))  # [(1, 4), (2, 5), (3, 6)]

    def test_str(self):
        s = 'hw'
        print(s[1:])  #w
        print(s[1:2])  #w
        print(s[1:3])  #w
        print(s[:])  #hw

    def test_queue(self):
        q = Queue()
        q.put(1)
        q.put(2)
        print(q.get())
        print(q.get())
        print(q.empty())

    def test_deque(self):
        q = deque()
        q.append(1)
        q.append(2)
        print(q[0])  # 只有deque才有'peek'操作
        print(q.popleft())
        print(q.popleft())
        print(not q)

    def test_stack(self):
        a = []
        a.append(1)
        a.append(2)
        a.pop()
        print(a)

    def test_any(self):
        print(any([0, 0]))  # False
        print(any([0, 1]))  # True
        a = [[0, 0], [0, 1]]
        print([1 in r for r in a])  # [False, True], "1 in r" 是一个表达式返回布尔值
        print(any(1 in r for r in a))  # True

    def test_sum(self):
        print(sum([1, 2, 3]))  # 6
        # countif with generator
        print([1 if i == 1 else 0 for i in [1, 0, 1, 1, 1, 0]])  # "1 if i == 1 else 0" 是一个表达式返回1或0
        print(sum(1 if i == 1 else 0 for i in [1, 0, 1, 1, 1, 0]))


class TestCommon(unittest.TestCase):
    def test_linklist(self):
        n = new_linklist(1, 2, 3)
        print(n)
