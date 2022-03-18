#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
# 2022-03-18 之前做过，凭借印象一次性写出来了
#

from typing import List

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in rec:
                return rec[v], i
            else:
                rec[target - v] = i


# @lc code=end
