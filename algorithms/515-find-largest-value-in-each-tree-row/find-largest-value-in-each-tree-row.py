"""
515. find largest value in each tree row

https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/

在每个树行中找最大值
"""

import collections
from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


def largest_values(root: TreeNode) -> List[int]:
    """
    借助队列实现层序遍历
    See LeetCode 102
    """
    if root is None:
        return []

    queue = collections.deque()
    queue.append(root)

    ans = []

    while len(queue) != 0:
        cur_level_size = len(queue)

        node = queue.popleft()
        cur_level_max = node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

        cur_level_size -= 1

        for _ in range(cur_level_size):
            node = queue.popleft()
            cur_level_max = max(node.val, cur_level_max)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        ans.append(cur_level_max)

    return ans
