import unittest


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
