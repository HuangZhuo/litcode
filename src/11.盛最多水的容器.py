#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# 思路：移动左右端点，如果移动一边会导致水量的增加，那么移动这边，保存当前的最大值；如果都将导致减少，--那么同时所缩减两边，尝试找到更大值-- 留住较高的边
# 官方思路：直接留住较高的边即可
from typing import *


# @lc code=start
class Solution:
    def maxArea_mine(self, height: List[int]) -> int:
        def area(_l, _r):
            return (_r - _l) * min(height[_l], height[_r])

        l, r = 0, len(height) - 1
        max_ = area(l, r)
        while l < r:
            tmp = area(l + 1, r)
            if tmp > max_:
                max_ = tmp
                l += 1
                continue
            tmp = area(l, r - 1)
            if tmp > max_:
                max_ = tmp
                r -= 1
                continue
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_

    def maxArea(self, height: List[int]) -> int:
        # 官方题解
        l, r = 0, len(height) - 1
        ret = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            ret = max(ret, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ret


# @lc code=end
# print(Solution().maxArea_mine([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
# wrong cases
# print(Solution().maxArea_mine([1, 3, 2, 5, 25, 24, 5])) # 24

# offical cases
print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 3, 2, 5, 25, 24, 5]))
