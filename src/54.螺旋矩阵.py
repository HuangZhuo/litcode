#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

from typing import *


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ret


# @lc code=end
