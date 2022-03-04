"""
113. path sum ii

路径总和 II
"""

from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    DFS
    """

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(node: TreeNode, target: int):
            if not node:
                return

            path.append(node.val)
            target -= node.val

            if target == 0 and node.left is None and node.right is None:
                ans.append(path.copy())
                path.pop()
                return

            # try left
            if node.left is not None:
                dfs(node.left, target)

            # try right
            if node.right is not None:
                dfs(node.right, target)

            path.pop()

        dfs(root, sum)

        return ans


class Solution2:
    """
    BSF
    """

    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        ret = list()
        # 哈希表构建从子节点懂啊父节点的关系
        parent = collections.defaultdict(lambda: None)

        def get_path(node: TreeNode):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = parent[node]
            # 逆序
            ret.append(tmp[::-1])

        if not root:
            return ret

        # 两个队列，一个存节点，一个存路径和
        queue_node = collections.deque([root])
        queue_total = collections.deque([0])

        while queue_node:
            node = queue_node.popleft()
            rec = queue_total.popleft() + node.val

            if not node.left and not node.right:
                if rec == total:
                    get_path(node)
            else:
                if node.left:
                    # 构建父子关系
                    parent[node.left] = node
                    queue_node.append(node.left)
                    # 记录路径和
                    queue_total.append(rec)
                if node.right:
                    # 构建父子关系
                    parent[node.right] = node
                    queue_node.append(node.right)
                    # 记录路径和
                    queue_total.append(rec)

        return ret
