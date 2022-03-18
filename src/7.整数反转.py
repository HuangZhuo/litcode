#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
# 2022-03-18 审题啊！有符号数
# - 技巧点在于对负数取余的运算
# - 数字范围判断，现在的答案细节还是有问题的！有空看官方题解的证明。
#


# @lc code=start
class Solution:
    def reverse_v1(self, x: int) -> int:
        nega, max = False, (1 << 31) - 1
        if x < 0:
            nega = True
            x = -x
        ret = 0
        while (x != 0):
            ret = ret * 10 + x % 10
            if ret > max:
                return 0
            x = x // 10
        return -ret if nega else ret

    def reverse(self, x: int) -> int:
        MIN, MAX = -(1 << 31), (1 << 31) - 1
        ret = 0
        while (x != 0):
            digit = x % 10  # -123->7
            if x < 0 and digit > 0:
                digit -= 10  # 7->-3
            x = (x - digit) / 10  # (123- -3) / 10
            ret = ret * 10 + digit  # fix me: may be out of range!
            if ret < MIN or ret > MAX:
                return 0
        return int(ret)  # avoid 321.0


# @lc code=end

# print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(-2123456789))
