#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
# 解法一：开辟新数组
# 解法二：临时变量（涉及到数学推理，后面在研究）
# 解法三：来自编程珠玑（我该没记错吧）
#

from typing import *


# @lc code=start
class Solution:
    def rotate_math_err(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, m, n = 0, 0, len(nums)
        tmp = nums[0]
        while (m < n):
            i = (i + k) % n #err,这里麻烦之处在于计算下一位置
            nums[i], tmp = tmp, nums[i]  #swap
            m += 1

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(a, i, j):
            while (i < j):
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


# @lc code=end

# li = [1, 2, 3, 4, 5]
# Solution().rotate(li, 2)
# print(li)

# wrong cases
li = [-1, -100, 3, 99]
Solution().rotate(li, 2)
print(li)

# s1 [-1,-100,-1,99] tmp=3 i=2
# s2 [3,-100,-1,99] tmp=-1 i=0
# s3 [3,-100,-1,99] tmp=-1 i=2
# s3 [-1,-100,-1,99] tmp=3 i=0
# 如果是偶数有问题