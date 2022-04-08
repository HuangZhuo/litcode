#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。
#
# 示例 1：
#
# 输入：n = 1
# 输出：true
# 解释：2^0 = 1
#
# 进阶：你能够不使用循环/递归解决此问题吗？

# 2022-04-07
# 思路1: 将1不停左移位，直到【n】等于这个值
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        i = 0
        while i < 32:
            if n == 1 << i:
                return True
            i += 1
        return False

    def isPowerOfTwo_official(self, n: int) -> bool:
        # 妙啊
        return n > 0 and (n & (n - 1)) == 0


# @lc code=end

print(Solution().isPowerOfTwo(1))  # true
print(Solution().isPowerOfTwo(-2))  # false
print(Solution().isPowerOfTwo_official(3))  # false
print(Solution().isPowerOfTwo_official(4))  # true
