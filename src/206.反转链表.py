#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
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
    def reverseList(self, head: ListNode) -> ListNode:
        rh, t = None, None  # rh-reverse_head, t-tmp

        while head:
            t = rh
            rh = head
            head = head.next
            rh.next = t
        return rh


# @lc code=end
