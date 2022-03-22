#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
# 其实就是相当于自己写了个split
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        f, t, n = 0, 1, len(s)
        while (t < n):
            if (s[t] == ' '):
                ret.append(s[f:t][::-1])
                f = t + 1
            t += 1  # 总是要+1
        ret.append(s[f:][::-1])
        return ' '.join(ret)

    def reverseWords_pythonic(self, s: str) -> str:
        return ' '.join(w[::-1] for w in s.split(' '))


# @lc code=end

print(Solution().reverseWords('Hello World!'))
print(Solution().reverseWords_pythonic('Hello World!'))