#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
# 看题：使用常量级额外空间
# 第一种：结合二分查找做。O(nlogn)
# 第二种：双指针法。看题解一下就明白了，简单推理后得到更简单的解法。O(n)
#

from typing import *


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while (i < j):
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum < target:
                i += 1
            elif sum > target:
                j -= 1


# @lc code=end
