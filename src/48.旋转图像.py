#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from typing import *


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        width = len(matrix)
        for line in matrix:
            i, j = 0, width - 1
            while i < j:
                line[i], line[j] = line[j], line[i]
                i += 1
                j -= 1

        # (0,0)<->(-1,-1); (0,1)<->(-2,-1)
        # 这个循环的边界还是有点巧妙的！
        for i in range(width - 1):
            for j in range(width - i):
                matrix[i][j], matrix[-j - 1][-i - 1] = matrix[-j - 1][-i - 1], matrix[i][j]

        return matrix


# @lc code=end

print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
