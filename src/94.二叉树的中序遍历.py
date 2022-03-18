#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal_iter(root)

        ret = list()

        def traverse(node: TreeNode):
            if not node:  # fix: node.val->node
                return
            traverse(node.left)
            ret.append(node.val)
            traverse(node.right)

        traverse(root)
        return ret

    def inorderTraversal_iter(self, root: Optional[TreeNode]) -> List[int]:
        # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/204119
        stack, rst = [root], list()
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])  # 右边的元素先弹出处理
            elif isinstance(i, int):
                rst.append(i)
        return rst

    def inorderTraversal_iter_err1(self, root: Optional[TreeNode]) -> List[int]:
        ret = list()
        s = list([root])  # stack
        while (len(s) > 0):
            t = s.pop()
            if t.left:
                s.append(t.left)
            elif t.val:
                ret.append(t.val)
            elif t.right:
                s.append(t.right)

        return ret

    def inorderTraversal_array(self, root: Optional[TreeNode]) -> List[int]:
        r = len(root) - 1
        ret = list()

        def traverse(i):
            if i > r or None == root[i]:
                return
            traverse(2 * i + 1)
            ret.append(root[i])
            traverse(2 * i + 2)

        traverse(0)
        return ret


# @lc code=end

# print(Solution().inorderTraversal_array([]))
# print(Solution().inorderTraversal_array([1]))
# print(Solution().inorderTraversal_array([1, 2, 3]))

r_l = TreeNode(3)
r = TreeNode(2, r_l)
root = TreeNode(1, right=r)
print(Solution().inorderTraversal_iter(root))
