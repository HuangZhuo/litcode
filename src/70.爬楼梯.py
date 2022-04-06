#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# NOTE: 要点是缓存计算结果，不然算不过来的..
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        rec = {
            1: 1,
            2: 2,
        }

        def _p(_n):
            if _n not in rec:
                rec[_n] = _p(_n - 1) + _p(_n - 2)
            return rec[_n]

        return _p(n)


# @lc code=end

print(Solution().climbStairs(3))
print(Solution().climbStairs(44))