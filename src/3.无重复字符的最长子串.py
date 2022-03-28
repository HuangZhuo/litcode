#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
# 这道题官方的解法比较一般，感觉也不是其所说的时间复杂度O(n)
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

    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        f, t, n = 0, 0, len(s)  # f-from,t-to
        rec = set()
        m = 0  # m-max
        while (t < n):
            if (s[t] not in rec):
                rec.add(s[t])
            else:
                #case: abcdc
                while (s[f] != s[t]):
                    rec.remove(s[f])
                    f += 1
                f += 1
            m = max(m, t - f + 1)
            t += 1
        return m

    def lengthOfLongestSubstring_official(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

    def lengthOfLongestSubstring_user_captaintec(self, s: str) -> int:
        # https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/376956
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        受到 captaintec 启发使用字典后改进的算法
        '''
        f, t, n = 0, 0, len(s)  # f-from,t-to
        rec = {}
        m = 0  # m-max
        while (t < n):
            if (s[t] not in rec):
                rec[s[t]] = t
            else:
                #case: abcdcef,abba
                f = max(f, rec[s[t]] + 1)  # f不能回溯
                rec[s[t]] = t
            m = max(m, t - f + 1)
            t += 1
        return m


# @lc code=end

print(Solution().lengthOfLongestSubstring_official('abba'))  # 2

# base cases
print(Solution().lengthOfLongestSubstring('abcabcbb'))  # 3
print(Solution().lengthOfLongestSubstring('bbbbb'))  # 1

# wrong cases
print(Solution().lengthOfLongestSubstring(' '))  # 1
print(Solution().lengthOfLongestSubstring('aab'))  # 2
print(Solution().lengthOfLongestSubstring('dvdf'))  # 3
print(Solution().lengthOfLongestSubstring('abcabcbb'))  # 3

print(Solution().lengthOfLongestSubstring('pwwkew'))  # 3

print(Solution().lengthOfLongestSubstring('abba'))  # 2
