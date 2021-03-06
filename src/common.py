'''
1. 解题上下文环境依赖
2. 测试脚手架
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ',' + str(self.next)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def new_linklist(*args):
    h = iter = None
    for n in args:
        if not h:
            h = iter = ListNode(n)
        else:
            iter.next = ListNode(n)
            iter = iter.next
    return h