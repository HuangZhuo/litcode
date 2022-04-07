#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# NOTE: 这个问题和#70 差不多，一次提交通过。这类所谓动态规划，反而理解起来比较简单

from typing import *


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rec = {}

        def _cal(f):
            if f not in rec:
                if f == n - 1:
                    rec[f] = nums[f]
                elif f == n - 2:
                    rec[f] = max(nums[f], nums[f + 1])
                else:
                    rec[f] = max(nums[f] + _cal(f + 2), _cal(f + 1))
            return rec[f]

        return _cal(0)


# @lc code=end

print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))
