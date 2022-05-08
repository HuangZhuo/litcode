#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import *


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w, h = len(grid[0]), len(grid)

        def _s(i, j):
            if i < 0 or i >= h or j < 0 or j >= w:
                return
            elif grid[i][j] == '0':
                return 0
            else:
                grid[i][j] = '0'  # 重要：先标记为0，防止死循环
                _s(i - 1, j)
                _s(i + 1, j)
                _s(i, j - 1)
                _s(i, j + 1)
                return 1

        ret = 0
        # i行j列
        for i in range(h):
            for j in range(w):
                ret += _s(i, j)
        return ret


# @lc code=end
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid))
