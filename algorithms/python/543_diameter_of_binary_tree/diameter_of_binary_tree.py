"""
543. diameter of binary tree

二叉树的直径
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        """
        DFS

        任意一条路径均可以被看作由某个节点为起点，从其左儿子和右儿子向下遍历的路径拼接得到。
        """
        self.ans = 0

        def depth(node: TreeNode) -> int:
            """
            闭包递归函数

            :return: 返回从当前节点出发到以该节点为根节点的树的任意一个结点路径长度中的最大值
            """
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 0

            left_length = depth(node.left)
            right_length = depth(node.right)

            # 左子节点和右子节点的路径拼接
            if node.left is None:
                self.ans = max(self.ans, right_length + 1)
            elif node.right is None:
                self.ans = max(self.ans, left_length + 1)
            else:
                self.ans = max(self.ans, left_length + right_length + 2)

            return max(left_length, right_length) + 1

        depth(root)
        return self.ans
