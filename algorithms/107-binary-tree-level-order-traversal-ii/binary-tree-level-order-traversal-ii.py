"""
107. binary tree level order traversal ii

二叉树的层次遍历 II
"""

from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_bottom(root: TreeNode) -> List[List[int]]:
    """
    在 Python 中，我们需要返回一个 list，它不方便在头部插入元素，所以我们可以先用尾部插入的方式得到从上到下的层次遍历列表，然后
    反转。

    在 Java 中，由于我们需要返回的 List 是一个接口，这里可以使用链表实现，方便在头部插入元素。
    """
    level_order = []
    if root is None:
        return level_order
    q = collections.deque([root])
    while q:
        level = []
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level_order.append(level)

    return level_order[::-1]
