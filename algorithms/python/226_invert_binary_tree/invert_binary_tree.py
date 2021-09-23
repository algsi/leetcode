"""
226. invert binary tree

翻转二叉树
"""


class TreeNode:
    def __init__(self, x):
        # dfs
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        recursion

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
