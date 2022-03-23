#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
# 2022-03-18 这个题目是+1，因此有一些规律可以用，可以用来精简算法
#

from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while (i > 0):
            if digits[i] > 9:
                digits[i] %= 10
                digits[i - 1] += 1
            else:
                # NOTE: 由于是+1，一旦没进位也就不需要进位了
                return digits
            i -= 1
        if digits[0] > 9:
            digits[0] = 0
            digits.insert(0, 1)
        return digits

    def plusOne_trick(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while (i >= 0):
            # trick: 进位方式
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
                i -= 1
            else:
                return digits
        # trick: 省略if
        digits[0] = 0
        digits.insert(0, 1)
        return digits


# @lc code=end

print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([9, 9]))

# with trick test
print(Solution().plusOne([0]))
