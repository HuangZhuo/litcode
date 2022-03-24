#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
# 没啥思路，直接看了题解视频，留了个印象
# 用递归的方式5min就写出来一次通过的答案了，可见递归也是侧重问题描述而非细节。
#
from typing import *


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)

        def _s(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return 0
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0 #避免重复访问&计数
                return 1 + _s(i - 1, j) + _s(i + 1, j) + _s(i, j + 1) + _s(i, j - 1)

        ret = 0
        for i in range(h):
            for j in range(w):
                ret = max(ret, _s(i, j))
        return ret


# @lc code=end
print(Solution().maxAreaOfIsland([[1, 1], [1, 1]]))
