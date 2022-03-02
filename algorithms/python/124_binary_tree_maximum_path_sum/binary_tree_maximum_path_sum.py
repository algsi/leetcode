"""
124 binary tree maximum path sum

二叉树中的最大路径和
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def max_gain(node: TreeNode) -> int:
        if node is None:
            return 0
        # 递归计算左右子节点的最大贡献值
        # 只有在最大贡献值大于 0 时，才会选取对应子节点
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        price_new_path = node.val + left_gain + right_gain

        # 更新答案
        nonlocal max_sum
        max_sum = max(max_sum, price_new_path)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return int(max_sum)
