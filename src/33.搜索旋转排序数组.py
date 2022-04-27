#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from re import M
from typing import *


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                # 左侧有序 7,8,9|10,1,2,3
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 右侧有序 7,8,9,0,1|2,3,4
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


# @lc code=end
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8))
