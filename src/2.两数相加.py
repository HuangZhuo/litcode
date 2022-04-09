#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例 1：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#

# 我的想法：先处理合并，再处理进位，一次通过！

from common import ListNode
from common import new_linklist


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = tmp = ListNode()
        # 1. 处理合并
        while l1 or l2:
            if not l1:
                tmp.next = l2
                break
            elif not l2:
                tmp.next = l1
                break
            tmp.next = ListNode(l1.val + l2.val)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        # 2. 处理进位
        iter = h.next
        while iter:
            if iter.val >= 10:
                iter.val %= 10
                if iter.next:
                    iter.next.val += 1
                else:
                    iter.next = ListNode(1)
                    break
            iter = iter.next
        return h.next


# @lc code=end

l1 = new_linklist(9)
l2 = new_linklist(9, 9)
print(Solution().addTwoNumbers(l1, l2))
