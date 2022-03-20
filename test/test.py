import unittest


class TestCommon(unittest.TestCase):
    def test_sb(self):
        l = [1, 2, 3]
        print(l[::-1])  # reverse

    def test_zip(self):
        m = [[1, 2, 3], [4, 5, 6]]
        print(*m)  # unpack
        z = zip(*m)  # zip
        print(list(z))
