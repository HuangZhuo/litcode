#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
from common import *
from collections import deque
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # o(n)
    def connect_on(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                node.next = None if i == (n - 1) else q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root  # cur-cur_level, 当前需要处理的链表
        while True:
            dummy = dummy_tail = Node()
            while cur:
                if cur.left:
                    dummy_tail.next = cur.left
                    dummy_tail = dummy_tail.next
                if cur.right:  #ERR 这里不要用错成elif
                    dummy_tail.next = cur.right
                    dummy_tail = dummy_tail.next
                cur = cur.next
            if not dummy.next:
                break
            else:
                cur = dummy.next
        return root


# @lc code=end

root = Node(1, Node(2), Node(3))
Solution().connect(root)