#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
import math
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

    def minSubArrayLen_mine(self, target: int, nums: List[int]) -> int:
        n = len(nums) - 1
        l = 0
        r = -1
        s = 0  #s-sum
        ret = 0
        while s < target and r < n:
            r += 1
            s += nums[r]
            while s >= target:
                _ret = r - l + 1
                ret = _ret if ret == 0 else min(_ret, ret)
                # 左指针右移
                s -= nums[l]
                l += 1
        return ret

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 官方题解
        n = len(nums)
        ret = n + 1  # 设置答案为不可能的一个值
        l = r = 0
        s = 0
        while r < n:
            s += nums[r]
            while s >= target:
                ret = min(ret, r - l + 1)
                s -= nums[l]
                l += 1
            r += 1
        return 0 if ret == (n + 1) else ret


# @lc code=end

print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  #2
print(Solution().minSubArrayLen(4, [1, 4, 4]))  #1
print(Solution().minSubArrayLen(6, [10, 2, 3]))  #1
