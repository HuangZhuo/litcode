#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#


# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        ret = False

        def _bt(x, y):
            if x > tx or y > ty:
                return False
            elif x == tx and y == ty:
                return True
            return _bt(x + y, y) or _bt(x, x + y)

        return _bt(sx, sy)


# @lc code=end

print(Solution().reachingPoints(1, 1, 3, 5))
