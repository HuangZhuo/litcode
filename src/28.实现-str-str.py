#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        if n == 0: return 0
        if m == 0: return -1

        # 1. cal next,needle is ptn
        next = [0] * n
        j, i = 0, 1
        while i < n:
            if needle[i] == needle[j]:
                next[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = next[j - 1]  # ERR
                else:
                    next[i] = 0
                    i += 1
        # print(next)

        # 2. match
        i, j = 0, 0
        while i < n and j < m:
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                if i != 0:
                    i = next[i - 1]  # 匹配到一半，找到下一个匹配点
                else:
                    j += 1  # 第一个字符就匹配失败

        return j - n if i == n else -1


# @lc code=end

print(Solution().strStr('abcde', 'de'))
