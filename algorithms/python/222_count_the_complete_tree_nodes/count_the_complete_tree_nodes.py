"""
222. count the complete tree nodes

https://leetcode.com/problems/count-complete-tree-nodes/
https://leetcode-cn.com/problems/count-complete-tree-nodes/

完全二叉树的节点个数
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """
    广度优先搜索 or 深度优先搜索

    对于任意二叉树，都可以通过广度优先搜索或深度优先搜索计算节点个数，时间复杂度和空间复杂度都是 O(n)，其中 nn 是二叉树的节点个数。
    """

    def count_nodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.count_nodes(root.left) + self.count_nodes(root.right) + 1


class Solution2:
    """
    二分查找 + 位运算
    """

    def count_nodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        level = 0  # level begin at 0
        node = root
        while node.left is not None:
            level += 1
            node = node.left
        low = 1 << level
        high = (1 << (level + 1)) - 1
        while low < high:
            # 当 high = low + 1时，mid 必须取 high，否则会造成死循环
            mid = (high - low + 1) // 2 + low
            if self.exists(root, level, mid):
                low = mid
            else:
                high = mid - 1

        return low

    @staticmethod
    def exists(root: TreeNode, level: int, k: int) -> bool:
        bits = 1 << (level - 1)
        node = root
        while node is not None and bits > 0:
            if bits & k == 0:
                node = node.left
            else:
                node = node.right
            bits >>= 1
        return node is not None
