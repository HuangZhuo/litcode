import unittest
from queue import Queue
from collections import deque


class TestCommon(unittest.TestCase):
    def test_sb(self):
        # https://www.w3school.com.cn/python/python_howto_reverse_string.asp
        l = [1, 2, 3]
        print(l[::-1])  # reverse,向后退步的切片

    def test_zip(self):
        m = [[1, 2, 3], [4, 5, 6]]
        print(*m)  # unpack
        z = zip(*m)  # zip
        print(list(z))

    def test_str(self):
        s = 'hw'
        print(s[1:])  #w
        print(s[1:2])  #w
        print(s[1:3])  #w

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