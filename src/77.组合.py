#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# 跟#46 ~~异曲同工~~，不太对，这是一个组合问题，涉及到去重。
# 去重其实就是递增或者递减
from typing import *


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def _bt(_f, _li: list):  # f-from
            if len(_li) == k:
                ret.append([*_li])
                return
            # _li.append(_f)
            # for i in range(_f + 1, n + 1):
            #     _bt(i, _li)
            # _li.pop()

            for i in range(_f, n + 1):
                _li.append(i)
                _bt(i + 1, _li)
                _li.pop()

        _bt(1, [])
        return ret

    def combine_official(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        return combs

    def combine_err_range(self, n: int, k: int) -> List[List[int]]:
        # 我想把排列的思路直接拿过来，但是没有找到合适的去重办法！
        # 可以参考下这个题解：https://leetcode-cn.com/problems/combinations/solution/zu-he-by-leetcode-solution/1321146
        narr = [i for i in range(1, n + 1)]

        def _p(_e, _c):  # e-end_idx c-count
            if _c == 1:
                return [[narr[i]] for i in range(_e)]
            else:
                ret = []
                for i in range(_e):
                    narr[i], narr[_e - 1] = narr[_e - 1], narr[i]
                    for v in _p(_e - 1, _c - 1):
                        tmp = [narr[_e - 1]]
                        tmp.extend(v)
                        ret.append(tmp)
                    narr[_e - 1], narr[i] = narr[i], narr[_e - 1]
                return ret

        return _p(n, k)


# @lc code=end

print(Solution().combine(3, 1))
print(Solution().combine(3, 2))
