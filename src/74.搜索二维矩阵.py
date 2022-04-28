#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# 2022-04-28 这道题初看是找到一维索引到二维索引的映射，终于搞一次一次性通过了，丢

from typing import *


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w, h = len(matrix[0]), len(matrix)
        f, t = 0, w * h - 1
        while f <= t:
            mid = (f + t) >> 1
            mi, mj = mid // w, mid % w
            if matrix[mi][mj] == target: return True
            elif matrix[mi][mj] < target: f = mid + 1
            else: t = mid - 1
        return False


# @lc code=end

print(Solution().searchMatrix([[1, 2], [3, 4]], 2))
print(Solution().searchMatrix([[1, 2], [3, 4]], 5))
