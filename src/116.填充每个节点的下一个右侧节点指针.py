#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
# 思路：有点像广度优先遍历的样子
#
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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

from typing import *
from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            if not n:
                continue
            if not q:
                n.next = None
            else:
                n.next = q[0]
            if n.left:
                q.append(n.left)
                q.append(n.right)
        return root


# @lc code=end

#    1
#  2   3
# 4 5 6 7

# pre: 1,2,4,5,3,6,7
# mid: 4,2,5,1,6,3,7
# post:4,5,2,6,7,3,1

Solution().connect(Node(1, None, None))
