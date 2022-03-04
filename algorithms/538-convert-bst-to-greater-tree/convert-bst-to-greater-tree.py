"""
538. convert bst to greater tree

https://leetcode.com/problems/convert-bst-to-greater-tree
https://leetcode-cn.com/problems/convert-bst-to-greater-tree

把二叉搜索树转换为累加树
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    """
    二叉搜索树的性质，左节点 < 根 < 右节点
    """

    def convertBST(self, root: TreeNode) -> TreeNode:
        arr: List[TreeNode] = []
        self.traversal(root, arr)

        # 累加
        for i in range(1, len(arr)):
            arr[i].val += arr[i - 1].val

        return root

    def traversal(self, node: TreeNode, arr: List[TreeNode]):
        """
        反序中序遍历
        """
        if node:
            # 先右节点
            if node.right:
                self.traversal(node.right, arr)
            # 其次根节点
            arr.append(node)
            # 最后左节点
            if node.left:
                self.traversal(node.left, arr)


class Solution2:

    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        反中序遍历：递归

        Complexity Analysis
        time complexity: O(n)
        space complexity: O(n)（递归调用保存栈帧所需要的空间）
        """
        if root is not None:
            # 将右子树转换为累加树
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)

        return root


class Solution3:

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        反中序遍历：基于栈

        Complexity Analysis
        time complexity: O(n)
        space complexity: O(n)（栈所需要的空间）
        """
        total = 0
        stack = []
        node = root
        while stack or node is not None:
            while node is not None:
                # 总是先遍历右节点，确保降序遍历
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left

        return root


class Solution4:

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        反序中序 Morris
        """

        def get_successor(node: TreeNode):
            """
            get the node with the smallest value than this one
            """
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root
