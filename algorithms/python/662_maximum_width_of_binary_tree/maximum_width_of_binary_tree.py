"""
662. maximum width of binary tree

https://leetcode-cn.com/problems/maximum-width-of-binary-tree/

二叉树的最大宽度
"""

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


def width_of_binary_tree(root: TreeNode) -> int:
    """
    计算二叉树的最大宽度

    BFS，用队列实现二叉树的层序遍历

    该算法会超时，原因是遇到很多空节点时没有剪枝
    """
    if root is None:
        return 0

    q = collections.deque()
    q.append(root)
    max_width = 1

    has_next_level = True
    while has_next_level:

        level_size = len(q)

        cur_level_width = 0
        none_count = 0
        has_next_level = False
        print(level_size)
        for _ in range(level_size):
            node = q.popleft()

            if node is None:
                q.append(None)
                q.append(None)
                if cur_level_width != 0:
                    none_count += 1
            else:
                q.append(node.left)
                q.append(node.right)
                if not has_next_level:
                    has_next_level = (node.left is not None) or (node.right is not None)
                cur_level_width += 1
                cur_level_width += none_count
                none_count = 0

        max_width = max(max_width, cur_level_width)

    return max_width


def width_of_binary_tree_2(root: TreeNode) -> int:
    """
    计算二叉树的最大宽度

    BFS
    广度优先搜索顺序遍历每个节点的过程中，我们记录节点的 position 信息，对于每一个深度，第一个遇到的节点是最左边的节点，最后一个到达的节点是最右边的节点。
    """
    queue = [(root, 0, 0)]
    cur_depth, left, ans = 0, 0, 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth + 1, pos * 2))
            queue.append((node.right, depth + 1, pos * 2 + 1))

            # a new level
            if cur_depth != depth:
                cur_depth = depth
                left = pos

            ans = max(ans, pos - left + 1)

    return ans


class Solution:
    def width_of_binary_tree_3(self, root: TreeNode) -> int:
        """
        DFS
        """

        # 存储每一层第一个非空节点的position
        left = {}
        self.ans = 0

        def dfs(node: TreeNode, depth: int = 0, pos: int = 0):
            if node is not None:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, 2 * pos)
                dfs(node.right, depth + 1, 2 * pos + 1)

        dfs(root, 0, 0)
        return self.ans
