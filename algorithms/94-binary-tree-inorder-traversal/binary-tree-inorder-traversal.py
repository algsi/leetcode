"""
94. binary tree inorder traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

二叉树的中序遍历
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        self.inorder_traversal_internal(root, ans)
        return ans

    def inorder_traversal_internal(self, node: TreeNode, ans: List[int]):
        """
        recursion
        """
        if node.left is not None:
            self.inorder_traversal_internal(node.left, ans)

        ans.append(node.val)

        if node.right is not None:
            self.inorder_traversal_internal(node.right, ans)

    def inorder_traversal_2(self, root: TreeNode) -> List[int]:
        """
        non-recursive
        """
        if root is None:
            return []
        stack = []
        ans = []
        cur = root
        while cur is not None or len(stack) != 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans
