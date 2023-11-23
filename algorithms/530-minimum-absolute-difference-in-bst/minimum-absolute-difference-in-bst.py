"""
530. minimum absolute difference in bst

https://leetcode.com/problems/minimum-absolute-difference-in-bst/
https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/

二叉搜索树的最小绝对差
"""

"""
二叉搜索树的性质：

1. 节点右子树上任意一个节点，大于左子树上任意一个节点。
2. 二叉搜索树中序遍历得到的值序列是递增有序的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    中序遍历 + 空间优化
    """

    def getMinimumDifference(self, root: TreeNode) -> int:

        def dfs(node):
            nonlocal res, pre

            if node is None:
                return

            # 中序遍历，先遍历左子树
            dfs(node.left)
            if pre != -1:
                # node.val 始终大于等于 pre
                res = min(res, node.val - pre)

            pre = node.val
            # 中序右子树
            dfs(node.right)

        pre = -1  # 使用 pre 来保留中序遍历序列前一个节点的值，从而省去了用数组来存储中序遍历的结果
        res = float('inf')
        dfs(root)
        return int(res)
