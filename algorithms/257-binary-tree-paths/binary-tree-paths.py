"""
257. binary tree paths

二叉树的所有路径
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        ans = []

        def dfs(node: TreeNode, path: str):
            """
            DFS
            :param node: current node
            :param path: the path from root to current node
            """
            if node.left is None and node.right is None:
                ans.append(path)
            if node.left is not None:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right is not None:
                dfs(node.right, path + '->' + str(node.right.val))

        dfs(root, str(root.val))
        return ans
