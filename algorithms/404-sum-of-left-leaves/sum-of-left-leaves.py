"""
404. sum of left leaves

左叶子之和
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Recursion

    注意：一定要是叶子节点，非叶子节点不需要加和
    """

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            res += root.left.val
        return res + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
