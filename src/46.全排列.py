#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
# 2022-03-28 没记错的话，简单的方式是递归处理。
# 这是一道难题，但是通过率却出奇高（78%），可见大部分都是抄答案，包括我。
# +2022-04-05 昨晚我想了一下，其实用递归方式解决也是很明显的：遍历从列表中取出一个元素，求**其余元素的全排列**，组合起来就是所有全排列。
#
from typing import *


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        ret = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            for v in self.permute(nums[1:]):
                tmp = [nums[0]]
                tmp.extend(v)
                ret.append(tmp)  # ERR: 这里不能append `mp.extend(v)` 的返回值
            nums[i], nums[0] = nums[0], nums[i]
        return ret


# @lc code=end

# print(Solution().permute([1]))
print(Solution().permute([1, 2]))
print(Solution().permute([1, 2, 3]))
