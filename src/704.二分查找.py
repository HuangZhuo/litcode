#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import *


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while (i <= j):
            x = (i + j) // 2
            if nums[x] == target:
                return x
            elif nums[x] > target:
                j = x - 1
            else:
                i = x + 1
        return -1


# @lc code=end

print(Solution().search([1], 1))
print(Solution().search([1, 2], 1))
