#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#

# 本质上，这是一道数学推理题目。


# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty:
            return True
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        # print(tx, ty)
        if tx == sx:
            return ty > sy and (ty - sy) % sx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % sy == 0
        else:
            return False

    def reachingPoints_bad(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def _bt(x, y):
            if x > tx or y > ty:
                return False
            elif x == tx and y == ty:
                return True
            return _bt(x + y, y) or _bt(x, x + y)

        return _bt(sx, sy)


# @lc code=end

print(Solution().reachingPoints(1, 1, 3, 5))
print(Solution().reachingPoints(2, 3, 8, 19))
print(Solution().reachingPoints(2, 3, 8, 20))
print(Solution().reachingPoints(10, 4, 10, 20))
