#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
# 从应用上来说有点像画图工具中的油漆桶
#
from typing import *


# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        w, h = len(image[0]), len(image)
        bc = image[sr][sc]  # base color

        def _d(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return  # 边界
            if image[i][j] != bc or image[i][j] == newColor:
                return  # 不用刷or已经刷过了
            image[i][j] = newColor
            _d(i - 1, j)
            _d(i + 1, j)
            _d(i, j - 1)
            _d(i, j + 1)

        _d(sr, sc)
        return image


# @lc code=end
