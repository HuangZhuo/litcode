#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import *


# @lc code=start
class Solution:
    def minSubArrayLen_err(self, target: int, nums: List[int]) -> int:
        # 想当然借鉴 #11 的想法，不过没有分析推理的支持，答案也是错误的。
        n = sum(nums)
        if n < target:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                n -= nums[l]
                if n <= target: break
                l += 1
            else:
                n -= nums[r]
                if n <= target: break
                r -= 1
        return r - l


# @lc code=end

print(Solution().minSubArrayLen(4, [1, 4, 4]))
