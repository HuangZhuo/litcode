#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
# 一次性提交：
# - 208/208 cases passed (32 ms)
# - Your runtime beats 94.09 % of python3 submissions
# - Your memory usage beats 96.75 % of python3 submissions (14.8 MB)
#
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = t = ListNode()  # t-tail
        while list1 and list2:
            if list1.val < list2.val:
                t.next = list1
                list1 = list1.next
            else:
                t.next = list2
                list2 = list2.next
            t = t.next
        if not list1:
            t.next = list2
        elif not list2:
            t.next = list1
        return dummy.next


# @lc code=end
