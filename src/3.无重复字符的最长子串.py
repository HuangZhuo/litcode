#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring_bad(self, s: str) -> int:
        f, t, n = 0, 0, len(s)  # f-from,t-to
        rec = dict()
        m = 0  # m-max
        while (t < n):
            if (s[t] not in rec):
                rec[s[t]] = t
                t += 1
            else:
                m = max(m, t - f)
                f = rec[s[t]] + 1
                t = f  # 这种回退方式很dirty
                rec.clear()
        return max(m, t - f)

    def lengthOfLongestSubstring(self, s: str) -> int:
        f, t, n = 0, 0, len(s)  # f-from,t-to
        rec = set()
        m = 0  # m-max
        while (t < n):
            if (s[t] not in rec):
                rec.add(s[t])
            else:
                f += 1
            m = max(m, t - f)
            t += 1
        return m


# @lc code=end

print(Solution().lengthOfLongestSubstring('abcabcbb'))  # 3
print(Solution().lengthOfLongestSubstring('bbbbb'))  # 1

# wrong cases
print(Solution().lengthOfLongestSubstring(' '))  # 1
print(Solution().lengthOfLongestSubstring('aab'))  # 2
print(Solution().lengthOfLongestSubstring('dvdf'))  # 3
print(Solution().lengthOfLongestSubstring('abcabcbb'))  # 3

print(Solution().lengthOfLongestSubstring('pwwkew'))  # 3
