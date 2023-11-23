"""
111. minimum depth of binary tree

二叉树的最小深度
"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


def min_depth(root: TreeNode) -> int:
    """
    BFS
    """
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    level = 1
    count = 1
    while len(queue) > 0:
        while count > 0:
            node = queue.popleft()
            if node.left is None and node.right is None:
                return level
            count -= 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        count = len(queue)
        level += 1

    return level
