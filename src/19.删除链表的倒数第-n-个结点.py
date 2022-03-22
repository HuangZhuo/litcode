#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd_err(self, head: ListNode, n: int) -> ListNode:
        node, t = head, None  #target
        i = 1
        while (node):
            if i < n - 1:
                i += 1
            elif t == None:
                t = node
                node = t.next
            else:
                t = t.next
            node = node.next
        node = t.next
        t.next = node.next
        del node
        return head


# @lc code=end

n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
Solution().removeNthFromEnd(n1, 3)