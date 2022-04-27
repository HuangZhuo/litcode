#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchBoundL(f, t):
            while f <= t:
                mid = f + (t - f) // 2
                if nums[mid] == target:
                    if mid == f or nums[mid - 1] < target:
                        return mid
                    t = mid - 1
                elif nums[mid] < target:
                    f = mid + 1
                else:
                    t = mid - 1
            return -1

        def searchBoundR(f, t):
            # 找第一个大于target的
            while f <= t:
                mid = f + (t - f) // 2
                if nums[mid] == target:
                    if mid == t or nums[mid + 1] > target:
                        return mid
                    f = mid + 1
                elif nums[mid] < target:
                    f = mid + 1
                else:
                    t = mid - 1
            return -1

        l, r = 0, len(nums) - 1
        min_ = searchBoundL(l, r)
        if min_ < 0:
            return -1, -1
        else:
            return min_, searchBoundR(min_, r)


# @lc code=end

print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 7))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 10))
