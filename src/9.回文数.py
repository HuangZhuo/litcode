#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
# 2022-03-18 遗漏了特殊条件判断：0
# v1使用了list，效率不好
# 最终答案和题解不能说差不多，只能说完全一致


# @lc code=start
class Solution:
    def isPalindrome_v1(self, x: int) -> bool:
        if x < 0:
            return False
        if x // 10 == 0:
            return True
        if x % 10 == 0:
            return False
        digits = list()
        while (x > 0):
            digits.append(x % 10)
            x = x // 10
        i, pivot = 0, len(digits) // 2
        while (i <= pivot):
            if digits[i] != digits[-i - 1]:
                return False
            i += 1
        return True

    def isPalindrome(self, x: int) -> bool:
        # NOTE: 可以直接用数字迭代就不要使用list，效率太低
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while (y < x):
            y = y * 10 + x % 10
            x = x // 10
        return x == y or x == y // 10


# @lc code=end
print(Solution().isPalindrome(0))
print(Solution().isPalindrome(1))
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(1213))
print(Solution().isPalindrome(1221))