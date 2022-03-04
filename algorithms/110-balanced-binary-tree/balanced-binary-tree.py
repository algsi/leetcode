"""
110. balanced binary tree

平衡二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        res = True

        def path(node: TreeNode) -> int:
            """
            Returns the height of the current node
            """
            if node is None:
                return 0
            left = path(node.left)
            right = path(node.right)
            if abs(left - right) > 1:
                nonlocal res
                res = False
            return max(left, right) + 1

        path(root)
        return res
