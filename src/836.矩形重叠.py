#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
# 这道题我确实没想到好办法，惭愧--
# 官方题解
# 方法1：一个矩形在另一个的上下左右
# 方法2：利用在x，y轴方向投影的线段是否重叠。关于方法2，我看评论还延申出一个 iou（交并比）的概念，有点意思。https://leetcode-cn.com/problems/rectangle-overlap/solution/ju-xing-zhong-die-by-leetcode-solution/292243

from typing import *


# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top


# @lc code=end
