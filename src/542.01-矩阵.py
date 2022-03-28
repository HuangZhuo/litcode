#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
# 看了题解：
# 技巧1：要反过来思考从0开始向周围搜索。
# 技巧2：将所有0加入已遍历列表
#
import collections
from typing import *


# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        w, h = len(mat[0]), len(mat)
        ret = [[0] * w for _ in range(h)]
        zp = [(i, j) for i in range(h) for j in range(w) if mat[i][j] == 0]
        q = collections.deque(zp)
        rec = set(zp)  # !所有的0直接加入已遍历列表
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (ni, nj) in rec:
                    continue
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                ret[ni][nj] = ret[i][j] + 1  # 源点正好是0
                rec.add((ni, nj))
                q.append((ni, nj))
        return ret


# @lc code=end

print(Solution().updateMatrix([[1, 1, 1], [1, 1, 0]]))
