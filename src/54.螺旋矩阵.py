#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

from typing import *


# @lc code=start
class Solution:
    def spiralOrder_pythonic(self, matrix: List[List[int]]) -> List[int]:
        '''
        trick 解法
        通过python 的 unpack, zip 操作实现矩阵“旋转”，“弹出”一条边然后重复即可
        '''
        ret = []
        while matrix:
            ret += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ret

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        常规解法
        确定四个边界，按照顺时针遍历4条边，每遍历一条边，将边界进行压缩，直到所有元素遍历完毕
        '''
        if (len(matrix) == 0):
            return []
        left, top, right, botton = 0, 0, len(matrix[0]), len(matrix)
        ret = []
        n = right * botton
        while (n > 0):
            for i in range(left, right):
                ret.append(matrix[left][i])
                n -= 1
            top += 1
            for i in range(top, botton):
                ret.append(matrix[i][right - 1])
                n -= 1
            if n == 0:
                # trick: 只有往右和往下的时候，需要判断元素是否处理完毕。
                break
            right -= 1
            for i in range(right - 1, left - 1, -1):
                ret.append(matrix[botton - 1][i])
                n -= 1
            botton -= 1
            for i in range(botton - 1, top - 1, -1):
                ret.append(matrix[i][left])
                n -= 1
            left += 1
        return ret


# @lc code=end

print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# wrong cases:

# 01,02,03,04
# 05,06,07,08
# 09,10,11,12

# 7
# 9
# 6