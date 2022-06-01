#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
# 思路：有点像广度优先遍历的样子
#
from collections import deque
from typing import *

from common import *
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
    def connect_err(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            if not q:
                n.next = None
            else:
                # 这里有问题，会建立跨层的链接
                n.next = q[0]
            if n.left:
                q.append(n.left)
                q.append(n.right)
        return root


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                # 利用循环嵌套解决分层问题
                node = q.popleft()
                if i == n - 1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
        return root


# @lc code=end

#    1
#  2   3
# 4 5 6 7

# pre: 1,2,4,5,3,6,7
# mid: 4,2,5,1,6,3,7
# post:4,5,2,6,7,3,1

Solution().connect(Node(1, None, None))
