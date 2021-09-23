"""
1O2. binary tree level order traversal

二叉树的层序遍历
"""

import collections
from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


def level_order(root: TreeNode) -> List[List[int]]:
    """
     广度优先搜索

     complexity analysis
     time complexity: O(n)
     space complexity: O(n)
    """
    if root is None:
        return []

    queue = [(0, root)]  # 队列中的元素为元组，元素第一个值表示节点的所在的层标识，第二个元素指示节点
    ans: List[List[int]] = []
    while len(queue) != 0:
        level, node = queue.pop(0)  # 出队
        if len(ans) <= level:
            ans.append([node.val])
        else:
            ans[level].append(node.val)

        # 子节点的层标识加一
        if node.left is not None:
            queue.append((level + 1, node.left))
        if node.right is not None:
            queue.append((level + 1, node.right))

    return ans


def level_order_2(root: TreeNode) -> List[List[int]]:
    """
    优化：不必再去判断每个节点的层级
    """
    if root is None:
        return []

    # 节点队列
    queue = collections.deque()
    queue.append(root)

    ans = []
    while queue:
        # 当前层节点数量
        cur_level_size = len(queue)
        ans.append([])

        # 依次从队列中取当前层所有元素进行拓展，然后进入下一层迭代
        for _ in range(cur_level_size):
            # 弹出最先入队列的节点
            node = queue.popleft()
            ans[-1].append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return ans
