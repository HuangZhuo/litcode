#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
# 结束判断是否传染完毕？
# 法1：记录新鲜的数量和感染的数量（bad）
# 法2：最后一次遍历是否存在1
#

import collections
from typing import *


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        rot = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2]
        q = collections.deque(rot)
        m = 0  # m-minutes
        while q:
            roted = False
            for _ in range(len(q)):  # 层计数
                i, j = q.popleft()
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if ni < 0 or ni >= h or nj < 0 or nj >= w:
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        roted = True
                        q.append((ni, nj))
            if roted:
                m += 1
        if any(1 in r for r in grid):
            return -1
        return m


# @lc code=end
