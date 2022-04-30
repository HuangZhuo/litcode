#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# 2022-04-30
# 根据题目条件必然有一个峰值
# 思路：
# 画了个草图，如果当前不是峰值，那么在相邻的值更大的一边必然有峰值
# 提交失败：
# 没有考虑一个元素数组，而在Python里取负索引会变成引用倒数的元素。

from typing import *


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        f, t = 0, len(nums) - 1
        while f <= t:
            mid = (f + t) >> 1
            if mid == 0 or nums[mid] > nums[mid - 1]:
                if mid == t or nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    f = mid + 1
            else:
                t = mid - 1


# @lc code=end

print(Solution().findPeakElement([1]))
print(Solution().findPeakElement([1, 2]))
