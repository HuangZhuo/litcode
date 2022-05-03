#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# 我的思路：
# 拿出来一个元素，剩下的问题就变成两数字之和了。并且只需要找拿出元素的后面的元素
# 语法：
# extend 返回值为空
# 难点：
# 去重是个麻烦

from typing import *


# @lc code=start
class Solution:
    def threeSum_err_duplicate(self, nums: List[int]) -> List[List[int]]:
        '''
        将问题转化成了twoSum，然而却无法去重
        '''
        n = len(nums)
        if n < 3:
            return []

        def twoSum(f, target):  # f-from
            ret, rec = [], {}
            for i in range(f + 1, n):
                v = nums[i]
                if v in rec:
                    ret.append([rec[v], i])
                else:
                    rec[target - v] = i
            # print(f,target,ret)
            return ret

        ret = []
        for i in range(n):
            for v in twoSum(i, -nums[i]):
                tmp = [nums[i]]
                tmp.extend([nums[i] for i in v])
                ret.append(tmp)
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 参考：https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ret = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target, l, r = -nums[i], i + 1, n - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    # 还需要继续寻找其它答案，比如[-5,1,2,3,4]
                    # 跳过重复元素
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l -= 1
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    r -= 1
        return ret


# @lc code=end

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
