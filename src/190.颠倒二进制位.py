#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret = (ret << 1) | (n & 1)  # ERR: 注意位运算优先级并加上括号
            n = n >> 1
        return ret

    def reverseBits_official2(self, n: int) -> int:
        '''
        官方有一种分治法实现，十分巧妙：https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode-solu-yhxz/859440
        '''
        raise NotImplementedError


# @lc code=end

print(Solution().reverseBits(43261596))