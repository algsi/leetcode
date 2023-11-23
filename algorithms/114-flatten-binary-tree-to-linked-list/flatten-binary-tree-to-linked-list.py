"""
114. flatten binary tree to linked list

https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

二叉树展开为链表
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    """
    递归 + 前序遍历
    """

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        # 展开二叉树
        self.internal(root)

    def internal(self, node: TreeNode):
        """
        返回二叉树展开后，最后一个节点的引用
        """
        left_last, right_last = None, None
        if node.left is not None:
            # 展开左子树
            left_last = self.internal(node.left)

        if node.right is not None:
            # 展开右子树
            right_last = self.internal(node.right)

        # 进行合并
        if left_last is None:
            if right_last is None:
                return node
            else:
                return right_last
        else:
            left_last.right = node.right
            node.right = node.left

        node.left = None
        right_last = right_last if right_last is not None else left_last

        return right_last


class Solution2:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        cur = root
        while cur:
            if cur.left:
                predecessor = cur.left
                # 寻找左子树的最右节点
                while predecessor.right:
                    predecessor = predecessor.right
                # 让左子树的最右节点的右指针指向当前节点的右节点，完成拼接
                predecessor.right = cur.right

                cur.right = cur.left
                cur.left = None

            # 下一个节点
            cur = cur.right
