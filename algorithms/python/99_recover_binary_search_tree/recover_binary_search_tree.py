"""
99. recover binary search tree

恢复二叉搜索树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    """
    递归



    Complexity Analysis
    time complexity: O(N)
    space complexity: O(N)
    """

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            pass

    def internal(self, node, left: bool):
        """
        以 node 为根节点，返回其左子树中的最大节点或者右子树中的最小节点
        """
        if left:
            if node.left is not None:
                left_node = self.internal(node.left, True)
                if left_node.val > node.val:
                    # change
                    left_node.val, node.val = node.val, left_node.val
                    return left_node
        else:
            if node.right is not None:
                right_node = self.internal(node.left, False)
                if right_node.val < node.val:
                    # change
                    right_node.val, node.val = node.val, right_node.val
                    return right_node

        return node
