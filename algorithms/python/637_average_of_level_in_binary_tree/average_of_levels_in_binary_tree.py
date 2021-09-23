"""
637. average of levels in binary tree

二叉树的层平均值
"""

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


def average_of_levels(root: TreeNode) -> List[float]:
    """
    Queue
    """
    ans = []
    queue = deque([root])
    counter = 1
    while len(queue) > 0:
        sum_level, tmp = 0, counter
        while counter > 0:
            node = queue.popleft()
            sum_level += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            counter -= 1
        ans.append(sum_level / tmp)
        counter = len(queue)

    return ans
