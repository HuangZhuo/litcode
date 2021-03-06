#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
# 这个问题没看参考解出来了
# 思路一开始就是对的，而且是一次遍历，顺序找到第 N 个节点，此时将 target 指向 head。接着遍历，将 target 后移。
# 惭愧的是确实花了很多时间，而且解题过程中也十分依赖测试和调试。
#
# 官方题解
# 1. 遍历两次，第一次算出长度，第二次就知道是删除第 len-N 个节点
# 2. 使用栈，全部压到栈里面，再弹出 N 次（比较耗空间 O(L)）
# 3. 一次遍历，双指针
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ',' + str(self.next)


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node, pret, t = head, None, None  #t-target
        i = 1
        while (node):
            # print('>>', node.val)
            if i < n:
                i += 1
            elif t == None:
                t = head  # 这里是head，之前错误的整成node
                # print('++', 'init', t.val)
            else:
                pret = t
                t = t.next
                # print('++', 'move', t.val)
            node = node.next
        if pret:
            pret.next = t.next
            # del t
        else:
            pret = head
            # del pret
            head = head.next
        return head

    def removeNthFromEnd_official3(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        t, iter = dummy, head
        for i in range(n):
            iter = iter.next

        while (iter):
            iter = iter.next
            t = t.next

        t.next = t.next.next
        return dummy.next


# @lc code=end


def newList():
    n5 = ListNode(5, None)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    return n1


# h = Solution().removeNthFromEnd(newList(), 3)
# print(h)

h = Solution().removeNthFromEnd_official3(newList(), 5)
print(h)
